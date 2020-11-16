from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/api')
def super_simple():
    return jsonify(message='Hello from the FramesandPackets API'), 200

@app.route('/not_found')
def not_found():
   return jsonify(message='Data requested not found :('), 404

if __name__ == '__main__':
    app.run()
