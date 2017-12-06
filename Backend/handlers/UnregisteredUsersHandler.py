import sqlite3
import json
from flask import request, jsonify
from crud.UnregisteredUsersCRUD import *

db = 'data/sqlalchemy_hdl.db'

def unregisteredUsersHandler(user_id=None):
	if request.method =="GET":
		if user_id != None:	
			result = readUnregisteredUser(db, user_id)
			if result != '':
				return json.dumps(result), 200
			else:
				return "Not Found", 404
		else:
			result = readUnregisteredUsers(db)
			if result != '':
				return json.dumps(result), 200
			else:
				return "Not Found", 404

	elif request.method == "PUT":
		name = request.form['name']
		latitude = request.form['latitude']
		longitude = request.form['longitude']

		if updateUnregisteredUser(db, user_id, name, latitude, longitude):
			return "Operation Complete\n", 200
		else:
			return "Operation Fail\n", 500

	elif request.method == "DELETE":
		if deleteUnregisteredUser(db, user_id):
			return "Operation Complete\n", 200
		else:
			return "Operation Fail\n", 500


	elif request.method =="POST":
		name = request.form['name']
		latitude = request.form['latitude']
		longitude = request.form['longitude']

		if createUnregisteredUser(db, name, latitude, longitude):
			return "Operation Complete\n", 200
		else:
			return "Operation Fail\n", 500