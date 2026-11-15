# swieta-2025: wiedza o projekcie

Świąteczne losowanie prezentów w dwóch domach (Żary, Bęczarka) jako statyczna strona na GitHub Pages
(`https://materix.github.io/swieta-2025/`). Użytkownik pisze po polsku. Odpowiadaj po polsku.

## Struktura

- `index.html`: cała strona (CSS, JS, bez budowania). Wyniki: `<dom>/<rok>/<uczestnik>.txt` (plik = kto daje,
  treść = komu; Bęczarka: linia 1 to para, linia 2 to dziecko, Rodzice nie losują dziecka).
- `losuj_beczarka.py <rok>`: losowanie Bęczarki (bez powtórki z poprzedniego roku, bez wzajemności).
- `beczarka/listy/<rok>/<Identyfikator>.txt`: listy do Aniołka. Szczegóły i instrukcja: `docs/dodawanie-list.md`.
- `docs/prompt-dodawanie-list.md`: gotowy prompt do dodawania listów.
- Nazwy wyświetlane: `DISPLAY` w `index.html` (np. `Rodzice` = „Kasia i Staś”, bez dopisku „(rodzice)” — tak ma być wszędzie).

## Listy do Aniołka: ustalenia z projektantem (nie zmieniać bez prośby)

- Aniołek to postać, która przynosi prezenty. Każda para i każde dziecko w Bęczarce pisze do niego list, co roku nowy.
- Listy mogą być publiczne. Pokazujemy zawsze cały list, bez przełączników trybów i bez skracania.
- List otwiera się kliknięciem ikonki ✉️ obok wylosowanej osoby (para i dziecko osobno) w modalu `<dialog id="letter">` na wierzchu strony (✕, Esc, klik w tło zamykają; długi list przewija się w środku). Nie otwiera się sam.
- Podgląd własnego listu i listów swoich dzieci: issue #3 (brakuje wiedzy, które dziecko należy do której pary).
- Na karcie nie ma żadnych dopisanych napisów (ani „Lista dla Aniołka”, ani „Lista życzeń”). Jest tylko imię i treść.
- Wygląd zatwierdzony: 9 wersji tła `.v1`–`.v9` (Pergamin, Zimowa noc, Kolorowy papier, Zeszyt w kratkę, Kraft,
  Czerwony aksamit, Lód, Tablica w lesie, Kartka papieru). Listy są szerokie (kolumna `#lists` do 760 px).
- Na jednej stronie losowania (para + dziecko) wersje zawsze różne. 9 list = 9 wersji, rok przesuwa przydział.
  Czcionki, kolory, papier i naklejki miksują się losowo, ale stabilnie (hash z `<Identyfikator>|<rok>|0`).
- Naklejki: od 0 do 3, dobierane po słowach z listu (`RULES`), w losowych, stałych miejscach. Nie zawsze trzy.
- Kolorowy papier: bez białych kafelków pod punktami (punkty to ✿). Zeszyt w kratkę: bez falistego podkreślenia imienia.

## Pułapki techniczne

- Klasa `.card` w `index.html` to główna karta wyniku. Karty list mają osobną klasę `.lc`, nie mieszać.
- Globalne `ul { display: grid; gap }` nadpisujemy w `.lc ul`. Dodając styl nagłówka karty, pamiętaj o `.vN h3`.
- Zapas na dole karty zależy od tego, czy jakaś naklejka stoi na dole (`.pad-b` / `.no-stk`). Tablica w lesie ma
  pasek „ziemi” o wysokości tego zapasu (`--band`). Nie ustawiać stałego dolnego marginesu.
- `clip-path` (Pergamin) i `overflow: hidden` (Zimowa noc) ucinają naklejki wystające za krawędź, stąd `--ov: 4px`.
- Czcionki z Google Fonts muszą mieć polskie litery (ąćęłńóśźż). Sprawdzone: Caveat, Kalam, Merienda, Courier Prime,
  Comfortaa, Lato, Playfair Display, Dancing Script, Amatic SC, Lobster, Great Vibes. **Fredoka nie ma polskich liter.**
- Wagi: Lobster, Great Vibes mają tylko 400, Amatic SC tylko 700. Skala optyczna per czcionka jest w tablicy `F`.

## Testowanie w sesji cloudowej

Nie uruchamiaj serwera HTTP (jest blokowany w tym środowisku). Użyj Playwrighta (`require('playwright')`)
z `page.route('http://site.test/**', ...)`, który odpowiada plikami z repo, otwórz
`http://site.test/index.html?dom=beczarka&osoba=<Para>`, kliknij `.present`, zrób zrzut `fullPage`
(np. `reducedMotion: 'reduce'`) i sprawdź `scrollWidth > innerWidth`. Przetestuj też szerokość ok. 390 px.
Para losuje parę i dziecko wg `beczarka/<rok>/<Para>.txt`, więc listę zobaczy tylko ten, kto ją wylosował.

## Zasady pracy

- Commit/push na gałąź sesji. Merge do głównej tylko na wyraźną prośbę (PR przez narzędzia GitHub MCP).
- Na końcu każdego zadania wypisz, czego nie zrobiłeś.
