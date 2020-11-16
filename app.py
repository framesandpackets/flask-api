from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/api/<string:name>/<int:age>')
def api(name: str, age: int):
    if age < 18:
        return jsonify(message="Sorry " + name + ", you are not old enough."), 401
    else:
        return jsonify(message="Hello!, " + name + "! you are old enough. "), 200
    

@app.route('/not_found')
def not_found():
   return jsonify(message='Data requested not found :('), 404


if __name__ == '__main__':
   app.run()
