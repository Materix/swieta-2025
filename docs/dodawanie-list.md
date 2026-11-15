# Dodawanie list do Aniołka (Bęczarka)

Lista to list napisany do Aniołka przez parę albo dziecko (np. „Ola i Michał”, „Wojtek”). Po otwarciu prezentu strona
pokazuje listy **wylosowanej pary** i **wylosowanego dziecka**. Listy są co roku nowe i wyświetlane w całości.

## Gdzie leżą pliki

`beczarka/listy/<rok>/<Identyfikator>.txt`, np. `beczarka/listy/2026/Ola-Michal.txt`.

| Identyfikator       | Wyświetlana nazwa      | Rodzaj  |
|---------------------|------------------------|---------|
| `Agula-Bartula`     | Agula i Bartula        | para    |
| `Ola-Michal`        | Ola i Michał           | para    |
| `Kasia-Pawel`       | Kasia i Paweł          | para    |
| `Julianka-Piotrek`  | Julianka i Piotrek     | para    |
| `Rodzice`           | Kasia i Staś           | para    |
| `Jozek`             | Józek                  | dziecko |
| `Wandzia`           | Wandzia                | dziecko |
| `Ritka`             | Ritka                  | dziecko |
| `Wojtek`            | Wojtek                 | dziecko |

Nazwy wyświetlane są w `DISPLAY` w `index.html`. Katalog `beczarka/<rok>/` to wyniki losowania, a nie listy
(nie mieszać: tam plik `Ola-Michal.txt` mówi, kogo Ola i Michał losują).

## Format pliku

Zwykły tekst UTF-8, emoji dozwolone.

- Wiersze zaczynające się od `- ` to punkty (strona rysuje je jako ozdobne punkty, bez myślnika).
- Pozostałe wiersze to akapity. Pusty wiersz rozdziela akapity, a zwykłe złamanie wiersza zostaje złamaniem.
- Link: `[tekst](https://adres)` albo sam adres `https://...`.
- Nie dodawać własnych tytułów ani dopisków (np. „Lista życzeń”). Strona sama pokazuje tylko imię nad listem.
- Treść wklejamy tak, jak ją przysłano. Dozwolone drobne poprawki techniczne: usunięcie podwójnych spacji,
  końcowych spacji i spacji przed myślnikiem w punkcie. Nie poprawiamy stylu, literówek ani nie skracamy.

## Jak dodać kolejny list

1. Zapisz tekst w `beczarka/listy/<rok>/<Identyfikator>.txt` (zob. tabela).
2. Nic nie trzeba zmieniać w `index.html`: strona sama szuka pliku po otwarciu prezentu.
3. Sprawdź lokalnie (patrz niżej), commit, push, merge do głównej gałęzi. GitHub Pages odświeża się po merge.

Brak pliku nie jest błędem: strona po prostu nie pokaże tej listy.

## Nowy rok

1. Wylosuj: `python3 losuj_beczarka.py <rok>` i dopisz rok do `years` dla `beczarka` (i `zary`) w `HOUSES` w `index.html`.
2. Listy do `beczarka/listy/<rok>/`. Stare listy poprzednich lat zostają (są widoczne po wyborze roku na stronie).

## Jak strona wybiera wygląd (żeby nic nie zmieniać ręcznie)

- 9 wersji tła `.v1`–`.v9` w `index.html`: Pergamin, Zimowa noc, Kolorowy papier, Zeszyt w kratkę, Kraft,
  Czerwony aksamit, Lód, Tablica w lesie, Kartka papieru.
- Przydział: 5 par + 4 dzieci = 9 list = 9 wersji. W jednym roku każda lista ma inną wersję, więc na jednej
  stronie (para + dziecko) nigdy się nie powtarzają. Rok przesuwa przydział (`styleOf`).
- Miksowanie: czcionka tekstu, czcionka nagłówka, kolor akcentu i (dla Kartki papieru) papier i wzór są
  losowane z puli, ale stabilnie dla danej osoby i roku (hash z `<Identyfikator>|<rok>|0`).
- Naklejki: 0–3, dobierane po słowach w liście (`RULES` w `index.html`), każda w losowym, ale stałym miejscu.
  Jeśli nic nie pasuje, naklejek nie ma. Gdy pasuje więcej niż 3, wybieramy 3 losowo (stabilnie).
  Żeby dodać nowe słowo kluczowe → emoji, dopisz wpis do `RULES`.

## Sprawdzanie lokalnie

Uruchom lokalny serwer w katalogu repo (`python3 -m http.server`) i otwórz
`http://localhost:8000/?dom=beczarka&osoba=<Para>`, kliknij prezent. Para losuje parę i dziecko wg
`beczarka/<rok>/<Para>.txt`, więc listę zobaczy tylko ten, kto ją wylosował.

W cloudowej sesji Claude Code nie uruchamiamy serwera. Wystarczy Playwright z `page.route()`, który podaje pliki repo pod
udawanym adresem (zob. `CLAUDE.md`).

## Linki do stron wyników

Podstawa: `https://materix.github.io/swieta-2025/`

- Żary: `?dom=zary&osoba=Agnieszka`, `Gabrysia`, `Krzysztof`, `Michal`, `Ola`
- Bęczarka: `?dom=beczarka&osoba=Agula-Bartula`, `Ola-Michal`, `Kasia-Pawel`, `Julianka-Piotrek`, `Rodzice`
