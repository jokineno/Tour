
### Käyttötapauksia
1. Muusikko on lähdössä keikalle. Edellisenä iltana hän avaa sovelluksen ja katsoo keikkapäivän aikataulut ja speksit: mistä on lähtö, kuinka kauan matka kestää, monelta on load-in, soundcheck, showtime sekä miten ruokailu on järjestetty. 
2. Muusikko katsoo alkuvuodesta, että millainen kiertue on tulossa. Hän avaa pääsivun ja tarkastelee keikkoja sieltä. Hän voi myös valita vain tietyn artistin keikat, jos hän soittaa useammassa bändissä. 
3. Admin voi poistaa vääriä keikkoja ja tulevaisuudessa myös muokata keikan tietoja - esimerkiksi vaihtunutta showtimea. 
4. Uusi kiertue on alkamassa ja kaikki crewin ja bändin jäsenet haluaisivat keikkojen tarkat tiedot etukäteen. Admin voi lisätä kiertueen tiedot ja liittää soittajat kiertueeseen, jonka jälkeen he pystyvät tarkastelemaan koko kiertuetta keskitetysti.


### Käyttäjät
Sovelluksella on kaksi käyttäjäryhmää, jotka vaativat kirjautumisen:
- Peruskäyttäjä ja Admin.

#### Peruskäyttäjä voi:
- Tarkastella keikkoja
- Muuttaa omia tietojaan, mutta ei käyttäjäroolia

#### Admin voi:
- Lisätä, poistaa, muokata konsertteja ja niihin liittyviä yksityiskohtia.
- Listata käyttäjiä (saada mahdollisesti raportteja heistä: esim soitettujen keikkojen määrä tms statistiikkaa)
- Muokata käyttäjien oikeuksia
- Nähdä kaikki käyttäjät

### Toiminnallisuus
- Kirjautuminen ja uloskirjautuminen: peruskäyttäjä tai admin.
- Kirjautumisessa on käytössä lomakkeen validointi. Esim: salasana ei saa olla tyhjä tai nimimerkin pitää olla vähintään 2 merkkiä pitkä. 
- Keikkojen listaus eri filtterein (myöhemmin): päivämäärän (ennen/jälkeen), nouseva tai laskeva järjestys pvm mukaan tai keikkojen listaus artistin perusteella. -> tietty keikka liittyy aina tiettyyn artistiin.
- Käyttäjien listaus, poistaminen, muokkaaminen (Admin)
- Admin voi myös poistaa muusikon yksittäiseltä keikalta ja lisätä tämän tilalleen esimerkiksi toisen soittajan.

