### Käyttöohje

#### Yleistä
> Ohjelman käynnistyessä ensimmäisen kerran, luodaan käyttäjät admin:admin ja user:user. Voit käyttää kumpaa tahansa sovelluksen testaukseen

### Rekisteröityminen

1. Käyttäjä painaa oikeasta yläkulmasta register ja täyttää kentät. 
2. Kaikki kentät ovat pakollisia. 
3. Validoinnin onnistuessa käyttäjä saa käyttäjäroolikseen __"USER"__. Hän ei voi itse sitä muuttaa, mutta admin voi antaa hänelle sovelluksen hallintaoikeudet. 
4. Jos käyttäjätunnus on jo olemassa tai käyttäjä ei käytä __A-Z__, __a-z__, __0-9__ merkkejä, niin hänen syötteensä hylätään ja hänen tulee yrittää rekisteröintiä uudestaan. 

### Kirjautuminen

1. Käyttäjä painaa __login__ ja täyttää __käyttäjätunnus__ -ja __salasanakentän__. 
2. Jos tunnukset vastaavat tietokannan tietoja, käyttäjä kirjautuu.
3. Sallitut merkit ovat myös kirjautumisessa __A-Z__, __a-z__, __0-9__. Jos kirjautumisessa käytetään muita merkkejä, niin käyttäjä saa virheviestin. 
4. Jos käyttäjän  syöttämiä tietoja ei löydy tietokannasta, käyttäjä saa viestin, että käyttäjää ei ole. 

### Uloskirjautuminen

1. Käyttäjä painaa __logout__ ja kirjautuu automaattisesti ulos. 

### Omien tietojen tarkastelu

1. Käyttäjä painaa oikeasta yläkulmasta __"profile"__, joka johtaa hänen profiilin tietoihin. 
2. Hän voi muokata nimeään ja käyttäjätunnustaan ja tallentaa tiedot __"save changes"__ -painikkeesta. 
3. Käyttäjä näkee lisäksi pienen tilaston hänen soittamistaan, tulevista ja peruttujen keikkojen määrästä. 


### Keikkojen tarkastelu

1. Käyttäjä painaa __"Your Gigs"__, jossa hän näkee käyttäjään liittyvät keikat. 
2. Hän voi painaa lisäksi __view__, josta hän pääsee tarkastelemaan yksittäisen keikan tietoja. 
3. Käyttäjä ei voi poistaa keikkoja vain admin voi poistaa keikkoja. Admin voi poistaa keikan __"delete"__ -painikkeesta. 
4. Delete -nappi ei luo "varmistus"-kenttää vaan poistaa keikan suoraan. Koen, että vahinkopainalluksen takia suurta määrää työtä ei tarvi tehdä uudelleen, joten tämä on vain käytön sujuvoittamiseksi. 
4. Jos ohjelmaa käyttää admin, niin hän näkee __"All Gigs"__ -painikkeesta kaikkien keikat. 
5. Keikkoja voi hakea kiertueittain __search__ -hakukentän avulla. 

### Keikan luonti

1. Vain admin voi luoda keikkoja. 
2. Admin painaa __"create a new gig"__ navigointipalkista, joka johdattaa hänet keikan luonti -lomakkeelle. 
3. Jos lomake validoidaan lähettäessä, uusi keikka luodaan. 
4. Ennen keikkaa on luotu kiertue, johon liitetty käyttäjiä. Keikkaa luotaessa valitaan kiertue. Keikka lisätään ainoastaan niille käyttäjille, jotka liittyvät valittuun kiertueeseen. 
5. Jos validointi ei onnistu, niin ohjelma palauttaa käyttäjlle __"fill this field"__ kyseisen kentän kohdalla. 


### Kiertueen luonti

1. Vain admin voi luoda kiertueen.
2. Kiertuessa luotaessa määritetään kiertueen nimi, aloitus -ja lopetuspäivä. Lisäksi merkitään käyttäjät, jotka liittyvät kiertueeseen. 


### Kiertueiden tarkastelu

1. User ja Admin voi tarkastella kiertueita.
2. User tai admin painaa __"Your Tours"__ tai __"All Tours"__ riippuen kumpi käyttäjärooli on käytössä. 
2. User näkee vain häneen liittyvät kiertueet ja admin näkee kaikki kiertueet. 
3. Kiertue-näkymässä näkee myös kuinka monta keikkaa niihin liittyy. 
4. Käyttäjä voi myös painaa __view__, josta hän pääsee näkemään kiertueen tietoja omassa näkymässä ja lisäksi siihen liittyvät keikat. 


### Kiertueiden poisto

1. Vain admin voi poistaa kiertueen. 
2. Admin on kiertueet -näkymässä ja painaa view. 
3. Seuraavaksi hän painaa delete tour and all gigs. 
4. Tämä johtaa varmistus näkymään (yes or no), jotta admin ei vahingossa poista runsaasti dataa. 
5. Kiertueen poistaminen aiheuttaa kiertueen sekä siihen liittyvien keikkojen häviämisen. 


### Ohjelman hallinta

1. Admin voi tarkastella käyttäjien ja kiertueiden sekä keikkojen tietoja. 
2. Admin painaa "administration", josta hän voi nähdä listattuna kaikki käyttäjät. Hän voi muuttaa heidän rooliaan __(change role)__ tai poistaa heidät järjestelmästä __(x)__. 
3. Admin näkee lisäksi kuinka monta keikkaa liittyy kuhunkin kiertueeseen ja käyttäjään. 



### Keikkojen muokkaus

1. Keikkojen muokkaus tapahtuu ainoastaan adminin toimesta. 
2. Hän on all gigs -näkymässä ja painaa halutun keikan kohdalta "edit", joka johtaa lomakkeelle, jossa tietoja voidaan muuttaa. 
3. Keikkoja pääsee myös muokkaamaan kiertue -näkymästä, josta voi valita kiertueeseen liittyvät keikan kohdalta __edit__ ja tehdä muutoksia lomakkeelle. 
3. __Save changes__ -nappulalla tiedot päivittyvät tietokantaan. 

