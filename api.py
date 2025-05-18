from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def sum_api():
    return jsonify({"sum": 10})

if __name__ == '__main__':
    app.run()
