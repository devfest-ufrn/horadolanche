import sqlite3
import json


def toJSON(cursor,fetchall=True):
	columns = cursor.description
	result = [{columns[index][0]:column for index, column in enumerate(value)}   
  		for value in (cursor.fetchall() if fetchall else cursor.fetchone())]
  	return result

def readUnregisteredUser(database, user_id):
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''SELECT * FROM unregistereduser WHERE id = ?''', (user_id))
		result = toJSON(cursor)	
	except Exception as e:
		conn.rollback()
		return ''
	finally:
		conn.close()
	
	return result

def readUnregisteredUsers(database):
	try:
		conn = sqlite3.connect(database)		
		cursor = conn.cursor()
		cursor.execute('''SELECT * FROM unregistereduser''')
		
		result = toJSON(cursor,True)
	except Exception as e:
		conn.rollback()
		return ''
	finally:
		conn.close()

	return result

def createUnregisteredUser(database, name, latitude=None, longitude=None):
	success = True
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''INSERT INTO unregistereduser(name,latitude,longitude) VALUES (?,?,?)''', (format(name),latitude,longitude))

		conn.commit()
	except Exception as e:	
		conn.rollback()
		success = False
	finally:
		conn.close()

	return success

def updateUnregisteredUser(database, id, name=None, latitude=None, longitude=None):
	success = True
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()

		if name != None:
			cursor.execute('''UPDATE unregistereduser SET name = ?, latitude = ?, longitude = ? WHERE id = ?''', (format(name), latitude,longitude, id))
		else:
			cursor.execute('''UPDATE unregistereduser SET latitude = ?, longitude = ? WHERE id = ?''', (latitude,longitude, id))
	
		conn.commit()
	except Exception as e:
		conn.rollback()
		success = False
	finally:
		conn.close()

	return success

def deleteUnregisteredUser(database, id):
	success = True
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''DELETE FROM unregistereduser WHERE id = ?''', (id))

		conn.commit()
	except Exception as e:	
		conn.rollback()
		success = False
	finally:
		conn.close()

	return success