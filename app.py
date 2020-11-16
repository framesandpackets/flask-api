from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/api')
def super_simple():
    return jsonify(message='Hello from the FramesandPackets API'), 200


@app.route('/not_found')
def not_found():
   return jsonify(message='Data requested not found :('), 404


@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message="Sorry " + name + ", you are not old enough."), 401
    else:
        return jsonify(message="Hello!, " + name + "! you are old enough. "), 200



if __name__ == '__main__':
   app.run()
