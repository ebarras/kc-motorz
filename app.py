from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1/kcmotorz'
db = SQLAlchemy(app)

from models import *

@app.route('/')
def home():
	return "Hello"

@app.route('/admin')
def admin():
	cars = (db.session.query(Cars)
			.filter(Cars.is_sold == 0)
			.filter(Cars.deleted_at == None)
			.order_by(Cars.sale_date.desc())
			.all()
		)
	return render_template('admin/index.html', cars=cars)

@app.route('/admin/charts')
def admin_charts():
    return render_template('admin/charts.html')



if __name__ == '__main__':
	app.run(debug=True)