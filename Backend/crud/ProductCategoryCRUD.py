import sqlite3
import json

from crud.ProductsCRUD import readProduct

def toJSON(cursor,fetchall=True):
	columns = cursor.description
	result = [{columns[index][0]:column for index, column in enumerate(value)}   
  		for value in (cursor.fetchall() if fetchall else cursor.fetchone())]
	return result

def readProductCategory(database, relation_id):
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''SELECT * FROM productcategory WHERE id = ?''', (relation_id))
		result = toJSON(cursor)
	except Exception as e:
		conn.rollback()
		return ''
	finally:
		conn.close()
	
	return result

def readProductsCategories(database):
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''SELECT * FROM productcategory''')
		
		result = toJSON(cursor,True)
	except Exception as e:
		conn.rollback()
		return ''
	finally:
		conn.close()

	return result

def createProductCategory(database, product_id, category):
	success = True
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()

		if readProduct(database, product_id) == '':
			success = False
		else:
			cursor.execute('''INSERT INTO productcategory(product_id, category)
			 VALUES (?,?)''', (product_id, category))
			conn.commit()
	except Exception as e:	
		conn.rollback()
		success = False
	finally:
		conn.close()

	return success

def deleteProductCategory(database, relation_id):
	success = True
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''DELETE FROM productcategory WHERE id = ?''', (relation_id))

		conn.commit()
	except Exception as e:	
		conn.rollback()
		success = False
	finally:
		conn.close()

	return success

def deleteAProduct(database, product_id):
	success = True
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''DELETE FROM productcategory WHERE product_id = ?''', (product_id))

		conn.commit()
	except Exception as e:	
		conn.rollback()
		success = False
	finally:
		conn.close()

	return success

def deleteACategory(database, category):
	success = True
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''DELETE FROM productcategory WHERE category = ?''', (category))

		conn.commit()
	except Exception as e:	
		conn.rollback()
		success = False
	finally:
		conn.close()

	return success

def readAProductCategories(database, product_id):
	try:
		conn = sqlite3.connect(database)
		cursor = conn.cursor()
		cursor.execute('''SELECT category FROM productcategory WHERE id = ?''', (product_id))
		result = toJSON(cursor)
	except Exception as e:
		conn.rollback()
		return ''
	finally:
		conn.close()
	
	return result