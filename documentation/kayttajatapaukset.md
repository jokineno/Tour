
### Käyttötapauksia

1. Muusikko on lähdössä keikalle. Edellisenä iltana hän avaa sovelluksen ja katsoo keikkapäivän aikataulut ja speksit: mistä on lähtö, kuinka kauan matka kestää, monelta on load-in, soundcheck, showtime sekä miten ruokailu on järjestetty. (osittain toteutettu, lisätietolaatikko pitänee lisätä)
2. Muusikko katsoo alkuvuodesta, että millainen kiertue on tulossa. Hän avaa pääsivun ja tarkastelee keikkoja sieltä. Hän voi myös valita vain tietyn artistin keikat, jos hän soittaa useammassa bändissä (filteröinti toimii, paikan tai kiertueen nimen mukaan). 
3. Admin voi poistaa vääriä keikkoja ja tulevaisuudessa myös muokata keikan tietoja - esimerkiksi vaihtunutta showtimea (toimii). 
4. Uusi kiertue on alkamassa ja kaikki crewin ja bändin jäsenet haluaisivat keikkojen tarkat tiedot etukäteen. Admin voi lisätä kiertueen tiedot ja liittää soittajat kiertueeseen, jonka jälkeen he pystyvät tarkastelemaan koko kiertuetta keskitetysti (soittajat - kiertue on monesta moneen -suhde).
5. Uusi käyttäjä haluaa luoda tunnukset. Hän painaa 'rekisteröidy' ja syöttää tunnukset. Lomakkeen kentät on validoitu. Rekisteröitymisen onnistuttua käyttäjälle luodaan automaattisesti "muut -kiertue". 





### Admin
- Admin haluaa listata kaikki keikat, jossa on mukana kiertueen nimi 

```
> `SELECT gig.pvm, gig.name, gig.place, gig.showtime, gig.status, tour.name FROM GIG INNER JOIN Tour on Gig.tour_id = Tour.id;`
```

- Admin haluaa hakea keikkoja kiertueen nimen mukaan: 


```
> `SELECT gig.id, gig.pvm, gig.name, gig.place, gig.showtime, gig.status, tour.name FROM GIG INNER JOIN TOUR on Gig.tour_id = Tour.id WHERE Tour.name LIKE '%{?}%';`
Parametreinä query eli itse haku. 
```

- Admin haluaa listata kaikki kiertueet

```
> `SELECT * FROM Tour`
```

- Admin haluaa listata kaikki keikat siten, että näkee myös kiertueen nimen: 

```
> `SELECT gig.pvm, gig.name, gig.place, gig.showtime, gig.status, tour.name FROM Gig INNER JOIN Tour on Gig.tour_id = Tour.id;`
```

- Admin haluaa listata kiertueet keikkojen määrän mukaan: 

```
> `SELECT tour.name, count(*) FROM Gig INNER JOIN tour ON Tour.id=gig.tour_id  GROUP BY tour.name;`
```

- Admin haluaa listata käyttäjät keikkojen määrän mukaan: 


```
> `SELECT account.name, count(*) FROM tours_users INNER JOIN account ON tours_users.account_id = account.id GROUP BY account.name;`
```


- Admin haluaa lisätä uuden keikan: 


```
> `INSERT INTO GIG (id, name, place,pvm, showtime, status, account_id, tour_id) VALUES (?,?,?,?,?,?,?,?);`
Parametreinä, id, nimi, paikka, päivämäärä, showtime, status, keikkaan liittyvä id ja keikkaan liittyvä kiertue. 
```

- Admin haluaa poistaa käyttäjän: 

```
> `DELETE FROM account WHERE account.id = ?`
Parametrinä käyttäjän id account.id
```



### Käyttäjä 
- Haluaa nähdä kuinka monta tulevaa, mennyttä tai peruttua keikkaa hänellä on: 

```
> `SELECT COUNT (gig.id) FROM Gig WHERE tour_id IN (SELECT tour_id FROM tours_users WHERE account_id = :account_id) and gig.status='Upcoming';")`

> SELECT COUNT (gig.id) FROM Gig WHERE tour_id IN (SELECT tour_id FROM tours_users WHERE account_id = :account_id) and gig.status='Past';")`

> SELECT COUNT (gig.id) FROM Gig WHERE tour_id IN (SELECT tour_id FROM tours_users WHERE account_id = :account_id) and gig.status='Cancelled';"`
```


- Käyttäjä haluaa nähdä häneen liittyvät keikat: 

```
> `SELECT gig.pvm, gig.name, gig.place, gig.showtime, gig.status, tour.name FROM GIG INNER JOIN TOUR on Gig.tour_id = Tour.id WHERE tour_id IN (SELECT tour_id FROM tours_users WHERE account_id = :account_id)`
```

- Käyttäjä haluaa listata hänen keikkansa nousevaan tai laskevaan järjestykseen:

```
> `SELECT gig.id, gig.pvm, gig.name, gig.place, gig.showtime, gig.status, tour.name FROM GIG INNER JOIN TOUR on Gig.tour_id = Tour.id WHERE tour_id IN (SELECT tour_id FROM tours_users WHERE account_id = :account_id) ORDER BY gig.pvm"`

`SELECT gig.id, gig.pvm, gig.name, gig.place, gig.showtime, gig.status, tour.name FROM GIG INNER JOIN TOUR on Gig.tour_id = Tour.id WHERE tour_id IN (SELECT tour_id FROM tours_users WHERE account_id = :account_id) ORDER BY gig.pvm DESC"`
```

- Käyttäjä haluaa hakea keikkoja kiertueen nimen mukaan


```
> `SELECT gig.id, gig.pvm, gig.name, gig.place, gig.showtime, gig.status, tour.name FROM GIG INNER JOIN TOUR on Gig.tour_id = Tour.id WHERE Tour.name LIKE '%{?}%'  AND tour_id IN (SELECT tour_id FROM tours_users WHERE account_id = :account_id);`

parametreinä query eli haku ja account_id
```

