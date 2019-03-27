### The Tour
Sovellus on web-sivusto, josta muusikot näkevät keskitetysti kiertueen keikat ja keikkaan liittyviä tietoja. 

### Käyttäjät
Sovelluksella on kaksi käyttäjäryhmää, jotka vaativat kirjautumisen:
- Peruskäyttäjä ja Admin.

#### Peruskäyttäjä voi:
- Tarkastella keikkoja
- Lisätä vieraita keikan vieraslistaan

#### Admin voi:
- Lisätä, poistaa, muokata konsertteja ja niihin liittyviä yksityiskohtia.
- Listata käyttäjiä (saada mahdollisesti raportteja heistä: esim soitettujen keikkojen määrä tms statistiikkaa)
- Muokata käyttäjien oikeuksia

### Toiminnallisuus
- Kirjautuminen ja uloskirjautuminen: peruskäyttäjä tai admin.
- Kirjautumisessa on käytössä lomakkeen validointi. Esim: salasana ei saa olla tyhjä tai nimimerkin pitää olla vähintään 2 merkkiä pitkä. 
- Keikkojen listaus eri filtterein (myöhemmin): päivämäärän (ennen/jälkeen), nouseva tai laskeva järjestys pvm mukaan tai keikkojen listaus artistin perusteella. -> tietty keikka liittyy aina tiettyyn artistiin.
- Käyttäjien listaus, poistaminen, muokkaaminen (Admin)
- Admin voi myös poistaa muusikon yksittäiseltä keikalta ja lisätä tämän tilalleen esimerkiksi toisen soittajan.




[Linkki sovellukseen](https://tsoha-tour-demo.herokuapp.com)
### Testitunnukset: 
Username: hello
Password: world

### Dokumentaatio
- [Käyttäjätapauksia](https://github.com/jokineno/Tour/blob/master/documentation/kayttajatapaukset.md)
- [Tietokantakaavio](https://github.com/jokineno/Tour/blob/master/documentation/tietokantakaavio.png)
