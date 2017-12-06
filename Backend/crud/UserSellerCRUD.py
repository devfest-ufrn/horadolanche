import sqlite3
import json

from UsersCRUD import readUser
from SellersCRUD import readSeller

def toJSON(cursor,fetchall=True):
	columns = cursor.description
	result = [{columns[index][0]:column for index, column in enumerate(value)}   
  		for value in (cursor.fetchall() if fetchall else cursor.fetchone())]
	return result

def readUserSeller(database, relation_id):
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''SELECT * FROM userseller WHERE id = ?''', (relation_id))
		result = toJSON(cursor)	
	except Exception as e:
		conn.rollback()
		return ''
	finally:
		conn.close()
	
	return result

def catchFollowedSellers(database, user_id):
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''SELECT seller FROM userseller WHERE user = ?''', (user_id))
		result = toJSON(cursor)	
	except Exception as e:
		conn.rollback()
		return ''
	finally:
		conn.close()
	
	return result

def catchID(database, user_id, seller_id):
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''SELECT id FROM userseller WHERE user = ? and seller = ?''', (user_id,seller_id))
		result = toJSON(cursor)	
	except Exception as e:
		conn.rollback()
		return ''
	finally:
		conn.close()
	
	return result


def readUsersSellers(database):
	try:
		conn = sqlite3.connect(database)		
		cursor = conn.cursor()
		cursor.execute('''SELECT * FROM userseller''')
		
		result = toJSON(cursor,True)
	except Exception as e:
		conn.rollback()
		return ''
	finally:
		conn.close()

	return result

def createUserSeller(database, user_id, seller_id):
	success = True
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()

		if(user_id != seller_id):
			if((readUser(database, user_id) != '') and (readSeller(database, seller_id) != '') and
				(catchID(user_id,seller_id) == '')):
				cursor.execute('''INSERT INTO userseller(user, seller) VALUES (?,?)''', (user_id, seller_id))
				conn.commit()
			else:
				success = False
		else:
			success = False
	except Exception as e:	
		conn.rollback()
		success = False
	finally:
		conn.close()

	return success

def deleteUserSeller(database, relation_id):
	success = True
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''DELETE FROM userseller WHERE id = ?''', (relation_id))

		conn.commit()
	except Exception as e:	
		conn.rollback()
		success = False
	finally:
		conn.close()

	return success