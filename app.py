from flask import Flask


app = Flask(__name__)


@app.route('/api')
def super_simple():
    return ('Hello from the FramesandPackets API')

if __name__ == '__main__':
    app.run()
