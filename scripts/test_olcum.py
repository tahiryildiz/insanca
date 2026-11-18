#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insanca · olcum.py test runner

Runs the open test set in tests/*.json, every example in references/ceviri-kaliplari.tsv, and, when present,
private cases kept OUTSIDE the repository (real client texts must never be published):

  ~/.claude/insanca-ozel/testler/*.json      (or the folder in INSANCA_OZEL_TESTLER)

Usage:
  python3 scripts/test_olcum.py          # all cases, exit code 1 on any failure
  python3 scripts/test_olcum.py -v       # also list passing cases

Case types (field "tur"):
  ek           metin, beklenen: "temiz" | "hata"
  genis_zaman  kelime, beklenen: true | false
  ceviri       metin, beklenen: "yakalanir" | "temiz" | "bilinen_kacak" (reported, not asserted)
  parca        metin, beklenen_cumle, beklenen_parca, beklenen_ceviri (optional)
  olgu         once, sonra, beklenen: "temiz"  or  beklenen_eklenen / beklenen_kaybolan: {etiket: [değerler]}

Uses only the Python 3 standard library.
"""

import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import olcum  # noqa: E402

ROOT = os.path.dirname(HERE)
PRIVATE = os.environ.get("INSANCA_OZEL_TESTLER") or os.path.join(os.path.expanduser("~"), ".claude", "insanca-ozel", "testler")


def check(case):
    """(passed: bool | None, detail: str). None means reported only."""
    t = case["tur"]
    if t == "ek":
        errors = olcum.suffix_errors(case["metin"])
        want_error = case["beklenen"] == "hata"
        return bool(errors) == want_error, "; ".join(errors) or "alarm yok"
    if t == "genis_zaman":
        got = olcum.is_aorist(case["kelime"])
        return got == case["beklenen"], f"is_aorist={got}"
    if t == "ceviri":
        hits = olcum.translation_hits(case["metin"])
        if case["beklenen"] == "bilinen_kacak":
            return None, "yakalandı (artık listede)" if hits else "kaçıyor (beklenen)"
        return bool(hits) == (case["beklenen"] == "yakalanir"), "; ".join(hits) or "yakalanmadı"
    if t == "parca":
        m = olcum.measure(case["metin"])
        ok = m["sentences"] == case["beklenen_cumle"] and m["fragments"] == case["beklenen_parca"]
        if "beklenen_ceviri" in case:
            ok = ok and bool(m["translation_hits"]) == case["beklenen_ceviri"]
        return ok, f"cümle={m['sentences']} parça={m['fragments']} çeviri={len(m['translation_hits'])}"
    if t == "olgu":
        lock = olcum.fact_lock(case["once"], case["sonra"])
        if case.get("beklenen") == "temiz":
            dirty = {k: v for k, v in lock.items() if v["eklenen"] or v["kaybolan"]}
            return not dirty, json.dumps(dirty, ensure_ascii=False) if dirty else "temiz"
        missing = []
        for kind, key in (("eklenen", "beklenen_eklenen"), ("kaybolan", "beklenen_kaybolan")):
            for label, values in case.get(key, {}).items():
                for v in values:
                    if v not in lock[label][kind]:
                        missing.append(f"{kind} {label}: {v}")
        return not missing, ("eksik: " + ", ".join(missing)) if missing else "beklenenlerin hepsi raporda"
    return False, f"bilinmeyen tür: {t}"


def tsv_cases():
    """Every example in the calque list must be caught by the list itself."""
    return [{"tur": "ceviri", "metin": ex, "beklenen": "yakalanir", "kaynak": f"ceviri-kaliplari.tsv · {label}"}
            for label, _, ex in olcum.load_translation_patterns() if ex]


def load(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data["vakalar"] if isinstance(data, dict) else data


def main():
    verbose = "-v" in sys.argv
    groups = [("açık", f, load(f)) for f in sorted(glob.glob(os.path.join(ROOT, "tests", "*.json")))]
    groups.append(("açık", "references/ceviri-kaliplari.tsv", tsv_cases()))
    private_files = sorted(glob.glob(os.path.join(PRIVATE, "*.json")))
    groups += [("özel", f, load(f)) for f in private_files]

    passed = failed = reported = 0
    for kind, source, cases in groups:
        for case in cases:
            ok, detail = check(case)
            label = case.get("metin") or case.get("kelime") or case.get("not") or case["tur"]
            label = label.replace("\n", " ")[:60]
            where = "özel" if kind == "özel" else os.path.basename(source)
            if ok is None:
                reported += 1
                if verbose:
                    print(f"  · [{where}] {case['tur']}: {label}  ({detail})")
            elif ok:
                passed += 1
                if verbose:
                    print(f"  ✓ [{where}] {case['tur']}: {label}")
            else:
                failed += 1
                print(f"  ✗ [{where}] {case['tur']}: {label}\n      {detail}")
    note = f" · özel vakalar: {len(private_files)} dosya" if private_files else " · özel vaka klasörü yok"
    print(f"\n{passed} geçti, {failed} kaldı, {reported} yalnız raporlandı{note}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
