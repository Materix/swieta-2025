# swieta-2025

Świąteczne losowanie prezentów w dwóch domach. Wyniki: `<dom>/<rok>/<uczestnik>.txt` (plik = kto daje, treść = komu).

- `zary/` — losują pojedyncze osoby; plik ma jedną linię (osoba).
- `beczarka/` — losują pary; linia 1 to obdarowywana para, linia 2 to dziecko
  (Rodzice nie losują dziecka, więc ich plik ma jedną linię).

Strona z wynikami (GitHub Pages):
- Żary: `https://materix.github.io/swieta-2025/?dom=zary&osoba=<Imię>`
- Bęczarka: `https://materix.github.io/swieta-2025/?dom=beczarka&osoba=<Para>` (np. `Ola-Michal`)

Dom wynika z linku (`dom=`) i jest wyróżniony na stronie — nie da się go zmienić na stronie; link bez `dom=` otwiera Żary.
Domyślnie pokazuje bieżący rok; inny rok wybierzesz z listy na stronie (albo `&rok=2025` w adresie).
Po kolejnym losowaniu dopisz nowy rok do `years` danego domu w `HOUSES` w `index.html`.

Losowanie Bęczarki: `python3 losuj_beczarka.py <rok>` — bez powtórki pary i dziecka z poprzedniego roku,
bez wzajemności (A→B wyklucza B→A).

Po kliknięciu prezent się otwiera (animacja). Strona zapamiętuje w przeglądarce (`localStorage`), że dana osoba
w danym domu i roku już otworzyła prezent — przy kolejnym wejściu wynik pokazuje się od razu, bez animacji.

Listy do Aniołka (tylko Bęczarka): `beczarka/listy/<rok>/<Obdarowywany>.txt` — jeden plik na parę lub dziecko
(`Ola-Michal`, `Rodzice`, `Wojtek`, `Jozek`, …), co roku nowe. Treść pisana zwykłym tekstem, emoji dozwolone:
wiersze zaczynające się od `- ` to punkty, reszta to akapity (pusty wiersz rozdziela akapity), link: `[tekst](https://adres)`
albo sam adres. Po otwarciu prezentu strona pokazuje cały list wylosowanej pary i dziecka (jeśli plik istnieje)
w jednej z 9 wersji tła; lista pary i dziecka mają zawsze różne wersje, a czcionka, kolory i naklejki (0–3, dobrane
ze słów w liście) są losowane stabilnie dla danej osoby i roku. Wygląd: style `.v1`–`.v9` w `index.html`.
Czcionki ładują się z Google Fonts.
