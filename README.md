### About the project
- The documentation is written in Finnish. However, I give a brief description in English in this chapter.
- This repository is a code for a web app, which has a customer and an admin side. 
- Backend: Python (Flask)
- FrontEnd: BootStrap
- Database: sqlite3 locally and PostGreSQL in production. 


#### The Tour - a project description
- This project is a webapp, which is designed for creative live production teams. On a client side, customers can add events such as gigs or concerts which can be reviewed all who are attached to that event. Admins can make changes to the events. 
- The Tour makes it easy for everyone who is participated in a project to follow what are the upcoming events on a tour. 

#### Exententions
- Import events and add them to a calender app (google calender for example). 
- Notify teams if changes are made
- Flask based security side of the app 


### The Tour
The Tour on websovellus, joka on suunniteltu tapahtumatuotantoryhmille. Kiertueella on tapahtumia, keikkoja, joihin liittyy käyttäjiä. Peruskäyttäjät voivat tarkastella tulevia ja menneitä tapahtumiaan sovelluksen avulla kootusti. Superkäyttäjä ali admin voi lisätä uusia tapahtumia ja kiertueita, jotka liittyvät tiettyihin käyttäjiin. Tällä tavoin esimerkiksi uuden kiertueen ja sen tapahtumien keskittäminen kaikille kiertueen jäsenille helpottaa produktion organisointia. 


[Linkki tuotannossa olevaan sovellukseen](https://tsoha-tour-demo.herokuapp.com)
- Käytä mieluiten Google Chromea


### Testitunnukset:
#### Admin tunnuksella voit hallita sovellusta, käyttöoikeuksia, keikkojen ja kiertueiden lisäystä. 
#### Peruskäyttäjänä voit tarkastella käyttäjään liittyviä tietoja ja muokata oman profiilin tietoja. 
| Username | Password |
| -------- | -------- |
| admin    | admin    |
| user     | user     |
 


### Dokumentaatio
- [Käyttäjätapauksia](https://github.com/jokineno/Tour/blob/master/documentation/kayttajatapaukset.md)
- [Tietokannan rakenne](https://github.com/jokineno/Tour/blob/master/documentation/tietokanta.md)
- [Kehitettävää ja rajoituksia](https://github.com/jokineno/Tour/blob/master/documentation/rajoituksetjaehdotukset.md)
- [Käyttöohje](https://github.com/jokineno/Tour/blob/master/documentation/kaytto-ohje.md)
- [Asennusohje](https://github.com/jokineno/Tour/blob/master/documentation/installation_guide.md)
