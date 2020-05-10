from flask import abort
from config import db
from models import Population, PopulationSchema

# funktiota kutsutaan, kun käyttäjä tekee GET-pyynnön
# URL-päätepisteeseen /api/populations
def read_all():

    # tehdään kysely population-tietokantaan
    # kysely palauttaa listan Population-olioita, jotka
    # talletetaan muuttujaan populations
    populations = Population.query \
        .order_by(Population.country_name) \
        .all()

    # populations listan sisältämä tieto 'sarjallistetaan' (serialize)
    # tämä tehdään, jotta tieto saadaan JSON-muotoon
    population_schema = PopulationSchema(many=True)
    return population_schema.dump(populations)


# vastaa, kun tehdään GET-pyyntö URL-päätepisteeseen /api/populations/{country_id}
def read_one(country_id):

    # tehdään kysely tietokantaan
    # tulos hyväksytään, jos rivin kentän country_id sisältämä arvo
    # on sama kuin pyyntöön liitetty

    population = Population.query \
        .filter(Population.country_id == country_id) \
        .one_or_none()

    if population is not None:
        population_schema = PopulationSchema()
        return population_schema.dump(population)

    else:
        abort(
            404,
            f'Population not found for country_id: {country_id}'
        )