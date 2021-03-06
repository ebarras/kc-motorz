from flask import Flask, render_template, redirect, url_for, abort
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1/kcmotorz'
db = SQLAlchemy(app)

from models import *

@app.route('/')
def home():
	return "Hello"

@app.route('/admin/')
@app.route('/admin/cars')
def admin_cars():
	cars = (db.session.query(Cars)
			.filter(Cars.is_sold == 0)
			.filter(Cars.deleted_at == None)
			.order_by(Cars.sale_date.desc())
			.all()
		)
	return render_template('admin/cars.html', cars=cars, heading="Cars", sub_heading="Cars Not Yet Sold")

@app.route('/admin/cars/all')
def admin_cars_all():
	cars = (db.session.query(Cars)
			.filter(Cars.deleted_at == None)
			.order_by(Cars.created_at.desc())
			.all()
		)
	return render_template('admin/cars.html', cars=cars, heading="All Cars", sub_heading="List of All Cars")

@app.route('/admin/cars/sold')
def admin_cars_sold():
	cars = (db.session.query(Cars)
			.filter(Cars.is_sold == 1)
			.filter(Cars.deleted_at == None)
			.order_by(Cars.sale_date.desc())
			.all()
		)
	return render_template('admin/cars.html', cars=cars, heading="Sold Cars", sub_heading="Cars That Have Been Sold")

@app.route('/admin/car/<int:car_id>')
def admin_car(car_id):
	try:
		car = (db.session.query(Cars)
				.filter(Cars.id == car_id)
				.one()
			)
	except NoResultFound:
		abort(404)
	return render_template('admin/car.html', car=car, heading='Edit Car', sub_heading=str(car.year) + ' ' + car.make + ' ' + car.model)

@app.route('/admin/car/add')
def admin_car_add():
	return render_template('admin/car_add.html', heading="New Car", sub_heading="Add a new car to the system.")

@app.route('/admin/charts')
def admin_charts():
    return render_template('admin/charts.html')



if __name__ == '__main__':
	app.run(debug=True)