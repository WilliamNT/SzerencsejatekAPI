# OtoslottoAPI
Ez egy nyílt forráskódú API az ötöslottó [jelenlegi](https://bet.szerencsejatek.hu/jatekok/otoslotto) információinak lekéréshez.

### A kulisszák mögött
A script minden bejövő kérésnél lekéri és rendszerezi a nyilvánosan elérhető adatokat, majd vissza küldi azokat ```JSON``` formátumban.

### Használat & demó
- Demó: [kattints ide](https://lottery.skiby.net/api/v1/current)
- Endpointok:
  - A kéréseket a ```/api/v1/current/``` endpointra kell küldeni.
- A kéréseket ```GET``` kérésként küldd.
- Jelenleg az adatokat nem gyűjtji a rendszer sehova sem, szóval egy rate limit rendszert lehet bevezetek a jövőben.

A script beüzemeléséhez szükséged lesz a Python 3.8+ verziójára. Ssükséges csomagok: ```pip install -r requirements.txt```
