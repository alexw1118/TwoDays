from flask import json, jsonify, app, Flask, render_template
import uuid
from model import User


app = Flask(__name__)


@app.route('/')
def default():
    uid = test()
    return render_template('Index.html', uuid=uid)


@app.route('/url_path')
def name():
    records = [[1,2,3,4,5,6,7,8,9,0,11],[1,2,3,4,5,6,7,8,9,0,11],[1,2,3,4,5,6,7,8,9,0,11]]
    list = []
    for record in records:
        user = User.User(record)
        do = vars(user)
        list.append(do)

    objdict = {
        "username": user.username,
        "bank_account": user.bank_account,
        "privilege": user.privilege
    }
    data = [1,2,3,4,5,6,7]
    property_id = uuid.uuid4()
    print(property_id)
    return jsonify(list)


@app.route('/url_path2')
def summary():
    data = "method()"
    user = User.User([1,2,3,4,5,6,7,8,9,0,11]).__dict__
    do = dict(user)
    response = app.response_class(
        response=json.dumps(do),
        status=200,
        mimetype='application/json'
    )
    return response


def test():
    property_id = uuid.uuid4()
    return property_id


if __name__ == '__main__':
    app.run(debug=True)
