import sqlite3
import json

from UsersCRUD import readUser

def toJSON(cursor,fetchall=True):
	columns = cursor.description
	result = [{columns[index][0]:column for index, column in enumerate(value)}   
  		for value in (cursor.fetchall() if fetchall else cursor.fetchone())]
	return result

def readSeller(database, seller_id):
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''SELECT * FROM seller WHERE id = ?''', (seller_id))
		result = toJSON(cursor)	
	except Exception as e:
		conn.rollback()
		return ''
	finally:
		conn.close()
	
	return result

def catchSellerByUserID(database, user_id):
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''SELECT * FROM seller WHERE true_id = ?''', (user_id))
		result = toJSON(cursor)	
	except Exception as e:
		conn.rollback()
		return ''
	finally:
		conn.close()
	
	return result


def readSellers(database):
	try:
		conn = sqlite3.connect(database)		
		cursor = conn.cursor()
		cursor.execute('''SELECT * FROM seller''')
		
		result = toJSON(cursor,True)
	except Exception as e:
		conn.rollback()
		return ''
	finally:
		conn.close()

	return result

def createSeller(database, user_id, cpf, cnpj=None):
	success = True
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()

		if (readUser(database, user_id) == '') or (catchSellerByUserID(database, user_id) != ''):
			success = False
		else:
			cursor.execute('''INSERT INTO seller(true_id, cpf, cnpj) VALUES (?,?,?)''', (user_id, cpf, cnpj))
			conn.commit()
	except Exception as e:	
		conn.rollback()
		success = False
	finally:
		conn.close()

	return success

def updateSeller(database, seller_id, cnpj = None):
	success = True
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()

		cursor.execute('''UPDATE seller SET cnpj = ? WHERE id = ?''', (cnpj, seller_id))
			
		conn.commit()
	except Exception as e:
		conn.rollback()
		success = False
	finally:
		conn.close()

	return success

def deleteSeller(database, seller_id):
	success = True
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''DELETE FROM seller WHERE id = ?''', (seller_id))

		conn.commit()
	except Exception as e:	
		conn.rollback()
		success = False
	finally:
		conn.close()

	return success