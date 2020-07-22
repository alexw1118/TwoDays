from flask import json, jsonify, app, Flask, render_template
from model import User, BaseProperty
from service import ViewProperty


app = Flask(__name__)


@app.route('/')
def default():
    return render_template('Index.html')


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
