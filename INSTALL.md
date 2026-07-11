# Kurulum Rehberi

İnsanca'nın çalışan tek dosyası `SKILL.md`; düz Markdown olduğu için dosya okuyabilen her yapay zeka aracında kullanılabilir. Aşağıda araç araç kurulum var. Ortak ilk adım çoğunda aynı: Repoyu bir yere klonla.

## Claude Code

Skill dizinine klonlaman yeterli, `/insanca` komutu kendiliğinden gelir:

```bash
git clone https://github.com/tahiryildiz/insanca.git ~/.claude/skills/insanca
```

Eklenti olarak kurmak istersen:

```
/plugin marketplace add tahiryildiz/insanca
/plugin install insanca@insanca
```

Skills CLI kullananlar için: `npx skills add tahiryildiz/insanca` (desteklenen tüm araçlara birden kurmak için `--agent '*'`).

## OpenAI Codex CLI

Codex, `~/.codex/prompts/` altındaki Markdown dosyalarını slash komutuna çevirir. İki adım:

```bash
git clone https://github.com/tahiryildiz/insanca.git ~/.codex/insanca
cp ~/.codex/insanca/adapters/codex/insanca.md ~/.codex/prompts/insanca.md
```

Kullanım: Codex içinde `/prompts:insanca` yazıp metni ekle. Adaptör dosyası Codex'e önce `~/.codex/insanca/SKILL.md` talimatını okutur, sonra metni döngüden geçirtir.

## Gemini CLI

Gemini CLI, `~/.gemini/commands/` altındaki TOML dosyalarını özel komut yapar:

```bash
git clone https://github.com/tahiryildiz/insanca.git ~/.gemini/insanca
mkdir -p ~/.gemini/commands
cp ~/.gemini/insanca/adapters/gemini/insanca.toml ~/.gemini/commands/insanca.toml
```

Kullanım: `/insanca [metin]`. Proje bazlı istersen aynı TOML'u `<proje>/.gemini/commands/` altına koy.

## Cursor

Repoyu projenin içine klonla, kural dosyasını Cursor'ın kural dizinine kopyala:

```bash
git clone https://github.com/tahiryildiz/insanca.git insanca
mkdir -p .cursor/rules
cp insanca/adapters/cursor/insanca.mdc .cursor/rules/insanca.mdc
```

Kural, açıklama tetiklemeli çalışır: Sohbette "şu metni doğallaştır" dediğinde Cursor kuralı devreye sokar, kural da `insanca/SKILL.md` dosyasını okutur.

## OpenCode ve AGENTS.md destekleyen diğer araçlar

AGENTS.md standardını destekleyen her araçta (OpenCode, Jules, Amp vb.) en garantili yol:

1. Repoyu bir yere klonla (ör. `~/.agents/insanca`).
2. `adapters/agents-md-snippet.md` içindeki bölümü, aracın global veya projenin `AGENTS.md` dosyasına yapıştır; `<KLON-YOLU>`nu klonladığın yolla değiştir.

OpenCode kullanıcıları skills CLI ile de kurabilir: `npx skills add tahiryildiz/insanca --agent opencode`.

## Başka herhangi bir araç veya sohbet arayüzü

Aracın dosya okuma yeteneği yoksa bile çözüm basit: `SKILL.md` içeriğini sistem talimatı ya da ilk mesaj olarak yapıştır, ardından "şu metni doğallaştır" de. ChatGPT/Claude/Gemini web arayüzlerinde özel talimat (custom instructions / Gem / Project) alanına da aynı içerik konabilir; dosya büyük geliyorsa yalnızca kalıp bölümlerini alıp `references/deyimler.md`yi ayrıca eklemek de çalışır.

## Kurulumu doğrulama

Hangi araçta olursa olsun şu mini testi yap: "Şu cümleyi doğallaştır: Günümüzde yapay zeka, hayatımızın her alanında kritik bir rol oynamaktadır." Doğru kurulmuşsa araç, klişe girizgahı ve önem şişirmesini teşhis edip somut bir cümle önermeli; cümleyi övüp geçiyorsa talimat dosyası okunmamış demektir.
