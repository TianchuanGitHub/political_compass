from flask import Flask
from flask import render_template
from peewee import *

db = SqliteDatabase('detainees.db')

class Country(Model):
    name = CharField()
    iso = CharField(primary_key=True)

    class Meta:
        database = db
        db_table = 'countries'

class Detainee(Model):
    country = ForeignKeyField(Country, related_name='detainees', to_field='iso', db_column='iso')
    name = CharField()
    isn = CharField(primary_key=True)
    nationality = CharField()
    iso = CharField()
    arrival_date = CharField()
    transfer_reason = CharField()
    capture_details = CharField()

    class Meta:
        database = db
        db_table = 'detainees'

app = Flask(__name__)

@app.route('/countries')
@app.route('/')
def index():
    countries = Country.select()
    return render_template('index.html', countries=countries)

@app.route('/country/<abbreviation>')
def show_country(abbreviation):
    country = Country.get(Country.iso == abbreviation)
    return render_template('country.html', country=country, abbreviation=abbreviation)

@app.route('/detainee/<isn>')
def show_detainee(isn):
    detainee = Detainee.get(Detainee.isn == isn)
    return render_template('detainee.html', detainee=detainee)

@app.route('/longest')
def longest():
    detainees = Detainee.select().where(Detainee.arrival_date != '').order_by(Detainee.arrival_date.asc()).limit(50)
    return render_template('longest.html', detainees=detainees)

@app.route('/stats')
def stats():
    earliest_arrival = Detainee.select().aggregate(fn.Max(Detainee.arrival_date))
    number_of_detainees = Detainee.select().count()
    return render_template('stats.html', earliest_arrival=earliest_arrival, number_of_detainees=number_of_detainees)

if __name__ == '__main__':
    app.run(debug=True)
