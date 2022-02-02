# SzerencsejatekAPI
Ez egy nyílt forráskódú API a [szerencsejatek.hu](https://www.szerencsejatek.hu/) jelenjegi játék információinak lekéréshez.

### A kulisszák mögött
A script minden bejövő kérésnél lekéri és rendszerezi a nyilvánosan elérhető adatokat, majd vissza küldi azokat ```JSON``` formátumban.

### Használat & demó
- Demó: [kattints ide](https://lottery.skiby.net/api/v1/current/otoslotto/)
- Endpointok:
  - A kéréseket a ```/api/v1/current/``` + ```lottoneve``` endpointra kell küldeni, ahol ```lottoneve``` lehet ```luxor```, ```joker```, ```otoslotto```, ```hatoslotto```, ```eurojackpot``` vagy ```skandinavlotto```.
- A kéréseket ```GET``` kérésként küldd.
- Jelenleg az adatokat nem gyűjtji a rendszer sehova sem, szóval egy rate limit rendszert lehet bevezetek a jövőben.
- A ```logoImage``` kulcs értéke nem frissül automatikusan, ezért az Angular természete miatt ez az érték elavult lesz a jövőben.

A script beüzemeléséhez szükséged lesz a Python 3.8+ verziójára. Ssükséges csomagok: ```pip install -r requirements.txt```
