# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import os
from apps.home import blueprint
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps.forms import ProductForm, DiscountForm
from apps.models import Product, Discount
from apps import db
from run import app
from werkzeug.utils import secure_filename


from apps.config import API_GENERATOR

items = []

@blueprint.route('/index')
@login_required
def index():
    product = Product.query.all()
    return render_template('home/index.html',segment='index', product=product ,API_GENERATOR=len(API_GENERATOR))

@blueprint.route('/items')
@login_required
def item():
    name = request.form.get("name")
    price = request.form.get("price")
    items.append(name)
    
    return redirect(url_for('home_blueprint.check', items= items, total = 100))


@blueprint.route('/result')
@login_required
def result():
    
    code = request.form['discount']
    bl = Discount.query.filter_by(name=code)
    if bl:
        flash('this is a valid discount code')
        return redirect('/check')
    else:
        flash('this is not a valid discount code')
        return redirect('/check')

@blueprint.route('/Reset')  
@login_required
def reset():
    items = []
    return render_template('home/check.html', segment='check')

@blueprint.route('/check')
@login_required
def check():
    product = Product.query.all()
    return render_template('home/check.html',segment='check', product=product, items=items, total=100)

@blueprint.route('/Product', methods=['GET', 'POST'])
@login_required
def product():
    form = ProductForm()
    if form.is_submitted():
        result = request.form
        product = Product()
        product.name = result['name']
        product.price = result['price']
        product.tax = result['tax']
        product.image = request.files['image'].filename
        
        # basedir = os.path.abspath(os.path.dirname(__file__))
        file = request.files['image']
        filename = secure_filename(file.filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER']), filename)
        
        db.session.add(product)
        db.session.commit()
        
    return render_template('home/Product.html', segment="Product",form=form)

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment, API_GENERATOR=len(API_GENERATOR))

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None



@blueprint.route('/Discount', methods=['GET','POST'])
@login_required
def discount():
    form = DiscountForm()
    result = request.form
    if form.is_submitted():
        discount = Discount()
        discount.name = result['name']
        discount.percentage = result['percentage']
        db.session.add(discount)
        db.session.commit()
        
    return render_template('home/Discount.html', segment="Discount" ,form=form)