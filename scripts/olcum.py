#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insanca · sayısal denetim (numeric audit)

Counts the measurable features of a Turkish text that often show up in AI-written prose.
It does not give a verdict like a detector would. Thresholds are alarm bells, not targets.

Adapted from scripts/audit.py of "İnsanlık öldü mü?" by MesutARIDORU
(https://github.com/MesutARIDORU/insanlik-oldu-mu, MIT License, Copyright (c) 2026 MesutARIDORU).
Changes for insanca: guide files point to references/turler.md and references/alanlar.md,
sentence-length CV thresholds follow insanca's Sayısal Denetim (alarm < 0.35, ok >= 0.40) and
are computed from 3 sentences up, any circumflexed letter is flagged (§32), saved texts live
under the "insanca" temp folder.

Usage:
  python3 olcum.py text.txt
  python3 olcum.py new.txt --before old.txt     # before → after comparison
  python3 olcum.py text.txt --json              # machine-readable output
  python3 olcum.py text.txt --guide             # also print the writing guides for the guessed genre and sector
  python3 olcum.py --guide "Şiir dili"          # print the writing guide for a given genre
  python3 olcum.py --guide "Finans"             # ...or for a given sector

Texts can come from standard input and be kept under a short name, so the agent never has to
write files of its own (in Claude Code that would ask for approval every time):
  python3 olcum.py - --save once --guide <<'METIN'
  ...original text...
  METIN
  python3 olcum.py - --save sonra --before once <<'METIN'
  ...rewritten text...
  METIN

Uses only the Python 3 standard library.
"""

import argparse
import json
import os
import re
import statistics
import sys
import tempfile
from collections import Counter

# ---------------------------------------------------------------- helpers

def tr_lower(s):
    """Lowercases with Turkish rules (I → ı, İ → i)."""
    return s.replace("I", "ı").replace("İ", "i").lower()


VOWELS = set("aeıioöuüâîû")
WORD_RE = re.compile(r"[^\W\d_]+(?:['’][^\W\d_]+)*|\d+(?:[.,]\d+)*(?:['’][^\W\d_]+)?")
LETTER_RE = re.compile(r"[^\W\d_]")

ABBREVIATIONS = {
    "dr", "prof", "doç", "yrd", "av", "sn", "bkz", "vb", "vs", "örn", "no", "st",
    "op", "uzm", "alb", "gen", "yy", "sf", "s", "c", "ltd", "şti", "inc", "co",
    "mr", "mrs", "ms", "jr", "sr", "ör", "çev", "haz", "ed", "der",
}


def words(s):
    return WORD_RE.findall(s)


def count_syllables(word):
    # In Turkish the syllable count equals the vowel count.
    return sum(1 for ch in tr_lower(word) if ch in VOWELS)


def count_terms(terms, lower_text):
    """Counts occurrences of each term that start at a word boundary."""
    found = Counter()
    for t in terms:
        n = len(re.findall(r"(?<!\w)" + re.escape(t), lower_text))
        if n:
            found[t] = n
    return found


# ---------------------------------------------------------------- word lists

AI_WORDS = [
    "kapsamlı", "bütüncül", "kilit rol", "kilit bir", "yenilikçi", "dönüştürücü",
    "vazgeçilmez", "benzersiz", "eşsiz", "büyüleyici", "göz kamaştır", "değer kat",
    "katkı sağla", "katkıda bulun", "olanak tanı", "olanak sağla", "imkan sun", "imkân sun",
    "ışık tut", "altını çiz", "gözler önüne ser", "hayata geçir", "önem arz",
    "büyük önem taşı", "kritik bir rol", "kritik öneme", "kritik bir öneme", "her zamankinden daha", "önemli bir rol", "dönüm noktası",
    "çığır aç", "devrim niteliğinde", "oyun değiştirici", "oyunun kurallarını",
    "derinlemesine", "dinamik dünya", "günün sonunda", "goblen", "unutulmaz bir deneyim",
    "sizi bekliyor", "potansiyelini", "ezber boz", "fark yarat", "yolculuğun", "yolculuğu",
]

TECH_BUZZWORDS = [
    "dijital dönüşüm", "uçtan uca", "ölçeklenebilir", "sorunsuz", "kesintisiz deneyim",
    "yapay zeka destekli", "yapay zekâ destekli", "yapay zeka odaklı", "veri odaklı",
    "inovasyon", "inovatif", "çözüm ortağı", "değer önerisi", "çevik", "akıllı çözüm",
    "yeni nesil", "son teknoloji", "en son teknoloji", "entegre çözüm", "optimize et",
    "optimizasyon", "verimliliği artır", "iş süreçlerini", "dijitalleş", "ekosistem",
    "sinerji", "geleceğe hazır", "çığır açan", "paradigma", "katma değer",
]

BUREAUCRATIC = [
    "bağlamında", "çerçevesinde", "doğrultusunda", "ilişkin", "itibariyle", "itibarıyla",
    "kapsamında", "noktasında", "sürecinde", "yönelik",
]

FILLER = [
    "önemle belirtmek", "belirtmek gerekir", "unutulmamalıdır", "şunu söylemek mümkün",
    "dikkat edilmesi gereken", "göz ardı edilmemeli", "etkili bir şekilde",
    "imkanına sahip", "imkânına sahip", "olduğu söylenebilir", "olabileceği düşünül",
    "bu noktada", "söylemek gerekirse",
]

CHAT_LEFTOVERS = [
    "bir yapay zeka", "bir yapay zekâ", "dil modeli olarak", "umarım yardımcı olur",
    "umarım faydalı olur", "regenerate response", "başka sorunuz olursa",
    "yardımcı olabileceğim başka", "harika bir soru", "çok güzel bir soru",
    "dilerseniz devam", "devam etmemi ister",
]

# correspondence clichés: mostly word-for-word translations of English e-mail formulas
MAIL_CLICHES = [
    ("umarım bu e-posta sizi iyi bulur", r"umarım bu (e-?posta|mesaj|ileti)\w* sizi iyi bul"),
    ("iletişime geçmekten çekinmeyin", r"iletişime geçmekten çekinmeyin|çekinmeden (benimle |bizimle )?iletişime geç"),
    ("…ile ilgili olarak iletişime geçmek istedim", r"ilgili olarak (sizinle )?iletişime geçmek ist"),
    ("ekte … bulabilirsiniz", r"ekte[^.!?\n]{0,80}bulabilirsiniz"),
    ("herhangi bir sorunuz olursa", r"herhangi bir (soru|sorunuz)[^.!?\n]{0,20}(olursa|olması durumunda)"),
    ("bu e-postayı … amacıyla yazıyorum", r"bu (e-?postayı|mesajı)[^.!?\n]{0,60}(amacıyla|için) (yazıyorum|kaleme aldım)"),
]

CLICHE_OPENINGS = [
    "günümüzde", "günümüz dünyasında", "günümüzün", "çağımızda", "dijital çağda", "dijital dünyasında",
    "hızla gelişen", "hızla değişen",
    "hepimizin bildiği gibi", "son yıllarda", "teknolojinin hızla",
]

CLICHE_CLOSINGS = [
    "sonuç olarak", "özetle", "kısacası", "uzun lafın kısası", "velhasıl",
    "parlak bir gelecek", "peki siz", "peki ya siz", "siz de bu", "unutmayın",
    "belki de asıl",
]

CONNECTIVE_OPENERS = [
    "aynı zamanda", "ayrıca", "bu bağlamda", "bu çerçevede", "bu doğrultuda", "buna ek olarak",
    "bununla birlikte", "bunun yanı sıra", "dahası", "dolayısıyla", "ek olarak", "kısacası",
    "öte yandan", "özetle", "sonuç olarak", "üstelik",
]

OFFICE_JARGON = [
    "feedback", "aksiyon al", "challenge", "deploy", "production", "sprint", "task",
    "deadline", "update", "brief", "insight", "meeting", "follow", "case", "target",
    "timeline", "roadmap", "onboarding", "kick-off", "sync", "approve", "set et",
    "check et", "focus", "efor", "proaktif", "networking", "mindset", "skill",
]

OVER_TRANSLATIONS = [
    "konuşlandır", "çekme isteği", "birleştirme isteği", "taahhüt et", "ara katman yazılımı",
    "istem mühendisliği", "ince ayarlama", "dal oluştur", "sürekli entegrasyon ve sürekli",
]

# aorist (geniş zaman) at the end of a sentence: yapar, gösterir, olur, olurlar, yaparsın, gerekmez (§56)
AORIST_END_RE = re.compile(
    r"(?:[ıiuü]r|[ae]r)(?:[ıiuü]m|s[ıiuü]n|[ıiuü]z|s[ıiuü]n[ıiuü]z|l[ae]r)?$"
    r"|m[ae]z(?:s[ıi]n|s[ıi]n[ıi]z|l[ae]r)?$"
)
# endings that look like the aorist but are not the hollow kind §56 is about
NOT_AORIST_RE = re.compile(
    r"[dt][ıiuü]r(?:l[ae]r)?$"          # copula -dır/-tır: counted as -dır family
    r"|[ae]bil[ıi]r\w*$"                 # -abilir: the ability form §56 recommends
)
# nouns, adjectives and particles that end like an aorist
AORIST_STOPWORDS = {
    "var", "kadar", "yer", "bir", "her", "biraz", "zarar", "karar", "haber", "eser", "ayar", "fikir",
    "şehir", "seyir", "emir", "sır", "onur", "gurur", "huzur", "tür", "kür", "hür", "asır", "bahar",
    "pazar", "dolar", "nadir", "hazır", "kader", "defter", "şeker", "süper", "server", "poster", "user",
    "bilgisayar", "kayır", "rahmetler", "teşekkürler", "tebrikler", "selamlar", "sevgiler", "evler",
    "yalnız", "hiç", "beraber", "değer", "ömür", "kar", "kâr", "zor", "mor",
}


def is_aorist(word):
    """True when a sentence-final word looks like a hollow aorist verb (§56). A heuristic, not a parser."""
    if len(word) < 3 or word in AORIST_STOPWORDS or NOT_AORIST_RE.search(word):
        return False
    # plural nouns end in -lar/-ler too ("kitaplar"); keep only aorist + -lar ("olurlar", "yapmazlar")
    if re.search(r"l[ae]r$", word) and not re.search(r"(?:[ıiuüae]r|m[ae]z)l[ae]r$", word):
        return False
    return bool(AORIST_END_RE.search(word))


CONTRAST = ["ama", "ancak", "fakat", "lakin", "oysa", "yine de"]
ADDITION = ["ve", "ayrıca", "hem", "üstelik"]

LABEL_PATTERN = re.compile(
    r"(?<!\w)(şu|şudur|şöyle|basit|net|açık|asıl \w+|sorun|mesele|cevap|yanıt|sır|fark|"
    r"ders|gerçek|kural|soru|sonuç|özet|işin aslı|ortak nokta)\s*(şu|şudur)?\s*:"
)

EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF\U00002B00-\U00002BFF]"
)

CAPITALIZED_CONJUNCTIONS = {"Ve", "İle", "Veya", "Ya", "Yahut", "Ki", "Da", "De", "Mı", "Mi", "Mu", "Mü",
                            "Mısın", "Misin", "Musun", "Müsün"}

STOPWORDS = set("""ve ile ama ancak fakat için gibi kadar daha çok en bir bu şu o da de ki mi mı mu mü
ne ya veya hem her şey olan olarak oldu olur olmak gibi sonra önce ise yani diye bunu buna bunun
onun ona onu biz siz ben sen onlar bizim sizin benim artık bile hiç değil var yok""".split())


# ---------------------------------------------------------------- parsing

def parse(text):
    """Splits the text into headings, paragraphs and sentences; counts formatting marks."""
    raw = text
    text = re.sub(r"```.*?```", "\n", text, flags=re.S)

    headings = []
    dialogue_lines = 0
    blocks, block = [], []
    for line in text.splitlines():
        st = line.strip()
        if not st:
            if block:
                blocks.append(block)
                block = []
            continue
        if re.match(r"#{1,6}\s", st):
            headings.append(re.sub(r"^#{1,6}\s+", "", st))
            if block:
                blocks.append(block)
                block = []
            continue
        st = re.sub(r"^>\s?", "", st)
        is_item = bool(re.match(r"^([-*+•]|\d+[.)])\s+", st))
        st = re.sub(r"^([-*+•]|\d+[.)])\s+", "", st)
        if re.match(r"^[—–]\s*", st):  # dialogue dash at line start
            dialogue_lines += 1
            st = re.sub(r"^[—–]\s*", "", st)
        block.append((st, is_item))
    if block:
        blocks.append(block)
    kept, frame_lines = strip_correspondence_frame(blocks)
    frame_words = sum(len(words(line)) for b in blocks for line, _ in b) - sum(len(words(line)) for b in kept for line, _ in b)
    blocks = kept

    paragraphs, sentences, paragraph_sentences = [], [], []
    for b in blocks:
        if any(m for _, m in b) or len(b) > 1 and all(len(words(s)) < 12 for s, _ in b):
            parts = [s for s, _ in b]  # list or dialogue: every line is its own unit
        else:
            parts = [" ".join(s for s, _ in b)]
        paragraphs.append(" ".join(parts))
        ps = []
        for part in parts:
            ps.extend(split_sentences(part))
        paragraph_sentences.append(ps)
        sentences.extend(ps)

    return {
        "raw": raw,
        "plain": "\n\n".join(paragraphs),
        "headings": headings,
        "paragraphs": paragraphs,
        "paragraph_sentences": paragraph_sentences,
        "sentences": sentences,
        "dialogue_lines": dialogue_lines,
        "frame_lines": frame_lines,
        "frame_words": frame_words,
    }


GREETING_LINE_RE = re.compile(r"^(merhaba|sayın|değerli|selam|herkese merhaba|iyi günler|günaydın|sevgili)\b[^.!?]{0,60}[,!:]?$")
CLOSING_LINE_RE = re.compile(r"^(saygılarımla|saygılarımızla|iyi çalışmalar|teşekkürler|teşekkür ederim|sevgiler|kolay gelsin|selamlar|en iyi dileklerimle)\b[^.!?]{0,30}[,.!]?$")


def strip_correspondence_frame(blocks):
    """Removes a letter's frame (greeting line, closing line and the signature below it).

    These short lines are conventions, not prose: counted as sentences they would trigger
    the short-sentence and same-opening alarms in every e-mail.
    """
    removed = 0
    if blocks and len(blocks[0]) == 1:
        first = tr_lower(blocks[0][0][0])
        if len(words(first)) <= 8 and GREETING_LINE_RE.match(first):
            removed += 1
            blocks = blocks[1:]
    for b in range(max(0, len(blocks) - 2), len(blocks)):
        for i, (line, _) in enumerate(blocks[b]):
            if len(words(line)) <= 5 and CLOSING_LINE_RE.match(tr_lower(line)):
                removed += len(blocks[b]) - i + sum(len(x) for x in blocks[b + 1:])
                blocks = blocks[:b] + ([blocks[b][:i]] if i else [])
                return blocks, removed
    return blocks, removed


END_RE = re.compile(r"([.!?…]+[\"”’»)]*)(\s+)")


def split_sentences(p):
    p = p.replace("**", "").replace("__", "")
    parts, start = [], 0
    for m in END_RE.finditer(p):
        following = p[m.end():m.end() + 1]
        mark = m.group(1)
        if following and following.islower():
            continue  # "19. yüzyıl", "vb. ile", "gitti... ve"
        if mark == ".":
            previous = re.findall(r"[^\s(]+$", p[start:m.start(1)])
            if previous and tr_lower(previous[0]).strip(".") in ABBREVIATIONS:
                continue
        part = p[start:m.end(1)].strip()
        if part:
            parts.append(part)
        start = m.end()
    rest = p[start:].strip()
    if rest:
        parts.append(rest)
    return [s for s in parts if words(s)]


# ---------------------------------------------------------------- measurement

def longest_run(seq, cond):
    best, current = 0, 0
    for i in range(len(seq)):
        if cond(i):
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best


def measure(text):
    a = parse(text)
    sentences = a["sentences"]
    paragraphs = a["paragraphs"]
    plain = a["plain"]
    lower = tr_lower(plain)
    all_words = words(plain)
    lettered = [w for w in all_words if LETTER_RE.search(w)]
    n_words = len(all_words) + a["frame_words"]  # the letter's frame is not prose but still part of the word count
    n_sentences = max(1, len(sentences))
    per_thousand = 1000 / max(1, n_words)

    lengths = [len(words(s)) for s in sentences] or [0]
    mean = statistics.mean(lengths)
    std = statistics.pstdev(lengths) if len(lengths) > 1 else 0.0
    cv = std / mean if mean else 0.0

    short_chain = longest_run(lengths, lambda i: lengths[i] <= 5)
    equal_run = 1
    current = 1
    for i in range(1, len(lengths)):
        if lengths[i] >= 10 and lengths[i - 1] >= 10 and abs(lengths[i] - lengths[i - 1]) <= 3:
            current += 1
            equal_run = max(equal_run, current)
        else:
            current = 1

    # long and short sentences side by side within a paragraph
    eligible_p, contrast_p = 0, 0
    for ps in a["paragraph_sentences"]:
        if len(ps) >= 3:
            eligible_p += 1
            pl = [len(words(s)) for s in ps]
            if min(pl) <= 8 and max(pl) >= 20:
                contrast_p += 1

    p_lengths = [len(words(p)) for p in paragraphs]
    p_cv = (statistics.pstdev(p_lengths) / statistics.mean(p_lengths)) if len(p_lengths) >= 4 and statistics.mean(p_lengths) else None

    # sentence openings
    openings = []
    for s in sentences:
        w = words(s)
        openings.append(tr_lower(w[0]) if w else "")
    opening_counts = Counter(openings)
    top_opening, top_opening_n = (opening_counts.most_common(1)[0] if opening_counts else ("", 0))
    same_opening_run = longest_run(openings, lambda i: i > 0 and openings[i] == openings[i - 1]) + 1 if openings else 0
    connective_openers = 0
    for s in sentences:
        ls = tr_lower(s)
        if any(re.match(re.escape(c) + r"(?!\w)", ls) for c in CONNECTIVE_OPENERS):
            connective_openers += 1

    # sentence endings
    last_words = []
    for s in sentences:
        w = [x for x in words(s) if LETTER_RE.search(x)]
        last_words.append(tr_lower(w[-1]) if w else "")
    maktadir = sum(1 for w in last_words if re.search(r"m[ae]kt[ae]d[ıi]r(l[ae]r)?$", w))
    dir_family = sum(1 for w in last_words if re.search(r"[dt][ıiuü]r(l[ae]r)?$", w))
    aorist = sum(1 for w in last_words if is_aorist(w))
    olur = len(re.findall(r"(?<!\w)olur(?:lar)?(?!\w)", tr_lower(plain)))
    endings = Counter(w[-3:] for w in last_words if len(w) >= 3)
    rhyme_suffix, rhyme_n = (endings.most_common(1)[0] if endings else ("", 0))

    # converb tail (-arak/-erek in the second half of the sentence)
    converb_tail = 0
    for s in sentences:
        w = [tr_lower(x) for x in words(s)]
        for i, x in enumerate(w):
            if re.search(r"(arak|erek)$", x) and x != "olarak" and i >= len(w) / 2:
                converb_tail += 1
                break

    # punctuation
    em_dash = 0
    for line in text.splitlines():
        body = re.sub(r"^\s*(>\s*)?([-*+]\s+)?[—–]\s*", "", line)  # a dialogue dash at line start does not count
        em_dash += body.count("—") + len(re.findall(r"\s–\s", body)) + len(re.findall(r"\s--\s", body))
    semicolons = plain.count(";")
    colons = len(re.findall(r"(?<!\d):(?!\d)", plain))
    labeled_colons = len(LABEL_PATTERN.findall(lower))
    exclamations = plain.count("!")
    ellipses = len(re.findall(r"\.\.\.|…", plain))
    questions = plain.count("?")

    # word counts
    asil = len(re.findall(r"(?<!\w)asıl(?!\w)", lower))
    degil = len(re.findall(r"(?<!\w)değil", lower))
    not_only = len(re.findall(r"(sadece|yalnızca|yalnız)\b[^.!?]{0,80}?değil", lower))
    belki_de = len(re.findall(r"(?<!\w)belki de(?!\w)", lower))

    triads = 0
    for m in re.finditer(r"([^\s,.;:!?]+(?: [^\s,.;:!?]+){0,2}), ([^\s,.;:!?]+(?: [^\s,.;:!?]+){0,2}) (ve|veya|ya da|ile) ([^\s,.;:!?]+)", lower):
        before = lower[max(0, m.start() - 2):m.start()]
        if not before.endswith(", "):
            triads += 1

    ai = count_terms(AI_WORDS, lower)
    buzz = count_terms(TECH_BUZZWORDS, lower)
    bureau = count_terms(BUREAUCRATIC, lower)
    filler = count_terms(FILLER, lower)
    leftovers = count_terms(CHAT_LEFTOVERS, tr_lower(a["raw"]))
    raw_lower = tr_lower(a["raw"])
    mail = {label: len(re.findall(rx, raw_lower)) for label, rx in MAIL_CLICHES}
    mail = {k: v for k, v in mail.items() if v}

    first_sentences = tr_lower(" ".join(sentences[:2])) if sentences else ""
    opening_cliches = [t for t in CLICHE_OPENINGS if re.search(r"(?<!\w)" + re.escape(t), first_sentences)]
    office = count_terms(OFFICE_JARGON, lower)
    over = count_terms(OVER_TRANSLATIONS, lower)
    self_answer = 0  # a question immediately followed by its own short answer
    for i in range(len(sentences) - 1):
        if sentences[i].rstrip().endswith("?"):
            nxt = tr_lower(sentences[i + 1]).strip()
            answer_like = re.match(r"(cevap|yanıt|çünkü|basit|elbette|kesinlikle|tabii|evet|hayır)(?!\w)", nxt)
            short_verdict = len(words(nxt)) <= 4 and not nxt.endswith(("!", "?"))
            if answer_like or short_verdict:
                self_answer += 1
    last_p = tr_lower(paragraphs[-1]) if paragraphs else ""
    closing_cliches = [t for t in CLICHE_CLOSINGS if re.search(r"(?<!\w)" + re.escape(t), last_p)]
    question_ending = bool(sentences) and sentences[-1].rstrip().endswith("?")

    contrast = sum(len(re.findall(r"(?<!\w)" + re.escape(c) + r"(?!\w)", lower)) for c in CONTRAST)
    addition = sum(len(re.findall(r"(?<!\w)" + re.escape(c) + r"(?!\w)", lower)) for c in ADDITION)
    addition += len(re.findall(r"(?<!\w)(de|da|te|ta)(?!\w)", lower))

    # formatting
    bold = len(re.findall(r"\*\*[^*\n]+\*\*", a["raw"]))
    emoji = len(EMOJI_RE.findall(a["raw"]))
    circumflexed = re.findall(r"\w*[âîûÂÎÛ]\w*", plain)
    circumflex_mixed = sorted({w for w in circumflexed
                               if re.search(r"(?<!\w)" + re.escape(tr_lower(w).translate(str.maketrans("âîû", "aiu"))) + r"(?!\w)", lower)})
    heading_conjunctions = []
    for h in a["headings"]:
        tokens = h.split()
        heading_conjunctions += [t for t in tokens[1:] if t.strip(".,:;!?") in CAPITALIZED_CONJUNCTIONS]

    # overlap between the first and the last paragraph
    def stems(p):
        return {tr_lower(w)[:5] for w in words(p) if len(w) >= 4 and tr_lower(w) not in STOPWORDS and LETTER_RE.search(w)}
    overlap = None
    if len(paragraphs) >= 3:
        A, B = stems(paragraphs[0]), stems(paragraphs[-1])
        if A and B:
            overlap = len(A & B) / min(len(A), len(B))

    # readability (Ateşman)
    syllables = sum(count_syllables(w) for w in lettered)
    syl_per_word = syllables / max(1, len(lettered))
    words_per_sentence = len(all_words) / n_sentences  # prose only: the letter's frame has no sentences
    atesman = 198.825 - 40.175 * syl_per_word - 2.610 * words_per_sentence

    return {
        "words": n_words,
        "sentences": len(sentences),
        "paragraphs": len(paragraphs),
        "mean_sentence": round(mean, 1),
        "sentence_cv": round(cv, 2),
        "shortest": min(lengths),
        "longest": max(lengths),
        "short_chain": short_chain,
        "equal_length_run": equal_run,
        "contrast_paragraphs": f"{contrast_p}/{eligible_p}",
        "paragraph_cv": round(p_cv, 2) if p_cv is not None else None,
        "top_opening": top_opening,
        "top_opening_share": round(top_opening_n / n_sentences, 2),
        "same_opening_run": same_opening_run,
        "connective_opening_share": round(connective_openers / n_sentences, 2),
        "maktadir_share": round(maktadir / n_sentences, 2),
        "dir_family_share": round(dir_family / n_sentences, 2),
        "rhyme": f"-{rhyme_suffix}" if rhyme_suffix else "",
        "rhyme_share": round(rhyme_n / n_sentences, 2),
        "converb_tail_share": round(converb_tail / n_sentences, 2),
        "aorist_share": round(aorist / n_sentences, 2),
        "olur": olur,
        "em_dash": em_dash,
        "dialogue_lines": a["dialogue_lines"],
        "semicolons": semicolons,
        "colons": colons,
        "labeled_colons": labeled_colons,
        "exclamations": exclamations,
        "ellipses": ellipses,
        "questions": questions,
        "asil": asil,
        "degil": degil,
        "not_only": not_only,
        "belki_de": belki_de,
        "triads_per_thousand": round(triads * per_thousand, 1),
        "triads": triads,
        "ai_words": dict(ai),
        "tech_buzzwords": dict(buzz),
        "bureaucratic": dict(bureau),
        "filler": dict(filler),
        "chat_leftovers": dict(leftovers),
        "mail_cliches": mail,
        "frame_lines": a["frame_lines"],
        "cliche_opening": opening_cliches,
        "office_jargon": dict(office),
        "over_translations": dict(over),
        "self_answer": self_answer,
        "cliche_closing": closing_cliches,
        "question_ending": question_ending,
        "contrast_addition_ratio": round(contrast / addition, 2) if addition else None,
        "bold": bold,
        "emoji": emoji,
        "circumflexed": len(circumflexed),
        "circumflex_mixed": circumflex_mixed,
        "heading_conjunctions": heading_conjunctions,
        "first_last_overlap": round(overlap, 2) if overlap is not None else None,
        "syllables_per_word": round(syl_per_word, 2),
        "atesman": round(atesman, 1),
    }


# ---------------------------------------------------------------- text profile (genre and sector guess)

# Labels are Turkish because they are shown to the user as they are.
GENRE_LABELS = {
    "poetry": "Şiir dili",
    "literary": "Edebi anlatı dili",
    "essay": "Deneme ve köşe yazısı dili",
    "spec": "Teknik şartname dili",
    "docs": "Teknik doküman dili",
    "corporate": "Kurumsal yazışma dili",
    "academic": "Akademik dil",
    "legal": "Hukuki dil",
    "news": "Haber dili",
    "marketing": "Pazarlama dili",
    "social": "Sosyal medya dili",
    "personal": "Kişisel yazı dili",
}

SECTOR_KEYWORDS = {
    "yazılım ve teknoloji": ["yazılım", "uygulama", "sunucu", "api", "deploy", "sürüm", "kod", "veri taban", "bulut",
                             "kullanıcı arayüz", "arayüz", "sprint", "modül", "sistem", "platform", "node.js", "npm", "git"],
    "finans": ["bütçe", "faiz", "kredi", "yatırım", "portföy", "hisse", "bilanço", "nakit", "fatura", "ödeme", "tl", "lira"],
    "sağlık": ["hasta", "tedavi", "klinik", "ilaç", "doktor", "hastane", "teşhis", "semptom", "sağlık"],
    "eğitim": ["öğrenci", "öğretmen", "ders", "okul", "müfredat", "sınav", "eğitim", "üniversite"],
    "hukuk": ["sözleşme", "taraflar", "madde", "mahkeme", "dava", "kanun", "yükümlü", "kvkk", "hüküm"],
    "perakende ve e-ticaret": ["sipariş", "kargo", "sepet", "indirim", "kampanya", "stok", "mağaza", "ürün"],
    "kamu ve yerel yönetim": ["belediye", "bakanlık", "vatandaş", "valilik", "kamu", "büyükşehir"],
    "insan kaynakları": ["çalışan", "işe alım", "izin", "bordro", "performans", "aday", "mülakat"],
    "pazarlama ve iletişim": ["marka", "reklam", "kampanya", "müşteri deneyimi", "sosyal medya", "etkileşim"],
}
# Keywords match at the start of a word, since Turkish adds suffixes at the end. Short abbreviations match only
# as whole words (an apostrophe suffix is fine): otherwise "tl" is found in "işaretli" and "git" in "gitti".
WHOLE_WORD_KEYWORDS = {"tl", "git", "api", "npm"}
SECTOR_PATTERNS = {
    name: [re.compile(r"(?<!\w)" + re.escape(k) + (r"(?!\w)" if k in WHOLE_WORD_KEYWORDS else "")) for k in keys]
    for name, keys in SECTOR_KEYWORDS.items()
}

GREETING_RE = re.compile(r"^\s*(merhaba|sayın|değerli|selam|herkese merhaba|iyi günler|günaydın|sevgili)\b[^\n]{0,60}[,!:]?\s*$", re.M)
CLOSING_RE = re.compile(r"(saygılarımla|saygılarımızla|iyi çalışmalar|teşekkürler|teşekkür ederim|sevgiler|kolay gelsin|bilgilerinize)\s*[,.!]?\s*$", re.M)
REQUIREMENT_END_RE = re.compile(r"(m[ae]l[ıi]d[ıi]r|m[ae]l[ıi]|m[ae]m[ae]l[ıi]d[ıi]r|[ae]c[ae]kt[ıi]r|[ae]bilmelidir)[.;]?$")
UNIT_RE = re.compile(r"\b\d+(?:[.,]\d+)?\s?(ms|sn|saniye|dakika|mb|gb|kb|tb|mbps|gbps|°c|kg|mm|cm|kw|v|hz)\b", re.I)
NUMBERED_RE = re.compile(r"^\s*\d+(\.\d+)+\s", re.M)
IMPERATIVE_END_RE = re.compile(r"(y?[ıiuü]n|y?[ıiuü]n[ıiuü]z)[.:!]?$")
PAST_END_RE = re.compile(r"(d[ıiuü]|t[ıiuü]|m[ıiuü]ş|m[ıiuü]şt[ıiuü]|[ıiuü]yordu)(m|n|k|z|lar|ler)?[.!?…]?$")
FIRST_PERSON_RE = re.compile(r"(?<!\w)(ben|bence|bana göre|benim|sanırım|düşünüyorum|bana|beni)(?!\w)")
CITATION_RE = re.compile(r"\([A-ZÇĞİÖŞÜ][^()]{1,40},?\s\d{4}[a-z]?\)|\bvd\.|\bet al\.")
# Turkish drops pronouns, so person is read from verb and possessive suffixes
FIRST_SINGULAR_RE = re.compile(r"(d[ıiuü]m|t[ıiuü]m|[ıiuü]yorum|[ae]c[ae]ğ[ıi]m|m[ıiuü]ş[ıiuü]m|[ae]r[ıiuü]m)$")
FIRST_PLURAL_RE = re.compile(r"(d[ıiuü]k|t[ıiuü]k|[ıiuü]yoruz|[ae]c[ae]ğ[ıi]z|[ıiuü]m[ıiuü]z[ıiuü]?|[ıiuü]m[ıiuü]zl[ae]|[ıiuü]m[ıiuü]zd[ae]n)$")
SECOND_PLURAL_RE = re.compile(r"([ıiuü]n[ıiuü]z[ıiuü]?|[ıiuü]n[ıiuü]zd[ae]|[ıiuü]n[ıiuü]zl[ae]|s[ıiuü]n[ıiuü]z)$")
# common nouns and adjectives that only look like person suffixes
PERSON_SUFFIX_STOPWORDS = {
    "otomatik", "kritik", "politik", "estetik", "pratik", "teknik", "mantık", "elektrik", "istatistik", "matematik",
    "grafik", "müzik", "dinamik", "sistematik", "plastik", "romantik", "klasik", "fabrik", "lojistik", "analitik",
    "dağıtım", "adım", "yapım", "üretim", "satım", "yatırım", "kadim", "tutum", "kullanım", "bakım", "katılım",
}
DATELINE_RE = re.compile(r"^[A-ZÇĞİÖŞÜ]{3,}[^\n]{0,40}\([^)]{2,40}\)\s*[-–—]")


def guess_profile(text):
    """Guesses the text's genre and sector from surface signals.

    It is a hint for the agent, not a verdict: the agent reads the text and decides.
    Returns {genre, label, sector, confidence, evidence, scores}.
    """
    a = parse(text)
    raw = a["raw"]
    lower = tr_lower(raw)
    plain_lower = tr_lower(a["plain"])
    sentences = a["sentences"]
    n_sent = max(1, len(sentences))
    endings = [tr_lower(s.strip()) for s in sentences]
    last_words = [(words(e) or [""])[-1] + (e[-1] if e and e[-1] in ".;:!?" else "") for e in endings]
    lines = [l.strip() for l in re.sub(r"```.*?```", "", raw, flags=re.S).splitlines() if l.strip() and not l.strip().startswith("#")]
    score = {k: 0.0 for k in GENRE_LABELS}
    evidence = {k: [] for k in GENRE_LABELS}

    def add(genre, points, why):
        score[genre] += points
        if why and why not in evidence[genre]:
            evidence[genre].append(why)

    # poetry: many short lines that are not closed with sentence punctuation
    if len(lines) >= 4:
        short = sum(1 for l in lines if len(words(l)) <= 8)
        open_ended = sum(1 for l in lines if not re.search(r"[.!?…]$", l))
        if short / len(lines) >= 0.7 and open_ended / len(lines) >= 0.5:
            add("poetry", 4, "kısa, noktayla kapanmayan dizeler")
        stanzas = [b for b in re.split(r"\n\s*\n", raw.strip()) if b.strip()]
        if len(stanzas) >= 2 and all(2 <= len(b.strip().splitlines()) <= 8 for b in stanzas) and short / len(lines) >= 0.7:
            add("poetry", 2, "kıtalara ayrılmış")

    # essay, column and personal writing: the writer speaks as "I"
    tokens = [tr_lower(w) for w in words(raw) if len(w) >= 4 and tr_lower(w) not in PERSON_SUFFIX_STOPWORDS]
    fp = len(FIRST_PERSON_RE.findall(plain_lower))
    fs = sum(1 for w in tokens if FIRST_SINGULAR_RE.search(w))
    if fp >= 2:
        add("essay", min(fp, 6) * 0.5, "birinci kişiden görüş")
    if fs + fp >= 2:
        add("personal", min(fs + fp, 8) * 0.75, "birinci tekil kişi")

    # an institution speaking as "we" to the reader as "you": announcements and notices
    we = sum(1 for w in tokens if FIRST_PLURAL_RE.search(w))
    you = sum(1 for w in tokens if SECOND_PLURAL_RE.search(w))
    if we >= 2 and you >= 1:
        add("corporate", 1.0 + min(we + you, 6) * 0.15, "kurum ağzından okura seslenme")
    elif we >= 3:
        add("corporate", 1.0, "kurum ağzından anlatım")

    # literary narrative: dialogue, narrative past tense
    dialogue = a["dialogue_lines"] + len(re.findall(r"(?<!\w)(dedi|diye sordu|diye bağırdı|fısıldadı|diye düşündü)(?!\w)", lower))
    if dialogue >= 2:
        add("literary", 2 + min(dialogue, 6) * 0.5, "diyalog")
    past = sum(1 for w in last_words if PAST_END_RE.search(w))
    if past / n_sent >= 0.5 and len(sentences) >= 4 and not FIRST_PERSON_RE.search(plain_lower) and we < 2 and fs < 2:
        add("literary", 1.5, "üçüncü kişiyle geçmiş zaman anlatısı")

    # technical specification: requirement modals, numbering, units
    req = sum(1 for w in last_words if REQUIREMENT_END_RE.search(w.rstrip(".;:!?")))
    if req:
        add("spec", req / n_sent * 6, "\"-malıdır / -ecektir\" gereklilik kipi")
    if NUMBERED_RE.search(raw):
        add("spec", 1.5, "numaralı maddeler")
        add("legal", 0.5, "")
    units = len(UNIT_RE.findall(raw))
    if units:
        add("spec", min(units, 4) * 0.6, "ölçü birimleri")
    for w in ("gereksinim", "şartname", "kabul kriter", "desteklemelidir", "en az", "en fazla"):
        if w in lower:
            add("spec", 0.6, "")

    # technical documentation: code, commands, headings, imperative steps
    if "```" in raw or re.search(r"`[^`\n]+`", raw):
        add("docs", 2.5, "kod ve komutlar")
    if re.search(r"(?m)^\s*(\$ |npm |pip |git |python3? |brew |curl )", raw):
        add("docs", 1.5, "kabuk komutları")
    if a["headings"]:
        add("docs", 1, "başlıklar")
    imperative = sum(1 for w in last_words if IMPERATIVE_END_RE.search(w.rstrip(".:!")))
    if imperative >= 2:
        add("docs", min(imperative, 5) * 0.5, "adım adım emir kipi")
    docs_terms = sum(1 for w in ("kurulum", "yapılandır", "bağımlılık", "depo", "dal ", "komut", "sunucu", "ortam", "sürüm", "parametre", "yükleyin", "çalıştırın")
                     if w in lower)
    if docs_terms:
        add("docs", min(docs_terms, 5) * 0.5, "kurulum ve geliştirme terimleri")
    if imperative >= 1 and you >= 2 and we < 2:
        add("docs", 1.0, "okura adım adım yol gösterme")

    # corporate correspondence: greeting and closing
    greeting = GREETING_RE.search(raw[:200].lower() if raw else "")
    closing = CLOSING_RE.search(lower[-250:])
    if greeting:
        add("corporate", 2.5, "selamlama")
    if closing:
        add("corporate", 2.5, "kapanış")
    for w in ("ekte", "bilgilerinize", "toplantı", "geri dönüş", "rica eder", "şirketimiz", "tüm çalışanlar", "ekip arkadaş",
              "destek ekib", "yeni sürüm", "duyur", "kullanıcılarımız", "müşterilerimiz"):
        if w in lower:
            add("corporate", 0.7, "")

    # academic
    if CITATION_RE.search(raw):
        add("academic", 2.5, "kaynak gösterimi")
    for w in ("bu çalışmada", "bulgular", "yöntem", "literatür", "örneklem", "hipotez", "anlamlı fark", "araştırma"):
        if w in lower:
            add("academic", 0.8, "akademik terimler")

    # legal
    for w in ("işbu", "taraflar", "yükümlüdür", "sözleşme", "fesih", "tazminat", "hükümleri", "kanun"):
        if w in lower:
            add("legal", 1, "hukuk terimleri")

    # news
    if DATELINE_RE.search(raw.strip()):
        add("news", 3, "haber girişi")
    reported = len(re.findall(r"(açıkladı|bildirildi|belirtti|ifade edildi|açıklandı|kaydedildi|aktardı)(?!\w)", lower))
    if reported:
        add("news", min(reported, 4) * 0.8, "aktarım fiilleri")

    # marketing
    promo = len(re.findall(r"(?<!\w)(indirim|kampanya|fırsat|hemen|kaçırmayın|keşfedin|ücretsiz|sınırlı|sizi bekliyor|hazır olun)", lower))
    if promo:
        add("marketing", min(promo, 6) * 0.7, "satış çağrısı")
    if raw.count("!") >= 2:
        add("marketing", 0.5, "")
        add("social", 0.3, "")

    # social media
    tags = len(re.findall(r"(?<!\w)#\w+", raw)) + len(re.findall(r"(?<!\w)@\w+", raw))
    if tags:
        add("social", 2 + min(tags, 4) * 0.5, "etiket ve bahsetmeler")
    if len(EMOJI_RE.findall(raw)) >= 2:
        add("social", 1.5, "emoji")
    if "linkedin" in lower or re.search(r"peki siz|yorumlara|yorumlarda|sizce|takipte kal|paylaşır mısınız", lower):
        add("social", 2, "takipçiye seslenme")
    announce = len(re.findall(r"heyecan verici bir|gurur duyuyoruz|mutluluk duyuyoruz|bu yolculukta|duyurumuz var|buluşalım", lower))
    if announce:
        add("social", min(announce, 3) * 0.7, "gönderi kalıpları")
    if re.search(r"(?m)^\s*[\U0001F300-\U0001FAFF\U00002600-\U000027BF]", raw):
        add("social", 0.8, "satır başında emoji")

    ranked = sorted(score.items(), key=lambda kv: kv[1], reverse=True)
    (best, s1), (_, s2) = ranked[0], ranked[1]
    if s1 < 1.5:
        best, label = None, "Belirsiz"
        confidence = "düşük"
    else:
        label = GENRE_LABELS[best]
        confidence = "yüksek" if s1 >= 3 and s1 >= 2 * max(s2, 0.1) else "orta" if s1 - s2 >= 1.5 else "düşük"

    sector_scores = {name: sum(len(p.findall(lower)) for p in patterns) for name, patterns in SECTOR_PATTERNS.items()}
    sector, hits = max(sector_scores.items(), key=lambda kv: kv[1])
    if best in ("poetry", "literary"):
        sector = "edebiyat"
    elif hits < 2:
        sector = "genel"

    return {
        "genre": best,
        "label": label,
        "sector": sector,
        "confidence": confidence,
        "evidence": evidence[best][:3] if best else [],
        "scores": {k: round(v, 1) for k, v in ranked if v > 0},
    }


def profile_line(p):
    tail = f" [ipuçları: {', '.join(p['evidence'])}]" if p["evidence"] else ""
    return f"Metin tanımı (tahmin): {p['label']} · Alan: {p['sector']} · güven: {p['confidence']}{tail}"


# ---------------------------------------------------------------- evaluation

def alarms(m):
    """Returns (label, value text, status, note) rows. status: 'ok' | 'warn' | 'alarm' | 'info'.

    Labels and notes are Turkish because they are shown to the user as they are.
    """
    w = max(1, m["words"])
    pct = lambda x: f"%{round(x * 100)}"
    total = lambda d: sum(d.values())
    rows = []

    def add(label, value, status, note=""):
        rows.append((label, value, status, note))

    if m["sentences"] >= 3:
        cv = m["sentence_cv"]
        add("Cümle boyu çeşitliliği", f"{cv:.2f}".replace(".", ","),
            "alarm" if cv < 0.35 else "warn" if cv < 0.40 else "ok",
            "değişim katsayısı; 0,35 altı metronom, 0,40 ve üstü insan aralığı")
        add("Geniş zamanla biten", pct(m["aorist_share"]),
            "alarm" if m["aorist_share"] > 0.40 else "warn" if m["aorist_share"] > 0.30 else "ok",
            "§56: okura dönük metinde kof genel doğru; tanım, kural ve şartnamede doğal")
    add("\"olur\"", str(m["olur"]), "alarm" if m["olur"] >= 2 else "warn" if m["olur"] == 1 else "ok",
        "§56: \"ücretsiz olur\" yerine okuru özne yap, işin fiilini kullan")
    if m["sentences"] >= 6:
        add("Eş boy cümle dizisi", f"{m['equal_length_run']} cümle",
            "alarm" if m["equal_length_run"] >= 5 else "warn" if m["equal_length_run"] == 4 else "ok",
            "boyu birbirine ±3 kelime yakın, art arda orta-uzun cümle")
        add("Kısa cümle zinciri", f"{m['short_chain']} cümle",
            "alarm" if m["short_chain"] >= 4 else "warn" if m["short_chain"] == 3 else "ok",
            "5 kelime ve altı, art arda")
        add("En sık açılış", f"\"{m['top_opening']}\" {pct(m['top_opening_share'])}",
            "alarm" if m["top_opening_share"] > 0.25 and m["sentences"] >= 8 else "ok",
            "cümlelerin dörtte birinden fazlası aynı kelimeyle açılıyorsa")
        add("Bağlaçla açılan cümle", pct(m["connective_opening_share"]),
            "alarm" if m["connective_opening_share"] > 0.25 else "warn" if m["connective_opening_share"] > 0.15 else "ok",
            "Ayrıca / Öte yandan / Dolayısıyla ...")
        add("-maktadır ile biten", pct(m["maktadir_share"]),
            "alarm" if m["maktadir_share"] > 0.30 else "warn" if m["maktadir_share"] > 0.15 else "ok",
            "akademik ve resmî metinde yüksek olabilir")
        add("En sık cümle sonu", f"{m['rhyme']} {pct(m['rhyme_share'])}",
            "alarm" if m["rhyme_share"] > 0.45 else "warn" if m["rhyme_share"] > 0.30 else "ok",
            "aynı ekle biten cümlelerin payı (kafiye)")
        add("Zarf-fiil kuyruğu", pct(m["converb_tail_share"]),
            "alarm" if m["converb_tail_share"] > 0.15 else "ok",
            "cümlenin ikinci yarısında -arak/-erek")
    else:
        add("Ritim ölçümleri", f"{m['sentences']} cümle", "info", "6 cümleden kısa metinde ritim ölçülmez")

    add("Uzun tire", str(m["em_dash"]), "alarm" if m["em_dash"] else "ok",
        f"satır başı konuşma çizgisi hariç ({m['dialogue_lines']} konuşma satırı)")
    semicolon_limit = max(2, w // 300)
    add("Noktalı virgül", str(m["semicolons"]),
        "alarm" if m["semicolons"] > semicolon_limit + 1 else "warn" if m["semicolons"] > semicolon_limit else "ok",
        f"bu uzunlukta en fazla {semicolon_limit}")
    add("Etiketli iki nokta", str(m["labeled_colons"]),
        "alarm" if m["labeled_colons"] >= 2 else "warn" if m["labeled_colons"] == 1 else "ok",
        "\"Sorun şu:\", \"Cevap basit:\" türü anons")
    add("\"asıl\"", str(m["asil"]), "alarm" if m["asil"] > 3 else "warn" if m["asil"] >= 2 else "ok", "")
    degil_limit = max(3, round(w / 250))
    add("\"değil\"", f"{m['degil']} (sadece…değil: {m['not_only']})",
        "alarm" if m["degil"] > degil_limit or m["not_only"] >= 2 else "warn" if m["not_only"] == 1 else "ok",
        "karşıtlıkla parlatma iskeleti")
    add("Üçleme yoğunluğu", f"{m['triads']} ({str(m['triads_per_thousand']).replace('.', ',')}/1000 kelime)",
        "alarm" if m["triads_per_thousand"] > 4 and m["triads"] >= 3 else "warn" if m["triads_per_thousand"] > 3 and m["triads"] >= 2 else "ok",
        "\"X, Y ve Z\"")
    n = total(m["ai_words"])
    add("Yapay zeka kelimeleri", f"{n} ({', '.join(m['ai_words'])})" if n else "0",
        "alarm" if n * 100 / w > 1.5 else "warn" if n >= 2 else "ok", "")
    n = total(m["tech_buzzwords"])
    add("Teknoloji moda sözleri", f"{n} ({', '.join(m['tech_buzzwords'])})" if n else "0",
        "alarm" if n >= 3 else "warn" if n >= 1 else "ok", "dijital dönüşüm, uçtan uca ...")
    n = total(m["bureaucratic"])
    add("Bürokratik ekler", f"{n} ({', '.join(m['bureaucratic'])})" if n else "0",
        "alarm" if n * 100 / w > 1.5 else "warn" if n >= 3 else "ok", "")
    n = total(m["filler"])
    add("Dolgu kalıpları", f"{n} ({', '.join(m['filler'])})" if n else "0",
        "alarm" if n >= 2 else "warn" if n == 1 else "ok", "")
    n = total(m["chat_leftovers"])
    add("Sohbet artığı", f"{n} ({', '.join(m['chat_leftovers'])})" if n else "0",
        "alarm" if n else "ok", "tek başına kesin iz")
    n = total(m["mail_cliches"])
    add("Yazışma kalıpları", f"{n} ({', '.join(m['mail_cliches'])})" if n else "0",
        "alarm" if n >= 2 else "warn" if n == 1 else "ok", "İngilizce e-posta kalıplarının birebir çevirisi")
    add("Kendi sorup cevaplama", str(m["self_answer"]),
        "alarm" if m["self_answer"] >= 2 else "warn" if m["self_answer"] == 1 else "ok", "\"Peki neden? Çünkü...\"")
    n = total(m["office_jargon"])
    add("Plaza jargonu", f"{n} ({', '.join(m['office_jargon'])})" if n else "0",
        "info" if n else "ok", "kitleye göre karar ver, bkz. references/jargon.md")
    n = total(m["over_translations"])
    add("Aşırı terim çevirisi", f"{n} ({', '.join(m['over_translations'])})" if n else "0",
        "warn" if n else "ok", "geliştirici kitlesi bu karşılıkları kullanmıyor olabilir")
    add("Klişe giriş", ", ".join(m["cliche_opening"]) or "yok", "alarm" if m["cliche_opening"] else "ok", "ilk iki cümlede")
    add("Klişe kapanış", ", ".join(m["cliche_closing"]) or "yok", "alarm" if m["cliche_closing"] else "ok", "son paragrafta")
    add("Soruyla kapanış", "evet" if m["question_ending"] else "hayır", "warn" if m["question_ending"] else "ok",
        "tek başına sorun değil, alışkanlık olursa iz")
    if m["first_last_overlap"] is not None:
        add("İlk-son paragraf örtüşmesi", f"{m['first_last_overlap']:.2f}".replace(".", ","),
            "alarm" if m["first_last_overlap"] > 0.45 else "warn" if m["first_last_overlap"] > 0.30 else "ok",
            "kapanış girişi tekrar ediyor mu")
    if m["paragraph_cv"] is not None:
        add("Paragraf boyu çeşitliliği", f"{m['paragraph_cv']:.2f}".replace(".", ","),
            "warn" if m["paragraph_cv"] < 0.20 else "ok", "hepsi aynı yükseklikte mi")
    add("Kalın vurgu", str(m["bold"]), "alarm" if m["bold"] > max(3, w // 150) else "ok", "")
    add("Emoji", str(m["emoji"]), "warn" if m["emoji"] else "ok", "")
    add("Şapkalı harf", (f"{m['circumflexed']} (karışık: {', '.join(m['circumflex_mixed'])})"
                         if m["circumflex_mixed"] else str(m["circumflexed"])),
        "alarm" if m["circumflex_mixed"] else "warn" if m["circumflexed"] else "ok",
        "§32: şapka kullanma; yazarın örneği ya da resmî metin şapkalıysa ona uy")
    add("Başlıkta büyük bağlaç", ", ".join(m["heading_conjunctions"]) or "yok",
        "alarm" if m["heading_conjunctions"] else "ok", "ve, ile, de, mi başlıkta da küçük yazılır")
    at = m["atesman"]
    band = "çok kolay" if at >= 90 else "kolay" if at >= 70 else "orta" if at >= 50 else "zor" if at >= 30 else "çok zor"
    add("Okunabilirlik (Ateşman)", f"{str(at).replace('.', ',')} ({band})", "info",
        f"ort. cümle {str(m['mean_sentence']).replace('.', ',')} kelime, {str(m['syllables_per_word']).replace('.', ',')} hece/kelime")
    return rows


MARKS = {"ok": "✓", "warn": "~", "alarm": "!", "info": "·"}


def report(m, before=None, profile=None):
    lines = []
    lines.append("insanca · sayısal denetim")
    if profile:
        lines.append(profile_line(profile))
    if before:
        lines.append(f"Önce: {before['words']} kelime, {before['sentences']} cümle, {before['paragraphs']} paragraf")
        lines.append(f"Sonra: {m['words']} kelime, {m['sentences']} cümle, {m['paragraphs']} paragraf")
    else:
        lines.append(f"Metin: {m['words']} kelime, {m['sentences']} cümle, {m['paragraphs']} paragraf")
    lines.append("Eşikler alarm zilidir, hüküm vermez. ✓ temiz · ~ dikkat · ! alarm")
    lines.append("")
    new = alarms(m)
    old = {label: (value, status) for label, value, status, _ in alarms(before)} if before else {}
    width = max(len(label) for label, *_ in new) + 2
    for label, value, status, note in new:
        if before and label in old:
            old_value, old_status = old[label]
            line = f"{MARKS[status]} {label.ljust(width)}{MARKS[old_status]} {old_value}  →  {value}"
        else:
            line = f"{MARKS[status]} {label.ljust(width)}{value}"
        if note and status in ("warn", "alarm"):
            line += f"   [{note}]"
        lines.append(line)
    n_alarm = sum(1 for *_, s, _ in new if s == "alarm")
    n_warn = sum(1 for *_, s, _ in new if s == "warn")
    lines.append("")
    if before:
        old_alarm = sum(1 for *_, s, _ in alarms(before) if s == "alarm")
        lines.append(f"Alarm: {old_alarm} → {n_alarm} · Dikkat: {n_warn}")
    else:
        lines.append(f"Alarm: {n_alarm} · Dikkat: {n_warn}")
    return "\n".join(lines)


# ---------------------------------------------------------------- input, saved texts and the genre guide

SAVED_NAME_RE = re.compile(r"^[a-z0-9_-]{1,40}$")
GENRES_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "turler.md")
SECTORS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "alanlar.md")


def saved_dir():
    root = os.environ.get("INSANCA_ROOT") or os.path.join(tempfile.gettempdir(), "insanca")
    folder = os.path.join(root, "texts")
    os.makedirs(folder, exist_ok=True)
    return folder


def save_text(name, text):
    if not SAVED_NAME_RE.match(name):
        sys.exit(f"Geçersiz ad: {name!r}. Küçük harf, rakam, - ve _ kullan.")
    path = os.path.join(saved_dir(), name + ".txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def read(source):
    """Reads a text from standard input (-), a file, or a name saved earlier with --save."""
    if source == "-":
        return sys.stdin.read()
    # a short name without a dot or slash is a saved text first, a file in the current folder second
    if SAVED_NAME_RE.match(source) and os.path.exists(os.path.join(saved_dir(), source + ".txt")):
        with open(os.path.join(saved_dir(), source + ".txt"), encoding="utf-8") as f:
            return f.read()
    if os.path.exists(source):
        with open(source, encoding="utf-8") as f:
            return f.read()
    sys.exit(f"Metin bulunamadı: {source!r} ne bir dosya ne de --save ile saklanmış bir ad.")


def reference_section(path, label, exact=False):
    """The "## " section of a reference file whose title matches label, or None.
    Without exact, a title that starts with the label (or the other way round) also matches."""
    try:
        with open(path, encoding="utf-8") as f:
            guide = f.read()
    except OSError:
        return None
    sections = re.split(r"(?m)^## ", guide)
    wanted = tr_lower(label or "").strip()
    for sec in sections[1:]:
        title = tr_lower(sec.splitlines()[0].strip())
        if wanted and (title == wanted or not exact and (title.startswith(wanted) or wanted.startswith(title))):
            return "## " + sec.strip().rstrip("-").strip()
    return None


def genre_guide(label, exact=False):
    """The section of references/turler.md for this genre label, or None."""
    return reference_section(GENRES_FILE, label, exact)


def sector_guide(label, exact=False):
    """The section of references/alanlar.md for this sector, after the rules that hold in every sector."""
    section = reference_section(SECTORS_FILE, label, exact)
    if not section:
        return None
    common = reference_section(SECTORS_FILE, "Her alanda geçerli olanlar", exact=True)
    return f"{common}\n\n{section}" if common else section


def named_guide(label):
    """The guide for a genre or sector given by name: an exact title first, then a prefix."""
    return (genre_guide(label, exact=True) or sector_guide(label, exact=True)
            or genre_guide(label) or sector_guide(label))


def main(argv=None):
    ap = argparse.ArgumentParser(description="insanca · numeric audit for Turkish text")
    ap.add_argument("text", nargs="?", help="text file, - for standard input, or a name saved with --save")
    ap.add_argument("--before", help="earlier version to compare against (file or saved name)")
    ap.add_argument("--save", metavar="NAME", help="keep the text under this name for later commands")
    ap.add_argument("--json", action="store_true", help="JSON output")
    ap.add_argument("--profile", action="store_true", help="print only the genre and sector guess")
    ap.add_argument("--guide", nargs="?", const="", metavar="GENRE_OR_SECTOR",
                    help="print the writing guides for the guessed genre and sector, or the guide for the genre or sector given")
    args = ap.parse_args(argv)

    if args.text is None:
        if args.guide:
            print(named_guide(args.guide) or f"Bu tür ya da alan için rehber yok: {args.guide}")
            return
        ap.error("a text is required")
    text = read(args.text)
    if args.save:
        save_text(args.save, text)
    # the genre is guessed from the original: with --before that is the earlier version
    profile = guess_profile(read(args.before) if args.before else text)
    if args.profile:
        print(json.dumps(profile, ensure_ascii=False, indent=1) if args.json else profile_line(profile))
        return
    m = measure(text)
    b = measure(read(args.before)) if args.before else None
    if args.json:
        out = {"after" if b else "measurement": m}
        if b:
            out["before"] = b
        out["profile"] = profile
        out["alarms"] = [{"label": l, "value": v, "status": s} for l, v, s, _ in alarms(m)]
        print(json.dumps(out, ensure_ascii=False, indent=1))
    else:
        print(report(m, b, profile))
    if args.guide is not None:
        if args.guide:
            guides = [named_guide(args.guide)]
        else:
            guides = [genre_guide(profile["label"]), sector_guide(profile["sector"])]
        for guide in guides:
            if guide:
                print("\n" + guide)


if __name__ == "__main__":
    main()
