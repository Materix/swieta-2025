# swieta-2025

Świąteczne losowanie prezentów w dwóch domach. Wyniki: `<dom>/<rok>/<uczestnik>.txt` (plik = kto daje, treść = komu).

- `zary/` — losują pojedyncze osoby; plik ma jedną linię (osoba).
- `beczarka/` — losują pary; linia 1 to obdarowywana para, linia 2 to dziecko
  (Rodzice nie losują dziecka, więc ich plik ma jedną linię).

Strona z wynikami (GitHub Pages):
- Żary: `https://materix.github.io/swieta-2025/?osoba=<Imię>`
- Bęczarka: `https://materix.github.io/swieta-2025/?dom=beczarka&osoba=<Para>` (np. `Ola-Michal`)

Domyślnie pokazuje bieżący rok; inny rok i dom wybierzesz z listy na stronie (albo `&rok=2025` w adresie).
Po kolejnym losowaniu dopisz nowy rok do `years` danego domu w `HOUSES` w `index.html`.

Losowanie Bęczarki: `python3 losuj_beczarka.py <rok>` — bez powtórki pary i dziecka z poprzedniego roku,
bez wzajemności (A→B wyklucza B→A).
