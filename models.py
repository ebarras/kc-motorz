from app import db
from sqlalchemy.dialects import mysql

class Cars(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	make = db.Column(db.String(255), unique=False)
	model = db.Column(db.String(255), unique=False)
	year = db.Column(db.Integer, unique=False)
	miles = db.Column(db.Integer, unique=False)
	color = db.Column(db.String(255), unique=False)
	is_for_sale  = db.Column(db.Integer, unique=False)
	purchase_price = db.Column(db.Float, unique=False)
	advertised_price = db.Column(db.Float, unique=False)
	deleted_at = db.Column(db.DateTime, unique=False)
	pictures = db.relationship('Pictures', backref='cars', lazy='dynamic')
	sale_date = db.Column(db.String(255), unique=False)
	is_sold = db.Column(db.Integer, unique=False)
	created_at = db.Column(db.DateTime, unique=False)

	def __init__(self, id, make, model, year, miles, color, is_for_sale, purchase_price, advertised_price, deleted_at, sale_date, is_sold):
	        self.id = id
	        self.make = make
	        self.model = model
	        self.year = year
	        self.miles = miles
	        self.color = color
	        self.is_for_sale = is_for_sale
	        self.purchase_price = purchase_price
	        self.advertised_price = advertised_price
	        self.deleted_at = deleted_at
	        self.sale_date = sale_date
	        self.is_sold = is_sold
	        self.created_at = created_at

	def __repr__(self):
	    return '<Make {}'.format(self.make)

class Pictures(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	file_name = db.Column(db.String(255), unique=False)
	car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), unique=False)

	def __init__(self, file_name, car_id):
		self.file_name = file_name
		self.car_id = car_id

	def __repr__(self):
	    return '<File_Name {}'.format(self.file_name)