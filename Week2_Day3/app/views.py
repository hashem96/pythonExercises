import flask

from . import app # The directory where the file is currently (here is app/)
from . import forms
from .models import Product
from . import db

def add_Products():
    #adding and querying from the databse 
    product =Product(name="Macbook Pro", price=1000.99, quantity=3,category="technology")
    db.session.add(product)
    db.session.commit()

    product =Product(name="Dell Laptop", price=899.99, quantity=5,category="technology")
    db.session.add(product)
    db.session.commit()


    product =Product(name="Brita Water filter", price=39.00, quantity=2,category="kitchen")
    db.session.add(product)
    db.session.commit()


@app.route("/")
@app.route("/home")
def index():
    return flask.render_template("index.html", title="My awesome app", title2="Awesome app")

@app.route("/product/<product_id>")
def filter_product_by_id(product_id):

    for product in Product.query.all():
        if product.id == int(product_id):
            break
    else:
        return "Product not found"

    return flask.render_template("product_by_id.html", 
    product_name = product.name ,
    product_price =  product.price , 
    product_stock =  product.quantity , product_category = product.category)

@app.route("/search/by-category/<category>")
def search_product_by_category(category):
    category_products = []
    for product in Product.query.all():
        if product.category == category :
            category_products.append(product.name)
        
    return flask.render_template("products_by_category.html" , filtred_products = category_products)

