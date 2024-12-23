from flask import Flask, jsonify
from business import getdata
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/api')
def about():
    data = getdata()
    data={
        'data': data
    }
    return jsonify(data)

if __name__ == '__main__':
    # app.run(debug=True) # debug mode enabled for development purpose. It shows error messages in console. In production, it should be disabled.
    app.run(host='0.0.0.0', port=8080, debug=True) # For deploying on a server. The IP address can be any public IP address.
