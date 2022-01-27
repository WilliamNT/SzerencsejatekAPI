# OtoslottoAPI
Ez egy nyílt forráskódú API az ötöslottó legutóbbi illetve [mindenkori sorsolásainak](https://bet.szerencsejatek.hu/cmsfiles/otos.html) lekéréséhez.

### A kulisszák mögött
A script minden bejövő kérésnél lekéri és rendszerezi a nyilvánosan elérhető HTML táblázatot, amit fentebb linkeltem.

### Használat & demó
- Demó: *hamarosan*
- Endpointok:
  - A kéréseket a ```/api/v1/results``` endpointra kell küldeni. Itt kettő paramétert kell meghatároznunk:
    - ```type```: A type (típus) lehetséges értékei a ```latest``` vagy ```all``` lehet (```latest``` a legelső, ```all``` az összes sor a táblázatból)
    - ```format```: A format (formátum) lehetséges értékei a ```json``` vagy ```html``` lehet. Ez a paraméter opcionális, és az alapértelmezett értéke a ```json```.
- A kéréseket ```GET``` kérésként küldd.
- Jelenleg az adatokat nem gyűjtji a rendszer sehova sem, szóval egy rate limit rendszert érdemes lehet bevezetni.

A script beüzemeléséhez szükséged lesz a Python 3.8+ verziójára. Ssükséges csomagok: ```pip install -r requirements.txt```
