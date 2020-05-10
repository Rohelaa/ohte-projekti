import os
from config import db
from models import Population
from itertools import islice
import csv

# valtioiden väkiluvut sisältävä csv-tiedosto
with open('C:/Users/bujak/Desktop/API_SP.POP.TOTL_DS2_en_csv_v2_988606.csv') as csvfile:
    # luodaan lista, johon talletetaan oliota
    population_data = []
    # DictReaderilla muunnetaan csv-tiedoston rivit dict-muotoon
    # islice moduulilla voidaan valikoida rivi, jolta lukeminen aloitetaan
    reader = csv.DictReader(islice(csvfile, 4, None))
    # lisätään dict-muodossa olevat rivit listaan
    for row in reader:
        population_data.append(row)


# Jos projektin hakemistosta löytyy tiedosto 'population.db',
# se poistetaan ja rivillä 25 luodaan sitten uusi
if os.path.exists('population.db'):
    os.remove('population.db')

# luodaan tietokanta
db.create_all()

# lisätään listassa oleva tieto sessioon
for country in population_data:

    # joissakin listassa olevissa olioissa kentän 'Country Name' arvo on 'Not Classified'
    # samoin joidenkin kenttien 'year_2018' arvo '' (tyhjä)
    # näitä ei nyt lisätä tietokantaan

    if country['Country Name'] == 'Not Classified' or country['2018'] == '':
        continue

    c = Population(country_name=country['Country Name'], year_2018=country['2018'])
    db.session.add(c)

# lisätään session data tietokantaan
db.session.commit()
