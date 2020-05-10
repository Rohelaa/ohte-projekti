from config import db, ma

# Olio-ohjelmointia hyödyntäen saadaan talletettua tietoa
# Python-olioon
class Population(db.Model):
    __tablename__ = 'population'
    country_id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String)
    year_2018 = db.Column(db.Integer)


# luokka, joka kuvaa, miten jonkin luokan attribuutit muunnetaan
# JSON-ystävälliseen muotoon
class PopulationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Population
        sqla_session = db.session
