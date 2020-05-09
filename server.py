from flask import render_template

# connexion moduulilla saa Swaggerin Python ohjelmaan
# Swagger tarjoaa hyödyllisiä työkaluja REST APIn tarkastelemista varten
import connexion

app = connexion.App(__name__, specification_dir='./')

# tiedostosta konfiguroidaan URL-päätepisteet
app.add_api('swagger.yml')


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
