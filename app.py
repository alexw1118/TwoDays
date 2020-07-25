from flask import json, jsonify, app, Flask, render_template, request
from model import User, BaseProperty
from service import Login, NewBill, Payment, PurchaseProperty, Register, RentProperty, \
    RequestApproval, UpdateProperty, UploadDocument, UploadImage, ViewBilling, ViewProperty, ViewPropertyDetails, \
    ViewRequest, UpdateBilling
from utils import common
from datetime import date


userA = []


app = Flask(__name__)


@app.route('/')
def default():
    return render_template('home.html')


@app.route('/login', methods=['POST'])
def admin_login():
    username = request.form['username']
    password = request.form['password']
    credential = username, password
    result = Login.sign_in(credential)
    token = result[0]
    msg = result[1]
    if token:
        print(msg)
        user = Login.user_detail(username)
        userA.append(username)
        property_list = ViewProperty.view_all()
        sold_property_list = ViewProperty.view_sold()
        request_list = ViewRequest.admin()
        billing_amount = ViewBilling.overview_unpaid()
        return render_template('dashboard.html', user=user, propertycount=len(property_list),
                               propertysold=len(sold_property_list), requestcount=len(request_list),
                               totalbillingamount=billing_amount)
    else:
        print(msg)
        return render_template('login.html')


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/viewAllProperty')
def view_property_page():
    if len(userA) != 0:
        username = userA[0]
        user = Login.user_detail(username)
        property_list = ViewProperty.admin()
        return render_template('viewAllProperty.html', user=user, propertylist=property_list)
    else:
        return render_template('login.html')


@app.route('/dashboard')
def dashboard_page():
    if len(userA) != 0:
        user = Login.user_detail(userA[0])
        property_list = ViewProperty.view_all()
        sold_property_list = ViewProperty.view_sold()
        request_list = ViewRequest.admin()
        billing_amount = ViewBilling.overview_unpaid()
        return render_template('dashboard.html', user=user, propertycount=len(property_list),
                               propertysold=len(sold_property_list), requestcount=len(request_list),
                               totalbillingamount=billing_amount)
    else:
        return render_template('login.html')


@app.route('/editAccount')
def edit_account_page():
    if len(userA) != 0:
        username = userA[0]
        user = Login.user_detail(username)
        return render_template('editProfilePage.html', user=user)
    else:
        return render_template('login.html')


@app.route('/manageProperty')
def manage_property_page():
    if len(userA) != 0:
        username = userA[0]
        user = Login.user_detail(username)
        property_list = ViewProperty.admin()
        return render_template('manageProperty.html', user=user, propertylist=property_list)
    else:
        return render_template('login.html')


@app.route('/registerProperty')
def register_property_page():
    if len(userA) != 0:
        username = userA[0]
        user = Login.user_detail(username)
        return render_template('registerProperty.html', user=user)
    else:
        return render_template('login.html')


@app.route('/registerP', methods=['POST'])
def register_property():
    if len(userA) != 0:
        username = userA[0]
        user = Login.user_detail(username)
        UID = request.form['UID']
        price = request.form['Price']
        PropertyType = request.form['PropertyType']
        YearBuilt = request.form['YearBuilt']
        TenureType = request.form['TenureType']
        Bedroom = request.form['Bedroom']
        Bathroom = request.form['Bathroom']
        Extraroom = request.form['ExtraRoom']
        Parking = request.form['Parking']
        Size = request.form['Size']
        FloorPlan = request.form['FloorPlan']
        Unit = request.form['Unit']
        Area = request.form['Area']
        Street = request.form['Street']
        District = request.form['District']
        State = request.form['State']
        Postcode = request.form['Postcode']
        Township = request.form['Township']
        inserted = UID, price, PropertyType, YearBuilt, TenureType, Bedroom, Bathroom, Extraroom, Parking, Size, FloorPlan, Unit, Area, Street, District, State, Postcode, Township
        UploadDocument.register_Property(inserted)
        return manage_property_page()
    else:
        return render_template('login.html')


@app.route('/redirect2UpdateP', methods=['POST'])
def redirect_update_property():
    if len(userA) != 0:
        username = userA[0]
        user = Login.user_detail(username)
        PropertyID = request.form['PropertyID']
        return render_template('editProperty.html', PropertyID=PropertyID, user=user)
    else:
        return render_template('login.html')


@app.route('/redirect2ViewDetails', methods=['POST'])
def redirect_property_details():
    if len(userA) != 0:
        username = userA[0]
        user = Login.user_detail(username)
        PropertyID = request.form['PropertyID']
        property_detail = ViewProperty.view_details(PropertyID)
        return render_template('viewDetails.html', property_detail=property_detail, user=user)
    else:
        return render_template('login.html')


@app.route('/viewRequest')
def redirect_view_request():
    if len(userA) != 0:
        username = userA[0]
        user = Login.user_detail(username)
        request_list = admin_request()
        requestuser = Login.user_detail(username)
        property_detail = ViewProperty.view_details(request_list[0]['PropertyID'])
        return render_template('viewAllRequest.html', user=user, request_list=request_list, requestuser=requestuser, property_detail=property_detail)
    else:
        return render_template('login.html')


@app.route('/updateP', methods=['POST'])
def update_property():
    if len(userA) != 0:
        username = userA[0]
        user = Login.user_detail(username)
        PropertyID = request.form['PropertyID']
        Furnish = request.form['Furnish']
        RentPrice = request.form['RentPrice']
        SellPrice = request.form['SellPrice']
        Usage = request.form['Usage']
        FreeUtility = request.form['FreeUtility']
        Images = request.form['Images']
        RentalStartDate = request.form['RentalStartDate']
        RentalEndDate = request.form['RentalEndDate']
        RentalPeriod = request.form['RentalPeriod']
        Description = request.form['Description']
        LastUpdatedDate = request.form['LastUpdatedDate']
        RentContract = request.form['RentContract']
        SellContract = request.form['SellContract']
        inserted = Furnish, RentPrice, SellPrice, Usage, FreeUtility, Images, RentalStartDate, RentalEndDate, RentalPeriod, Description, LastUpdatedDate, RentContract, SellContract, PropertyID
        UpdateProperty.modify(inserted)
        return manage_property_page()
    else:
        return render_template('login.html')


@app.route('/requestApprove', methods=['POST'])
def request_approve():
    if len(userA) != 0:
        RequestID = request.form['RequestID']
        value = 'Approve', RequestID
        respond_request(value)
        username = userA[0]
        user = Login.user_detail(username)
        request_list = admin_request()
        requestuser = Login.user_detail(username)
        property_detail = ViewProperty.view_details(request_list[0]['PropertyID'])
        return render_template('viewAllRequest.html', user=user, request_list=request_list, requestuser=requestuser,
                               property_detail=property_detail)
    else:
        return render_template('login.html')


@app.route('/requestReject', methods=['POST'])
def request_reject():
    if len(userA) != 0:
        RequestID = request.form['RequestID']
        value = 'Reject', RequestID
        respond_request(value)
        redirect_view_request()
        username = userA[0]
        user = Login.user_detail(username)
        request_list = admin_request()
        requestuser = Login.user_detail(username)
        property_detail = ViewProperty.view_details(request_list[0]['PropertyID'])
        return render_template('viewAllRequest.html', user=user, request_list=request_list, requestuser=requestuser,
                               property_detail=property_detail)
    else:
        return render_template('login.html')


@app.route('/redirect2BatchUpload')
def redirect_upload():
    if len(userA) != 0:
        username = userA[0]
        user = Login.user_detail(username)
        return render_template('uploadExcelFile.html', user=user)
    else:
        return render_template('login.html')


@app.route('/batchUploadProperty', methods=['POST'])
def batch_upload():
    f = request.form['csvfile']
    upload_property(f)
    user = Login.user_detail(userA[0])
    property_list = ViewProperty.view_all()
    sold_property_list = ViewProperty.view_sold()
    request_list = ViewRequest.admin()
    billing_amount = ViewBilling.overview_unpaid()
    return render_template('dashboard.html', user=user, propertycount=len(property_list),
                           propertysold=len(sold_property_list), requestcount=len(request_list),
                           totalbillingamount=billing_amount)


def login(username, password):
    credential = username, password
    message = Login.sign_in(input_credential=credential)
    return message


def register(user_details):  # user id = uuid (get from common)
    user = User.User(user=user_details)
    token = Register.sign_up(user=user)
    return token


def property_for_rent():
    return ViewProperty.rent()


def property_for_sale():
    return ViewProperty.sale()


def my_property(user_id):
    return ViewProperty.self(user_id=user_id)


def admin_property():
    return ViewProperty.admin()


def property_details(property_id):
    return ViewPropertyDetails.display(property_id=property_id)


def overview_billing(property_id):
    return ViewBilling.overview(property_id=property_id)


def my_billing(property_id):
    return ViewBilling.user(property_id=property_id)


def admin_billing(property_uid):
    return ViewBilling.admin(property_uid=property_uid)


def update_billing(new_billing_details):
    token = UpdateBilling.modify(value=new_billing_details)
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


def respond_request(value):
    token = RequestApproval.response(value=value)
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


def update_property_details(new_property_details):
    token = UpdateProperty.modify(value=new_property_details)
    if token is True:
        return "Property Updated Successfully!"
    else:
        return "Unable to Update The Property!"


def rent_property(value):
    token = RentProperty.rent(value=value)
    return token


def purchase_property(new_property_details, previous_property_uid, previous_ownership_id):
    token = PurchaseProperty.transfer(value=new_property_details, property_uid=previous_property_uid, ownership_id=previous_property_uid)
    return token


def payment(billing_id):
    payment_date = date.today()
    value = (payment_date, billing_id)
    token = Payment.pay(value=value)
    return token


def new_bill(new_billing_details):
    token = NewBill.create(value=new_billing_details)
    return token


#  BELOW ALL IS THE TESTING, CAN BE REFERENCES, CAN BE REMOVED
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


@app.route('/login', methods=['POST'])
def login_to_page():
    data = request.get_json()
    username = data['username']
    password = data['password']
    token = login(username, password)
    msg_dict = {
        "success": token[0],
        "message": token[1]
    }
    return jsonify(msg_dict)


@app.route('/url1')
def test1():
    # data = filter_property_for_sale({'property_type': 'Any', 'furnish': 'Any', 'tenure_type': 'Any', 'min_sell_price': 'Any', 'max_sell_price': 'Any', 'bedroom': 2, 'bathroom': 'Any', 'parking': 'Any', 'min_size': 1024, 'max_size': 1024})
    uid = common.get_uuid()
    user_details = (uid, 'WEE', 'wjs', '123', 'abc@email.com', '456', 'user', 'CIMB', '1111', '981118', None)
    value = ('3291aa4b-f87d-426a-bc52-955cfd5a9389', 6)
    new_property_details = ('2626190D-5046-4C77-8D10-0E4F8773F42C',	410000, 'Serviced Apartment', 2016, 'Freehold', 1, 2, 0, 2, 893, None, 'B-3A-20', 'Pacific Place', 'Jalan 1a/4a', 'Petaling Jaya', 'Selangor', '47301', 'Ara Damansara', 'link to the contract', 1, None, 0, 0, 'D678D762-C8C8-4EBC-90E4-655896E8949A', None, None, None, 'BOTH', 0, None, '2020-06-04', '2021-06-03', 1, 'Free Utilities', date.today(), None,	None)
    data = purchase_property(new_property_details, '2626190D-5046-4C77-8D10-0E4F8773F42C', '0B31D4C2-9A19-4F16-BABE-BD37C1F06BB3')
    msg_dict = {
        "success": data
    }
    return jsonify(msg_dict)


@app.route('/url2')
def test2():

    # data = filter_property_for_rent({'property_type': 'Any', 'furnish': 'Any', 'move_in_date': 'Any', 'min_sell_price': 'Any', 'max_sell_price': 'Any', 'bedroom': 4, 'bathroom': 'Any', 'parking': 'Any', 'min_size': 'Any', 'max_size': 'Any'})
    billing_details = ('01-July-2020', 'Rental', 2500, None, 1, 2)  # Property_id is the last value
    value = ('Approve', 1)  # Request_id is the last value
    request_details = ('15-July-2020', 'Pending', 'Rent', '01-July-2020', 1, '7ee30661-80ad-4862-966b-7279d0f80d22', 4)
    today = date.today()
    new_property_details = ('Fully', 3000.00, None, 'RENT', 0, None, None, None, None, 'House For Rent', today, None, None, 6)
    data = update_property_details(new_property_details=new_property_details)
    msg_dict = {
        "message": data
    }
    return jsonify(msg_dict)


@app.route('/url3')
def test3():
    # data = filter_property_for_sale({'property_type': 'Any', 'furnish': 'Any', 'tenure_type': 'Any', 'min_sell_price': 'Any', 'max_sell_price': 'Any', 'bedroom': 2, 'bathroom': 'Any', 'parking': 'Any', 'min_size': 1024, 'max_size': 1024})
    uid = common.get_uuid()
    path = "data.csv"
    data = upload_property(path)
    msg_dict = {
        "message": data
    }
    return jsonify(msg_dict)


@app.route('/api/login', methods=['POST'])
def login_user_api():
    data = request.get_json()
    message = login(data['username'], data['password'])
    login_dict = {
        "success": message[0],
        "message": message[1]
    }
    return jsonify(login_dict)


if __name__ == '__main__':
    app.run(debug=True)
