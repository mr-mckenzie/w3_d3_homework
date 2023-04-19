from app import app
from flask import render_template

from models.order_database import orders

@app.route('/orders')
def index():
    return render_template('index.jinja', orders = orders)

@app.route('/orders/<index>')
def display_order(index):
    resulting_order=orders[int(index)]
    return render_template('order.jinja', order=resulting_order)