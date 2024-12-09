from pydoc import doc
from flask import Flask, request,render_template,jsonify
app = Flask(__name__)
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
# Replace 'your_connection_string' with your actual MongoDB connection string
# Create a new client and connect to the server

load_dotenv()

uri = os.getenv('uri')
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    print("Couldn't connect to MongoDB")

db=client.bbijaykumar76

@app.route('/submit-signup', methods=['POST'])
def submit_signup():
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')
    data={'name':name, 'email':email, 'password':password}
    # insert data into MongoDB
    db.signupdata.insert_one(data)

    return 'Data submitted successfully!'

@app.route('/view')
def view_data():
    data=db.signupdata.find()
    dat=list(data)
    print(data) #<pymongo.synchronous.cursor.Cursor object at 0x0000016CEAB3DDF0>
    for data in dat:
        print(data) 
        del data['_id']
    # print data in a readable format
    data={
        'data': dat,
    }
    # print(
    #     'Data:', '\n'.join(
    #         f'Name: {doc["name"]}, Email: {doc["email"]}, Password: {doc["password"]}'
    #         for doc in data
    #     )
    # )
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True) # debug logging is enabled because it allows to restart the app without restarting the weserver
    #app.run(host='0.0.0.0', port=8080) # For deploying on a server
    #app.run(port=8080) # For running locally with default IP and port
    #app.run(host='127.0.0.1', port=8080) # For running locally with specific IP and port