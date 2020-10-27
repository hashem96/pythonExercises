from . import db

class Product(db.Model): 

    # Create attributes (SQL columns)
    id =db.Column(db.Integer(), primary_key=True) 
    name=db.Column(db.String(64))
    price= db.Column(db.Float())
    quantity=db.Column(db.Integer())
    category= db.Column(db.String(64))

