import os
# connexion moduulilla saa Swaggerin Python ohjelmaan
# Swagger tarjoaa hyödyllisiä työkaluja REST APIn tarkastelemista varten
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# kansio, jossa ohjelma toimii
basedir = os.path.abspath(os.path.dirname(__file__))

connex_app = connexion.App(__name__, specification_dir=basedir)

app = connex_app.app

# SQLAlchemy säätöjä
# ECHO saa aikaan SQL komentojen näkymisen konsolissa
# DATABASE_URI määrittää käytettävän tietokannan (sqlite) ja käytettävän tietokanta
# tiedoston nimen
# TRACK_MODIFICATIONS asettaa SQLAlchemyn tapahtuma järjestelmän pois päältä

app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'population.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# muuttujan db avulla päästään käsiksi tietokantaan
db = SQLAlchemy(app)

ma = Marshmallow(app)
