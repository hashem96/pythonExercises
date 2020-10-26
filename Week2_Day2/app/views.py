import flask

from . import app # The directory where the file is currently (here is app/)

from .models import products




@app.route("/")
@app.route("/home")
def index():
    return flask.render_template("index.html", title="Quick Shop")

@app.route("/product/<product_id>")
def filter_product_by_id(product_id):
    
    for product in products:
        if product["id"] == int(product_id):
            break
    else:
        return "Product not found"

    return flask.render_template("product_by_id.html", 
    product_name = product["name"] ,
    product_price =  product["price"] , 
    product_stock =  product["stock_quantity"] , product_category = product["category"])

@app.route("/search/by-category/<category>")
def search_product_by_category(category):
    category_products = []
    for product in products:
        if product["category"] == category :
            category_products.append(product["name"])
        
    return flask.render_template("products_by_category.html" , filtred_products = category_products)

