from flask import json, jsonify, app


@app.route('/url_path')
def name():
    data = "method()"
    return jsonify(data)


@app.route('/url_path')
def summary():
    data = "method()"
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

