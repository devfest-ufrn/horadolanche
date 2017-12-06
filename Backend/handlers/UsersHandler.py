import sqlite3
import json
from flask import request, jsonify

from crud.UsersCRUD import *

db = 'data/sqlalchemy_hdl.db'

def usersHandler(user_id=None):
	if request.method == "GET":
		if user_id != None:
			result = readUser(db, user_id)
			if result != '':
				return json.dumps(result), 200
			else:
				return "Not Found", 404
		else:
			result = readUsers(db)
			if result != '':
				return json.dumps(result), 200
			else:
				return "Not Found", 404
	elif request.method == "PUT":
		email = request.form['email']
		password = request.form['password']
		name = request.form['name']
		account_image = request.form['account_image']
		latitude = request.form['latitude']
		longitude = request.form['longitude']

		if updateUser(db, user_id, email, password, name, account_image, latitude, longitude):
			return "Operation Complete\n", 200
		else:
			return "Operation Fail\n", 500

	elif request.method == "DELETE":
		if deleteUser(db, user_id):
			return "Operation Complete\n", 200
		else:
			return "Operation Fail\n", 500


	elif request.method =="POST":
		username = request.form['username']
		email = request.form['email']
		password = request.form['password']
		name = request.form['name']
		account_image = request.form['account_image']
		latitude = request.form['latitude']
		longitude = request.form['longitude']


		if createUser(db, username, email, password, name, account_image, latitude, longitude):
			return "Operation Complete\n", 200
		else:
			return "Operation Fail\n", 500