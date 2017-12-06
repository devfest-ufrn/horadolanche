import sqlite3
import json
from flask import request, jsonify
from crud.UserSellerCRUD import *

def userSellerHandler(relation_id=None):
	if request.method == "GET":
		if relation_id != None:
			result = readUserSeller(db, product_id)
			if result != '':
				return json.dumps(result), 200
			else:
				return "Not Found", 404
		else:
			result = readUsersSellers(db)
			if result != '':
				return json.dumps(result), 200
			else:
				return "Not Found", 404
	
	elif request.method == "DELETE":
		if deleteUserSeller(db, relation_id):
			return "Operation Complete\n", 200
		else:
			return "Operation Fail\n", 500

	elif request.method == "POST":
		user_id = request.form['user_id']
		seller_id = request.form['seller_id']
		
		if createUserSeller(db, user_id, seller_id):
			return "Operation Complete\n", 200
		else:
			return "Operation Fail\n", 500