# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps import db
# NOW IAM DONE WITH THE MODELS
#Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Integer)
    tax = db.Column(db.Integer)
    image = db.Column(db.String(200))
    pass

#Discount Model
class Discount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    percentage = db.Column(db.Integer)
    pass
'''
Add your models below
'''

