from flask import json, jsonify, app, Flask, render_template
from model import User, BaseProperty
from service import DisplayChart, FilterProperty, Login, NewBill, Payment, PurchaseProperty, Register, RentProperty, \
    RequestApproval, UpdateProperty, UploadDocument, UploadImage, ViewBilling, ViewProperty, ViewPropertyDetails, \
    ViewRequest, UpdateBilling
from utils import common
from datetime import date


app = Flask(__name__)


@app.route('/')
def default():
    return render_template('Index.html')


def login(username, password):
    credential = username, password
    message = Login.sign_in(input_credential=credential)
    return message


def register(user_details):  # user id = uuid (get from common)
    user = User.User(user=user_details)
    token = Register.sign_up(user=user)
    return token[1]


def property_for_rent():
    return ViewProperty.rent()


def property_for_sale():
    return ViewProperty.sale()


def my_property(user_id):
    return ViewProperty.self(user_id=user_id)


def filter_property_for_rent(attribute_list):
    return FilterProperty.filter_rent(filter_list=attribute_list)


def filter_property_for_sale(attribute_list):
    return FilterProperty.filter_rent(filter_list=attribute_list)


def property_details(property_id):
    return ViewPropertyDetails.display(property_id=property_id)


def overview_billing(property_id):
    return ViewBilling.overview(property_id=property_id)


def my_billing(property_id):
    return ViewBilling.user(property_id=property_id)


def admin_billing(property_uid):
    return ViewBilling.admin(property_uid=property_uid)


def update_billing(new_billing_details, billing_id):
    token = UpdateBilling.modify(value=new_billing_details, billing_id=billing_id)
    if token is True:
        return "Billing Updated Successfully!"
    else:
        return "Unable to Update Billing!"


def my_incoming_request(ownership_id):
    return ViewRequest.incoming(ownership_id=ownership_id)


def my_outgoing_request(user_id):
    return ViewRequest.outgoing(user_id=user_id)


def admin_request():
    return ViewRequest.admin()


def respond_request(status, request_id):
    token = RequestApproval.response(request_status=status, request_id=request_id)
    return token


def make_request(new_request_details):
    token = RequestApproval.request(value=new_request_details)
    return token


def upload_property(csv_file):
    token = UploadDocument.send(csv_file=csv_file)
    if token is True:
        return "Property List Uploaded Successfully!"
    else:
        return "Unable to Upload Property List!"


def update_property_details(new_property_details, property_id):
    token = UpdateProperty.modify(value=new_property_details, property_id=property_id)
    if token is True:
        return "Property Updated Successfully!"
    else:
        return "Unable to Update The Property!"


def rent_property(user_id, property_id):
    token = RentProperty.rent(user_id=user_id, property_id=property_id)
    return token


def purchase_property(new_property_details, previous_property_uid, previous_ownership_id):
    token = PurchaseProperty.transfer(value=new_property_details, is_deleted=1, row_id_1=previous_property_uid, row_id_2=previous_ownership_id)
    return token


def payment(billing_id):
    payment_date = date.today()
    token = Payment.pay(payment_date=payment_date, billing_id=billing_id)
    return token


def new_bill(new_billing_details):
    token = NewBill.create(value=new_billing_details)
    return token


def display_historical_price(property_uid):
    rent_price = []
    sell_price = []
    last_updated_date = []
    property_list = DisplayChart.show_historical_price(property_uid=property_uid)
    for each_property in property_list:
        rent_price.append(each_property.rent_price)
        sell_price.append(each_property.sell_price)
        last_updated_date.append(each_property.last_updated_date)
    price_date_list = list(zip(rent_price, sell_price, last_updated_date))
    return price_date_list


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
