import flask, flask_login
from . import app, db
from . import forms

from .models import User,Product

def add_Products():
    #adding products to database 
    product=Product(name="Macbook Pro", price=1000.99, quantity=3,category="technology")
    db.session.add(product)
    db.session.commit()

    product=Product(name="Dell Laptop", price=899.99, quantity=5,category="technology")
    db.session.add(product)
    db.session.commit()

    product=Product(name="Brita Water filter",price=39.00,quantity=2,category="kitchen")
    db.session.add(product)
    db.session.commit()


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def index():

    #In case the user is logged in he will see the second view where he 
    # can search for a product
    query_form = forms.QueryForm()
    if query_form.validate_on_submit():
        return flask.redirect(f"/search/by-name/{query_form.query.data}")
    else:
        print(query_form.errors)

    return flask.render_template("index.html", title="Quick Shop",query_form=query_form)



@app.route("/search/by-name/<product_name>")
@flask_login.login_required
def filter_product_by_name(product_name):

    for product in Product.query.all():
        if product.name == product_name:
            break
    else:
        return "Product not found"
    return flask.render_template("product_by_name.html", 
    product_name = product.name ,
    product_price =  product.price , 
    product_stock =  product.quantity , product_category = product.category)


@app.route("/product/<product_id>")
@flask_login.login_required
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
@flask_login.login_required
def search_product_by_category(category):
    category_products = []
    for product in Product.query.all():
        if product.category == category :
            category_products.append(product.name)
        
    return flask.render_template("products_by_category.html" , filtred_products = category_products)


@app.route("/sign-up", methods=["GET", "POST"])
def signup():
    form = forms.SignupForm()

    if flask.request.method == "POST":
        if form.validate_on_submit():

            user = User()
            user.name = form.username.data
            user.password = form.password.data
            user.save()

            return flask.redirect('/')
        else:
            print("Form errors:", form.errors)

    return flask.render_template("signup.html", form=form)


@app.route("/sign-in", methods=["GET", "POST"])
def signin():
    form = forms.SigninForm()
    if form.validate_on_submit():
        user = User.login_user(form.username.data, form.password.data)
        if user:
            return flask.redirect('/')

    return flask.render_template("signin.html", form=form)

@app.route("/sign-out")
def signout():
    flask_login.logout_user()
    return flask.redirect('/')

