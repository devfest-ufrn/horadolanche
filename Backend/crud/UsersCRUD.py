import sqlite3
import json


def toJSON(cursor,fetchall=True):
	columns = cursor.description
	result = [{columns[index][0]:column for index, column in enumerate(value)}   
  		for value in (cursor.fetchall() if fetchall else cursor.fetchone())]
	return result

def readUser(database, user_id):
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''SELECT * FROM user WHERE id = ?''', (user_id))
		result = toJSON(cursor)
	except Exception as e:
		conn.rollback()
		return ''
	finally:
		conn.close()
	
	return result

def readUsers(database):
	try:
		conn = sqlite3.connect(database)		
		cursor = conn.cursor()
		cursor.execute('''SELECT * FROM user''')
		
		result = toJSON(cursor,True)
	except Exception as e:
		conn.rollback()
		return ''
	finally:
		conn.close()

	return result

def createUser(database, username, email, password, name, account_image=None, latitude=None, longitude=None):
	success = True
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''INSERT INTO user(username, email, password, name, account_image, latitude, longitude) VALUES (?,?,?,?,?,?,?)''',
		 (format(username), format(email), password, format(name), account_image, latitude, longitude))

		conn.commit()
	except Exception as e:	
		conn.rollback()
		success = False
	finally:
		conn.close()

	return success

def updateUser(database, id, email=None, password=None, name=None, account_image=None, latitude=None, longitude=None):
	success = True
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()

		if email != None:
			cursor.execute('''UPDATE user SET email = ? WHERE id = ?''', (email, id))
		if name != None:
			cursor.execute('''UPDATE user SET name = ? WHERE id = ?''', (format(name), id))
		if password != None:
			cursor.execute('''UPDATE user SET password = ? WHERE id = ?''', (password, id))
		if account_image != None:
			cursor.execute('''UPDATE user SET account_image = ? WHERE id = ?''', (account_image, id))
		if latitude != None:
			cursor.execute('''UPDATE user SET latitude = ? WHERE id = ?''', (latitude, id))
		if longitude != None:
			cursor.execute('''UPDATE user SET longitude = ? WHERE id = ?''', (longitude, id))
			
		conn.commit()
	except Exception as e:
		conn.rollback()
		success = False
	finally:
		conn.close()

	return success

def deleteUser(database, id):
	success = True
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''DELETE FROM user WHERE id = ?''', (id))

		conn.commit()
	except Exception as e:	
		conn.rollback()
		success = False
	finally:
		conn.close()

	return success