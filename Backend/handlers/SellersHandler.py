import sqlite3
import json
from flask import request, jsonify
from crud.SellersCRUD import *

db = 'data/sqlalchemy_hdl.db'

def sellersHandler(seller_id=None):
	if request.method == "GET":
		if seller_id != None:
			result = readSeller(db, seller_id)
			if result != '':
				return json.dumps(result), 200
			else:
				return "Not Found", 404
		else:
			result = readSellers(db)
			if result != '':
				return json.dumps(result), 200
			else:
				return "Not Found", 404
	elif request.method == "PUT":
		cnpj = request.form['cnpj']
		
		if updateSeller(db, seller_id, cnpj):
			return "Operation Complete\n", 200
		else:
			return "Operation Fail\n", 500

	elif request.method == "DELETE":
		if deleteSeller(db, seller_id):
			return "Operation Complete\n", 200
		else:
			return "Operation Fail\n", 500


	elif request.method == "POST":
		user_id = request.form['user_id']
		cpf = request.form['cpf']
		cnpj = request.form['cnpj']

		if createSeller(db, user_id, cpf, cnpj):
			return "Operation Complete\n", 200
		else:
			return "Operation Fail\n", 500