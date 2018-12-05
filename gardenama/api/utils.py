from flask import jsonify

def make_api_response(status_code, json_data):
    resp = jsonify(json_data)
    resp.status_code = status_code
    return resp