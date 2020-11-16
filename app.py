from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/api')
def super_simple():
    return jsonify(message='Hello from the FramesandPackets API')

if __name__ == '__main__':
    app.run()
