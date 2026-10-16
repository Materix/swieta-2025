#!/usr/bin/env python3
"""Losowanie dla domu Bęczarka.

Użycie: python3 losuj_beczarka.py <rok>   (np. 2026)

Wynik: beczarka/<rok>/<Para>.txt — linia 1: para, którą obdarowuje; linia 2: dziecko.
Reguły:
  * para nie losuje samej siebie,
  * para nie losuje tej samej pary co rok wcześniej,
  * brak wzajemności (jeśli A daje B, to B nie daje A),
  * każda para poza Rodzicami losuje jedno dziecko, inne niż rok wcześniej.
"""
import itertools
import secrets
import sys
from pathlib import Path

PAIRS = ["Agula-Bartula", "Ola-Michal", "Kasia-Pawel", "Julianka-Piotrek", "Rodzice"]
NO_CHILD = {"Rodzice"}
CHILDREN = ["Jozek", "Wandzia", "Ritka", "Wojtek"]
ROOT = Path(__file__).parent / "beczarka"


def read_year(year):
    result = {}
    for pair in PAIRS:
        path = ROOT / str(year) / f"{pair}.txt"
        if path.exists():
            lines = path.read_text(encoding="utf-8").split()
            result[pair] = (lines[0], lines[1] if len(lines) > 1 else None)
    return result


def main():
    year = int(sys.argv[1])
    out = ROOT / str(year)
    if out.exists():
        sys.exit(f"{out} już istnieje — nie nadpisuję.")
    prev = read_year(year - 1)

    pair_options = [
        dict(zip(PAIRS, perm))
        for perm in itertools.permutations(PAIRS)
        if all(
            giver != taker
            and prev.get(giver, (None,))[0] != taker
            and dict(zip(PAIRS, perm))[taker] != giver
            for giver, taker in zip(PAIRS, perm)
        )
    ]
    givers = [p for p in PAIRS if p not in NO_CHILD]
    child_options = [
        dict(zip(givers, perm))
        for perm in itertools.permutations(CHILDREN)
        if all(prev.get(g, (None, None))[1] != c for g, c in zip(givers, perm))
    ]
    if not pair_options or not child_options:
        sys.exit("Brak przydziału spełniającego reguły.")

    pairs = secrets.choice(pair_options)
    children = secrets.choice(child_options)
    out.mkdir(parents=True)
    for pair in PAIRS:
        lines = [pairs[pair]] + ([children[pair]] if pair in children else [])
        (out / f"{pair}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Zapisano {out} ({len(pair_options)} możliwych układów par, "
          f"{len(child_options)} układów dzieci).")


if __name__ == "__main__":
    main()
