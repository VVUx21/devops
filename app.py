from flask import Flask, request,render_template
from datetime import datetime
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

@app.route('/')
def home():
    today = datetime.now().strftime('%A, %d %B %Y') # for other date formats
    current_time = datetime.now().strftime(
        '%I:%M %p' # 12-hour format
        '%H:%M' # 24-hour format
        '%d-%m-%Y' # day-month-year format
        '%B %d, %Y' # full month name, day, year format
        '%A, %d %B %Y' # full weekday, day, month, year format
        '%A, %B %d, %Y %I:%M %p' # full weekday, month, day, year, 12-hour format
        '%A, %B %d, %Y %H:%M' # full weekday, month, day, year, 24-hour format
        '%a, %d %b %Y %I:%M %p' # abbreviated weekday, day, month, year, 12-hour format
    )
    return  render_template('index.html', today=today, datetime=current_time)

@app.route('/greet/<name>') # always returns the string...for any other purpose we have to typecast it to othe datatype...
def greet(name):
    return f'Hello, {name}!'

@app.route('/add/<int:a>/<int:b>') # typecasting to int for addition
def add(a, b):
    return str(a + b)

@app.route('/subtract') #how u get values from the request or query params
def subtract():
    a=request.values.get('a')
    b=request.values.get('b')
    
    return {
        'result': a,
        'difference': b
    }

@app.route('/submit-signup', methods=['POST'])
def submit_signup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    data={'name':name, 'email':email, 'password':password}
    # insert data into MongoDB
    db.signupdata.insert_one(data)

    return 'Data submitted successfully!'

@app.route('/view')
def view_data():
    data=db.signupdata.find()
    print(data) #<pymongo.synchronous.cursor.Cursor object at 0x0000016CEAB3DDF0>
    print(
        'Data:', '\n'.join(
            f'Name: {doc["name"]}, Email: {doc["email"]}, Password: {doc["password"]}'
            for doc in data
        )
    )
    # print data in a readable format
    # for doc in data:
    # print(f'Name: {doc["name"]}, Email: {doc["email"]}, Password: {doc["password"]}')
    # return 'Data fetched successfully!'
    return str(data) # print data as string

if __name__ == '__main__':
    app.run(debug=True) # debug logging is enabled because it allows to restart the app without restarting the weserver
    #app.run(host='0.0.0.0', port=8080) # For deploying on a server
    #app.run(port=8080) # For running locally with default IP and port
    #app.run(host='127.0.0.1', port=8080) # For running locally with specific IP and port