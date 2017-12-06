import sqlite3
import json
from flask import request, jsonify
from crud.ProductsCRUD import *

db = 'data/sqlalchemy_hdl.db'

def productsHandler(product_id=None):
	if request.method == "GET":
		if seller_id != None:
			result = readProduct(db, product_id)
			if result != '':
				return json.dumps(result), 200
			else:
				return "Not Found", 404
		else:
			result = readProducts(db)
			if result != '':
				return json.dumps(result), 200
			else:
				return "Not Found", 404
	elif request.method == "PUT":
		price = request.form['price']
		avaliable = request.form['avaliable']
		image = request.form['image']
		start_sell_time = request.form['start_sell_time']
		end_sell_time = request.form['end_sell_time']
		
		if updateProduct(db, product_id, price, avaliable, image, start_sell_time, end_sell_time):
			return "Operation Complete\n", 200
		else:
			return "Operation Fail\n", 500

	elif request.method == "DELETE":
		if deleteSeller(db, product_id):
			return "Operation Complete\n", 200
		else:
			return "Operation Fail\n", 500

	elif request.method == "POST":
		seller_id = request.form['seller_id']
		price = request.form['price']
		avaliable = request.form['avaliable']
		image = request.form['image']
		start_sell_time = request.form['start_sell_time']
		end_sell_time = request.form['end_sell_time']

		if createSeller(db, seller_id, price, avaliable, image, start_sell_time, end_sell_time):
			return "Operation Complete\n", 200
		else:
			return "Operation Fail\n", 500
