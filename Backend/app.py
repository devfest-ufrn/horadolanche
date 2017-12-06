from flask import Flask
import json
from flask import request, jsonify

from handlers.UsersHandler import *
from handlers.SellersHandler import *
from handlers.UnregisteredUsersHandler import *
from handlers.ProductsHandler import *
from handlers.UserSellerHandler import *
from handlers.ProductCategoryHandler import *

app = Flask(__name__)
db = 'data/sqlalchemy_hdl.db'

@app.route("/")
def welcome():
	return "Welcome to the project's API.",200

@app.route("/users", methods=['GET','POST'])
@app.route("/users/<user_id>", methods=['GET','PUT', 'DELETE'])
def usersView(user_id=None):
	return usersHandler(user_id)

@app.route("/unregistered-users", methods=['GET','POST'])
@app.route("/unregistered-users/<user_id>", methods=['GET','PUT', 'DELETE'])
def unregisteredUsersView(user_id=None):
	return unregisteredUsersHandler(user_id)

@app.route("/sellers", methods=['GET','POST'])
@app.route("/seller/<seller_id>", methods=['GET','PUT', 'DELETE'])
def sellersView(seller_id=None):
	return sellersHandler(seller_id)

@app.route("/products", methods=['GET','POST'])
@app.route("/product/<product_id>", methods=['GET','PUT', 'DELETE'])
def productsView(product_id=None):
	return productsHandler(product_id)

@app.route("/userseller", methods=['GET','POST'])
@app.route("/userseller/<relation_id>", methods=['GET', 'DELETE'])
def userSellerView(relation_id=None):
	return userSellerHandler(relation_id)

@app.route("/productcategory", methods=['GET','POST'])
@app.route("/productcategory/<relation_id>", methods=['GET', 'DELETE'])
def productCategoryView(relation_id=None):
	return productCategoryHandler(relation_id)


app.run()