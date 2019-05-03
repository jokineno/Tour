![Tietokantakaavio](https://github.com/jokineno/Tour/blob/master/documentation/tietokantakaavio.png)

#### account eli käyttäjätili
attribuutti | kuvaus | merkitys | esimerkki
--- | --- | --- | ---
id | Käyttäjän tunnus, kokonaisluku, joka muodostuu itsestään, kun käyttäjä luodaan | pääavain| 1
date_created | DATETIME, aika, jolloin käyttäjä on luotu | ei merkittävä | 2000-01-01 12:00:00.00000
date_modified | DATETIME, aika, jolloin käyttäjän tietoja on muokattu | ei merkittävä | 2000-01-01 12:00:00.00000
name | käyttäjän nimi, merkkijono, joka validointien takia rajoittuu 2-20 merkkiin. | ei merkittävä | helloworld
username | Käyttäjätunnus. Tietokantaan mahtuu 144 merkin mittainen merkkijono, mutta validointien takia tunnuksen pituus on 2-20 merkkiä. Sallitut merkit ovat a-z, A-Z, 0-9. | ei merkittävä, mutta ei jää myöskään tyhjäksi validoinnin takia | testuser1
password | Validoinnit rajoittavat merkkijonon 2-20 merkkiin. Sallitut merkit ovat a-z, A-Z, 0-9. Salasana tallennetaan PasswordFieldinä eli salattuina merkkeinä.  | Keskeinen attribuutti kirjautumista varten | sala3ana
role_id | Kokonaisluku, joka kuvaa käyttäjän roolia. | merkittävä käytön kannalta, vieras avain | 1 tai 2


#### tours_users eli kiertueiden ja käyttäjien liitostaulu

attribuutti | kuvaus | merkitys | esimerkki
--- | --- | --- | ---
account_id | Kokonaisluku, joka kuvaa tiettyä käyttäjää. Muodostuu, kun kiertueeseen liitetään käyttäjä | pakollinen, vieras avain| 1
tour_id | Kokonaisluku, joka kuvaa kiertuetta. Muodostuu, kun kiertue uodaan | pakollinen, vieras avain | 1




#### tour eli kiertue
attribuutti | kuvaus | merkitys | esimerkki
--- | --- | --- | ---
id | Kiertueen tunnus, kokonaisluku, joka muodostuu itsestään, kun kiertue luodaan | pääavain| 1
name | Kiertueen nimi. Merkkijono, joka luodaan kiertuessa luodessa adminin toimesta. Ei jää validointien takia tyhjäksi | Ei ohjelman kannalta merkittävä, mutta helpottaa käyttämistä| testikiertue
start_date | Date - kiertueen aloituspäivämärää. Pitää olla muodossa yyyy-mm-dd. | Pakollinen osa tietokantaa ja käyttöliittymää | 2000-01-01
end_date | Date - kiertueen lopetuspäivämäärä. Pitää olla muodossa yyyy-mm-dd. | Pakollinen osa tietokantaa ja käyttöliittymää | 2099-01-01



#### role eli käyttäjärooli
attribuutti | kuvaus | merkitys | esimerkki
--- | --- | --- | ---
id | Roolin tunnus, kokonaisluku, joka muodostuu itsestään, kun käyttäjälle luodaan rooli | pääavain| 1
name | Roolin nimi eli admin tai user. Kun käyttäjä rekisteröityy hänelle asetetaan user-rooli | Keskeinen ohjelman käyttämisen/hallinnoinnin kannalta | admin tai user




#### gig eli keikka
attribuutti | kuvaus | merkitys | esimerkki
--- | --- | --- | ---
id | Keikan tunnus, kokonaisluku, joka muodostuu itsestään, kun keikka luodaan | pääavain| 1
name | Keikan nimi, joka on merkkijono. Luodaan keikan luonnin yhteydessä.  | pakollinen ja käytön kannalta olennainen | testikeikka
place | Keikkapaikan nimi, joka on merkkijono. Luodaan keikan luonnin yhteydessä | olennainen käytön kannalta | Tavastia
pvm | Keikan päivämäärä, DATETIMe, jonka tulee olla muodossa yyyy-mm-dd. Kenttä validoidaan luodessa | olennainen käytön kannalta | 2019-03-03
showtime | Keikan aloitusaika, TIME, jonka tulee olla muodossa HH:MM. Tietokanta käyttää pidempää muotoa, mutta käytön helpoittamiseksi riittää, että vain tunnit ja minuutit asetetaan | 23:00
status | Keikan status, merkkijono, joka kuvaa onko keikka tulossa, mennyt vai peruttu. | ei olennainen, mutta helpottaa käyttöä | "upcoming" 
tour_id | Kokonaisluku, joka kuvaa mihin kiertueeseen keikka liittyy | pakollinen ja vieras avain | 2




CREATE TABLE -lausee: 

- CREATE TABLE tour (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	start_date DATETIME NOT NULL, 
	end_date DATETIME NOT NULL, 
	PRIMARY KEY (id)
);



- CREATE TABLE role (
	id INTEGER NOT NULL, 
	name VARCHAR(5) NOT NULL, 
	PRIMARY KEY (id)
);

- CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	role_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(role_id) REFERENCES role (id)
);

- CREATE TABLE gig (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	place VARCHAR(144) NOT NULL, 
	pvm DATETIME NOT NULL, 
	showtime TIME NOT NULL, 
	status VARCHAR(144) NOT NULL, 
	account_id INTEGER NOT NULL, 
	tour_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(tour_id) REFERENCES tour (id)
);

- CREATE TABLE tours_users (
	account_id INTEGER, 
	tour_id INTEGER, 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(tour_id) REFERENCES tour (id)
);
