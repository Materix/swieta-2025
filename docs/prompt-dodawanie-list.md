# Prompt: dodawanie listów do Aniołka

Wklej poniższy prompt do nowej sesji Claude Code w tym repozytorium, a pod nim treść listu (albo kilku).

```
Dodaj list(y) do Aniołka dla domu w Bęczarce na rok <ROK>.

Przeczytaj najpierw CLAUDE.md i docs/dodawanie-list.md.

Zasady:
- Dla każdego listu ustal obdarowywanego (identyfikator z tabeli w docs/dodawanie-list.md). Jeśli nie jest jasne, kto go napisał, zapytaj.
- Zapisz treść w beczarka/listy/<ROK>/<Identyfikator>.txt, tak jak ją przesłałem. Poprawiaj tylko technikę:
  podwójne spacje, końcowe spacje, spacja przed myślnikiem w punkcie. Nie zmieniaj stylu, nie skracaj, nie dopisuj tytułów.
- Punkty zostają jako wiersze zaczynające się od "- ". Linki jako [tekst](https://adres).
- Nie zmieniaj index.html, chyba że chodzi o nowy rok (years w HOUSES) albo o nowe słowa kluczowe naklejek (RULES).
- Sprawdź wynik: otwórz stronę wyników dla osoby, która losuje tego obdarowywanego (zob. beczarka/<ROK>/*.txt), kliknij prezent
  i obejrzyj kartę (Playwright z page.route, zob. CLAUDE.md). Zgłoś, jeśli tekst wygląda źle.
- Zrób commit i push na gałąź sesji. Merge do głównej tylko, gdy o to poproszę.
- Na końcu wypisz, czego nie zrobiłeś, oraz które listy (z 9) nadal brakują.

Treść listów:

<WKLEJ TUTAJ: "list od <Kto>" i pod spodem tekst>
```
