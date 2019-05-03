
### Käyttötapauksia

1. Muusikko on lähdössä keikalle. Edellisenä iltana hän avaa sovelluksen ja katsoo keikkapäivän aikataulut ja speksit: mistä on lähtö, kuinka kauan matka kestää, monelta on load-in, soundcheck, showtime sekä miten ruokailu on järjestetty. (osittain toteutettu, lisätietolaatikko pitänee lisätä)
2. Muusikko katsoo alkuvuodesta, että millainen kiertue on tulossa. Hän avaa pääsivun ja tarkastelee keikkoja sieltä. Hän voi myös valita vain tietyn artistin keikat, jos hän soittaa useammassa bändissä (filteröinti toimii, paikan tai kiertueen nimen mukaan). 
3. Admin voi poistaa vääriä keikkoja ja tulevaisuudessa myös muokata keikan tietoja - esimerkiksi vaihtunutta showtimea (toimii). 
4. Uusi kiertue on alkamassa ja kaikki crewin ja bändin jäsenet haluaisivat keikkojen tarkat tiedot etukäteen. Admin voi lisätä kiertueen tiedot ja liittää soittajat kiertueeseen, jonka jälkeen he pystyvät tarkastelemaan koko kiertuetta keskitetysti (soittajat - kiertue on monesta moneen -suhde).
5. Uusi käyttäjä haluaa luoda tunnukset. Hän painaa 'rekisteröidy' ja syöttää tunnukset. Lomakkeen kentät on validoitu. Rekisteröitymisen onnistuttua käyttäjälle luodaan automaattisesti "muut -kiertue". 





### Admin
- Admin haluaa listata kaikki keikat 

```
> `SELECT * FROM GIG`
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



### Käyttäjä 
- Haluaa nähdä kuinka monta tulevaa, mennyttä tai peruttua keikkaa hänellä on: 


```
> `SELECT COUNT (gig.id) FROM Gig WHERE tour_id IN (SELECT tour_id FROM tours_users WHERE account_id = :account_id) and gig.status='Upcoming';")`
> SELECT COUNT (gig.id) FROM Gig WHERE tour_id IN (SELECT tour_id FROM tours_users WHERE account_id = :account_id) and gig.status='Past';")`
> SELECT COUNT (gig.id) FROM Gig WHERE tour_id IN (SELECT tour_id FROM tours_users WHERE account_id = :account_id) and gig.status='Cancelled';"`
```


- Haluaa nähdä häneen liittyvät keikat: 