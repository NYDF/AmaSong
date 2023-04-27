from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Cart, Product
from app.forms import CartForm

cart_routes = Blueprint('carts', __name__)


@cart_routes.route('/')
@login_required
def get_all_():
    """
    Query for all stocks
    """
    all_stocks = Stock.query.all()
    return json.dumps({"stocks": [stock.to_dict() for stock in all_stocks]})



@stock_routes.route('/new', methods=["POST"])
@login_required
def add_stock():
    # print('here--------------------------------------')
    form = StockForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        # print('here++++++++++++++++++++++++', form.data["symbol"])

        old_stock = Stock.query.filter_by(symbol=form.data["symbol"]).first()
        # print("********************", old_stock)

        if old_stock:
            return {"messages": "stock already exist"}

        else:
            new_stock = Stock(symbol=form.data["symbol"])
            # print('here@@@@@@@@@@@@@@@@@@@@', new_stock)
            db.session.add(new_stock)
            db.session.commit()
            return new_stock.to_dict()

    else:
        return form.errors
