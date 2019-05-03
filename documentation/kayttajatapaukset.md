
### Käyttötapauksia

1. Muusikko on lähdössä keikalle. Edellisenä iltana hän avaa sovelluksen ja katsoo keikkapäivän aikataulut ja speksit: mistä on lähtö, kuinka kauan matka kestää, monelta on load-in, soundcheck, showtime sekä miten ruokailu on järjestetty. (osittain toteutettu, lisätietolaatikko pitänee lisätä)
2. Muusikko katsoo alkuvuodesta, että millainen kiertue on tulossa. Hän avaa pääsivun ja tarkastelee keikkoja sieltä. Hän voi myös valita vain tietyn artistin keikat, jos hän soittaa useammassa bändissä (filteröinti toimii, paikan tai kiertueen nimen mukaan). 
3. Admin voi poistaa vääriä keikkoja ja tulevaisuudessa myös muokata keikan tietoja - esimerkiksi vaihtunutta showtimea (toimii). 
4. Uusi kiertue on alkamassa ja kaikki crewin ja bändin jäsenet haluaisivat keikkojen tarkat tiedot etukäteen. Admin voi lisätä kiertueen tiedot ja liittää soittajat kiertueeseen, jonka jälkeen he pystyvät tarkastelemaan koko kiertuetta keskitetysti (soittajat - kiertue on monesta moneen -suhde).
5. Uusi käyttäjä haluaa luoda tunnukset. Hän painaa 'rekisteröidy' ja syöttää tunnukset. Lomakkeen kentät on validoitu. Rekisteröitymisen onnistuttua käyttäjälle luodaan automaattisesti "muut -kiertue". 


### Rekisteröityminen

1. Käyttäjä painaa oikeasta yläkulmasta register ja täyttää kentät. 
2. Kaikki kentät ovat pakollisia. 
3. Validoinnin onnistuessa käyttäjä saa käyttäjäroolikseen "USER". Hän ei voi itse sitä muuttaa, mutta admin voi antaa hänelle sovelluksen hallintaoikeudet. 
4. Jos käyttäjätunnus on jo olemassa tai käyttäjä ei käytä a-z, 0-9 merkkejä, niin hänen syötteensä hylätään ja hänen tulee yrittää rekisteröintiä uudestaan. 

### Kirjautuminen

1. Käyttäjä painaa login ja täyttää käyttäjätunnus ja salasanakentän. 
2. Jos tunnukset vastaavat tietokannan tietoja, käyttäjä kirjautuu. 

### Uloskirjautuminen

1. Käyttäjä painaa logout ja kirjautuu automaattisesti ulos. 

### Omien tietojen tarkastelu

1. Käyttäjä painaa oikeasta yläkulmasta "profile", joka johtaa hänen profiilin tietoihin. 
2. Hän voi muokata nimeään ja käyttäjätunnustaan ja tallentaa tiedot. 
3. Käyttäjä näkeel lisäksi pienen tilaston hänen soittamistaan, tulevista ja peruttujen keikkojen määrästä. 

### Keikkojen tarkastelu

1. Käyttäjä painaa "Your Gigs", jossa hän näkee häneen liittyvät keikat. 
2. Hän voi painaa lisäksi view, josta hän pääsee tarkastelemaan yksittäisen keikan tietoja. 
3. Käyttäjä ei voi poistaa keikkoja vain admin voi poistaa keikkoja. Admin voi poistaa keikan "delete" -painikkeesta. 
4. Delete -nappi ei luo "varmistus"-kenttää vaan poistaa keikan suoraan. Koen, että vahinkopainalluksen takia suurta määrää työtä ei tarvi tehdä uudelleen, joten tämä on vain käytön sujuvoittamiseksi. 
4. Jos ohjelmaa käyttää admin, niin hän näkee "ALL gigs" -painikkeesta kaikkien keikat. 

### Keikan luonti

1. Vain admin voi luoda keikkoja. 
2. Admin painaa "create a new gig" navigointipalkista, joka johdattaa hänet keikan luonti -lomakkeelle. 
3. Jos lomake validoidaan lähettäessä, uusi keikka luodaan. 
4. Ennen keikkaa on luotu kiertue, johon liitetty käyttäjiä. Keikkaa luotaessa valitaan kiertue. Keikka lisätään ainoastaan niille käyttäjille, jotka liittyvät valittuun kiertueeseen. 
5. Jos validointi ei onnistu, niin ohjelma palauttaa käyttäjlle "fill this field" kyseisen kentän kohdalla. 


### Kiertueen luonti

1. Vain admin voi luoda kiertueen.
2. Kiertuessa luotaessa määritetään kiertueen nimi, aloitus -ja lopetuspäivä. Lisäksi merkitään käyttäjät, jotka liittyvät kiertueeseen. 


### Kiertueiden tarkastelu

1. User ja Admin voi tarkastella kiertueita.
2. USer näkee vain häneen liittyvät kiertueet ja admin näkee kaikki kiertueet. 
3. Kiertuista näkee myös kuinka monta keikkaa niihin liittyy. 


### Kiertueiden poisto

1. Vain admin voi poistaa kiertueen. 
2. Admin on kirtueet -näkymässä ja painaa view. 
3. Seuraavaksi hän painaa delete tour and all gigs. 
4. Tämä johtaa varmistus näkymään (yes or no), jotta admin ei vahingossa poista runsaasti dataa. 
5. Kiertueen poistaminen aiheuttaa kiertueen sekä siihen liittyvien keikkojen häviämisen. 


### Ohjelman hallinta

1. Admin voi tarkastella käyttäjien ja kiertueiden sekä keikkojen tietoja. 
2. Admin painaa "administration", josta hän voi nähdä listattuna kaikki käyttäjät. Hän voi muuttaa heidän rooliaan (change role) tai poistaa heidät järjestelmästä (x). 
3. Admin näkee lisäksi kuinka monta keikkaa liittyy kuhunkin kiertueeseen ja käyttäjään. 



### Kiertueiden ja keikkojen muokkaus

1. Kiertueiden ja keikkojen muokkaus tapahtuu ainoastaan adminin toimesta. 
2. Hän on joko all gigs tai all tours -näkymässä ja painaa halutun kiertueen/keikan kohdalta "edit", joka johtaa lomakkeelle, jossa tietoja voidaan muuttaa. 
3. Save changes -nappulalla tiedot päivittyvät tietokantaan. 