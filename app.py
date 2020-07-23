from flask import json, jsonify, app, Flask, render_template
from model import User, BaseProperty
from service import ViewProperty, NewBill, PurchaseProperty, Login
from datetime import date


app = Flask(__name__)


@app.route('/')
def default():
    return render_template('Index.html')


def login(username, password):
    credential = username, password
    message = Login.login(credential)
    return message


#  after approved, when purchase button clicked, transaction start:
#  t1: signed contract & checkout to 3rd party payment api
#  t2: if payment success/ receive payment success token from 3rd party payment api, then insert payment into billing table
#  t3: execute transfer ownership
def purchase(property_id, property_uid, ownership_id):
    today = date.today()
    bill = (today, "purchase", 500000.00, today, property_id)
    token = NewBill.create_bill(bill)
    if token is True:
        purchased_property = ()
        token = PurchaseProperty.transfer_ownership(purchased_property, 1, property_uid, ownership_id)
    return token


@app.route('/url_path')
def name():
    records = ViewProperty.view_all_property()
    list = []
    for record in records:
        baseProp = BaseProperty.BaseProperty(record)
        do = vars(baseProp)
        list.append(do)
    return jsonify(list)


@app.route('/url_path2')
def summary():
    records = ViewProperty.view_all_property()
    list = []
    for record in records:
        baseProp = BaseProperty.BaseProperty(record)
        do = vars(baseProp)
        list.append(do)
    response = app.response_class(
        response=json.dumps(list),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)
