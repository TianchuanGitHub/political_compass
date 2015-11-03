from flask import Flask
from flask import render_template
from peewee import *

app	= Flask(__name__)
db = SqliteDatabase('detainees.db')

class	Country(Model):
	name	=	CharField()
	iso	=	CharField(primary_key=True)
	
	class	Meta:
		database	=	db
		db_table	=	'countries'


class	Detainee(Model):
	name	=	CharField()
	isn	=	CharField(primary_key=True)
	nationality	=	CharField()
	iso	=	CharField()
	arrival_date	=	CharField()
	transfer_reason	=	CharField()
	capture_details	=	CharField()

	class	Meta:
		database	=	db
		db_table	=	'detainees'





@app.route('/')
def	index():
	return	render_template('index.html')

@app.route('/country/<abbreviation>')
def	show_country(abbreviation):
	return	render_template('country.html',abbreviation=abbreviation)

if	__name__	==	'__main__':
	app.run(debug=True)