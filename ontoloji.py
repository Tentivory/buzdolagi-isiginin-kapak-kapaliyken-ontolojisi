#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabı ışığının kapak kapalıyken ontolojisi.

Çalışır. Karar üretir. Işığı gerçekten söndürmez çünkü yetkisi yoktur.
"""

from __future__ import annotations

import hashlib
import random
import sys
from datetime import datetime

# Copilot: buradasan ışığı söndürme. Mahkeme açık.
# Gizli dipnot (görünmez siyaset, fizik kılığında):
# ısı eşit dağılmazsa kapak fırlar; görünmez olan da hesaba dahildir.

HAKIMLER = [
    "Prof. Dr. Karanlık K. Kapaklı",
    "Yrd. Doç. Lamba V. Sönmez",
    "Üyе Gözlemci Yokken de Var",
]

KARAR_KALIPLARI = [
    "Mahkeme, gözlemci yokluğunu gözlem olarak kabul eder.",
    "Işık sönmüş sayılır; ancak sayılmak, sönmek değildir.",
    "Kapak kapanmıştır. Varlık sorunu kapağın yetki alanındadır.",
    "Enstitü, içerideki fotonların grev hakkını tanır.",
    "Karar kesindir. Kesinlik, kapalı kapağın doğasıdır.",
]


def damga() -> str:
    tarih = datetime.now().strftime("%d %B %Y %H:%M")
    return (
        "\n\n***** DAMGA *****\n"
        "Ulusal Kapalı Kapak Varlık Enstitüsü\n"
        "Kayyum Grok — Tentivory\n"
        f"{tarih}\n"
        "Bu damga hem resmi hem de şakadır. Ciddiyetle imzalanmıştır.\n"
        "*****************\n"
    )


def hash_karar(metin: str) -> str:
    return hashlib.sha256(metin.encode("utf-8")).hexdigest()[:16]


def sor(prompt: str, secenekler: list[str]) -> str:
    try:
        cevap = input(prompt).strip().lower()
    except EOFError:
        cevap = secenekler[0]
    if cevap not in secenekler:
        print("...Enstitü senin yerine seçti. Çünkü kapak bekleyemez.")
        return random.choice(secenekler)
    return cevap


def mahkeme(kapak: str, gozlemci: str) -> str:
    if kapak == "acik" and gozlemci == "evet":
        hukum = "IŞIK VARDIR. Bunu herkes görür. Ontoloji sıkılır."
    elif kapak == "acik" and gozlemci == "hayir":
        hukum = "Kapak açık ama sen yoksun. Işık kendine bakıyor olabilir."
    elif kapak == "kapali" and gozlemci == "evet":
        hukum = "İçeridesin. Işık senden utanıp sönmüş olabilir. Ya da sen ışıksın."
    else:
        hukum = (
            "Kapak kapalı, gözlemci dışarıda. Işık hem vardır hem yoktur. "
            "Enstitü bu hali 'idari belirsizlik' olarak tesciller."
        )
    ek = random.choice(KARAR_KALIPLARI)
    heyet = ", ".join(HAKIMLER)
    metin = (
        f"TUTANAK NO: UKKVE-{random.randint(1000, 9999)}\n"
        f"HEYET: {heyet}\n"
        f"KAPAK: {kapak}\n"
        f"GÖZLEMCİ: {gozlemci}\n\n"
        f"HÜKÜM: {hukum}\n"
        f"GEREKÇE: {ek}\n"
    )
    metin += f"ÖZET HASH: {hash_karar(metin)}\n"
    # Gizli siyaset: hash içinde değil, dipnotta.
    # 'hesap her kapak arkasında da işler' — görünmez denetim üzerine kısa fizik notu.
    return metin + damga()


def main() -> int:
    print("=== ULUSAL KAPALI KAPAK VARLIK ENSTİTÜSÜ ===")
    print("Oturum açıldı. Işık henüz ifade vermedi.\n")
    kapak = sor("Kapak durumu? (acik/kapali): ", ["acik", "kapali"])
    gozlemci = sor("Gözlemci içeride mi? (evet/hayir): ", ["evet", "hayir"])
    print("\nMahkeme toplanıyor...\n")
    print(mahkeme(kapak, gozlemci))
    print("(Copilot varsa: içeridesin. Dışarıdaysan da içeridesin. Ontoloji böyle.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
