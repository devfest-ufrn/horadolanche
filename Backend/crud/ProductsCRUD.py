import sqlite3
import json

from UsersCRUD import readUser

def toJSON(cursor,fetchall=True):
	columns = cursor.description
	result = [{columns[index][0]:column for index, column in enumerate(value)}   
  		for value in (cursor.fetchall() if fetchall else cursor.fetchone())]
	return result

def readProduct(database, product_id):
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''SELECT * FROM product WHERE id = ?''', (product_id))
		result = toJSON(cursor)
	except Exception as e:
		conn.rollback()
		return ''
	finally:
		conn.close()
	
	return result

def catchProductBySeller(database, seller_id):
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''SELECT * FROM product WHERE seller = ?''', (seller_id))
		result = toJSON(cursor)	
	except Exception as e:
		conn.rollback()
		return ''
	finally:
		conn.close()
	
	return result


def readProducts(database):
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''SELECT * FROM product''')
		
		result = toJSON(cursor,True)
	except Exception as e:
		conn.rollback()
		return ''
	finally:
		conn.close()

	return result

def createProduct(database, seller_id, price, avaliable, image, start_sell_time=None, end_sell_time=None):
	success = True
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()

		if readSeller(database, seller_id) == '':
			success = False
		else:
			cursor.execute('''INSERT INTO product(seller_id, price, avaliable, image, start_sell_time, end_sell_time)
			 VALUES (?,?,?,?,?,?)''', (seller_id, price, bool(avaliable), image, start_sell_time, end_sell_time))
			conn.commit()
	except Exception as e:	
		conn.rollback()
		success = False
	finally:
		conn.close()

	return success

def updateProduct(database, product_id, price = None, avaliable = None,
 image = None, start_sell_time = None, end_sell_time = None):
	success = True
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()

		if price != None:
			cursor.execute('''UPDATE product SET price = ? WHERE id = ?''', (price, id))
		if avaliable != None:
			cursor.execute('''UPDATE product SET avaliable = ? WHERE id = ?''', (bool(avaliable), id))
		if image != None:
			cursor.execute('''UPDATE product SET image = ? WHERE id = ?''', (image, id))
		if start_sell_time != None:
			cursor.execute('''UPDATE product SET start_sell_time = ? WHERE id = ?''', (start_sell_time, id))
		if end_sell_time != None:
			cursor.execute('''UPDATE product SET end_sell_time = ? WHERE id = ?''', (end_sell_time, id))

		conn.commit()
	except Exception as e:
		conn.rollback()
		success = False
	finally:
		conn.close()

	return success

def deleteProduct(database, product_id):
	success = True
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''DELETE FROM product WHERE id = ?''', (product_id))

		conn.commit()
	except Exception as e:	
		conn.rollback()
		success = False
	finally:
		conn.close()

	return success