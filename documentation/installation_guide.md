 # Asennus paikallisesti

Käyttäjän tulisi osata komentorivin perusteet, niin asennus onnistuu vaivatta. 

## Vaatimukset

Asenna etukäteen seuraavat palikat:

- python 3.6 tai 3.7
- pip ja virtuaaliympäristö vevn
- sqlite3


## Asennus

1. Kopioi eli kloonaa projekti paikalliselle koneellesi tekemällä komentorivillä seuraavasti: 
```
$ git clone git@github.com:jokineno/tour.git
```

Vaihtoehtoisesti projektin voi ladata purettavaksi .zip-tiedostona osoitteesta https://github.com/jokineno/Tour

2. Virtuaaliympäristön asennus ja aktivointi
```
$ python3 -m venv venv
$ source venv/bin/activate
```

3. Asenna riippuvuudet

```
$ pip install -r requirements.txt
```

4. Sovelluksen käynnistys
```
$ python3 run.py
```

_HUOM!_ sovelluksen käynnityessä ensimmäisen kerran ohjelmaan luodaan kaksi käyttäjää: ADMIN ja USER. 
- Kirjaudu tunnuksella admin ja salasanalla admin tai user ja user. 

5. Avaa selain osoitteessa http://localhost:5000/ tai sitä vastaavassa osoitteessa: http://127.0.0.1:5000/

6. Ohjelma on nyt käytettävissä paikallisesti. 


## Sovelluksen asentaminen Herokuun

+ riippuvuudet pitäisi olla ajan tasalla, sillä sovellus on kopio githubista. 

1. Asenna sovellus ensiksi paikallisesti yllä olevan ohjeen mukaan.

2. Asenna herokun tarjoamat komentorivityökalut


MacOS:
```
$ brew install heroku/brew/heroku
```

3. Kirjaudu Herokuun tunnuksillasi. Jos sinulla ei ole tunnuksia, niin luo ne ensiksi osoitteessa: http://heroku.com

```
$ heroku login
-> syötä tunnuksesi
```

4. Mene omalla koneellasi kansioon, jossa sovellus on ja luoda siitä "heroku-projekti"

```
$ cd ~/projekti
$ heroku create projekti
```

5. Lisää paikalliseen versionhallintaan tieto Herokusta ja lähetä projekti Herokuun

```
$ git remote add heroku
$ git add .
$ git commit -m "heroku setup"
$ git push heroku master
```

6. Projekti pyörii nyt Herokussa

7. Viritä seuraavaksi Herokun PostgreSQL tietokanta, jotta sovelluksen tieto tallentuu myös Herokussa
```
$ heroku config:set HEROKU=1
$ heroku addons:add heroku-postgresql:hobby-dev
```

8. Sovelluksella on nyt toimiva PostgreSQL -tietokanta Herokun palvelimella

Sovelluksen käynnistyessä luodaan admin -ja user -käyttäjät. Sovelluksessa voi rekisteröidä uuden käyttäjän, jonka rooliksi tulee user. Jos haluat kuitenkin luoda uuden admin käyttäjän, niin se tapahtuu komentorivillä seuraavanlaisesti. 

9. Uuden adminin luominen tuotantoympäristöön

Avaa komentorivi ja kirjoita: 

```
$ heroku pg:psql
projekti::DATABASE=> INSERT INTO account (name, username, password, role_id) VALUES ('Admin', 'admin', 'pass', 2);
```

role_id tulee olla 2, sillä se tarkoittaa pääkäyttäjää. role_id = 1 olisi tavallinen käyttäjä. 