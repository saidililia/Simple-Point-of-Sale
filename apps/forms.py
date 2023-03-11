from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField, validators, SubmitField
# ALMOST DONE WITH FORMS
class ProductForm(FlaskForm):
    name = StringField("Product Name")
    price = IntegerField("price")
    tax = IntegerField("tax")
    image = FileField()
    submit = SubmitField()
    
    pass

class DiscountForm(FlaskForm):
    name = StringField("Discount Name")
    percentage = IntegerField("percentage")
    submit = SubmitField()
   
    pass