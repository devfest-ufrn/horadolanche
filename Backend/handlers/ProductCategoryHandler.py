import sqlite3
import json
from flask import request, jsonify
from crud.ProductCategoryCRUD import *

db = 'data/sqlalchemy_hdl.db'

def productCategoryHandler(relation_id=None):
	if request.method == "GET":
		if seller_id != None:
			result = readProductCategory(db, relation_id)
			if result != '':
				return json.dumps(result), 200
			else:
				return "Not Found", 404
		else:
			result = readProductsCategories(db)
			if result != '':
				return json.dumps(result), 200
			else:
				return "Not Found", 404
	
	elif request.method == "DELETE":
		if deleteProductCategory(db, relation_id):
			return "Operation Complete\n", 200
		else:
			return "Operation Fail\n", 500

	elif request.method == "POST":
		product_id = request.form['product_id']
		category = request.form['category']
		
		if createProductCategory(db, product_id, category):
			return "Operation Complete\n", 200
		else:
			return "Operation Fail\n", 500
