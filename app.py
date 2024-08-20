from flask import Flask, jsonify, request
import json
import mysql.connector


app = Flask(__name__)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abcd1234",
    database="flaskapptable"
)


#### Python MySQL Create Table ####
cursor = mydb.cursor()
createatable = '''
Create Table If Not Exists Flask_App_Table (
    Username VARCHAR(20),
    Password VARCHAR(20),
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Email_Address VARCHAR(50),
    First_Name VARCHAR(20),
    Last_Name VARCHAR(20),
    Age INT,
    House_Address VARCHAR(100),
    State VARCHAR(20),
    City VARCHAR(20),
    Zip_Code VARCHAR(10),
    Country VARCHAR(50)
)
'''
cursor.execute(createatable)
mydb.commit()
mydb.close()


#### Python MySQL Insert Into Table ####
def insert():
    data = request.json
    mydb = mysql.connector.connect()
    cursor = mydb.cursor()

    tableinsert = '''
    Table Insert Flask_App_Table (Username, Password, Email_Address, First_Name, Last_Name, Age, House_Address, State, City, Zip_Code, Country)
    inserttable (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    inserttable = (
        data.get('Username'),
        data.get('Password'),
        data.get('Email Address'),
        data.get('First Name'),
        data.get('Last Name'),
        data.get('Age'),
        data.get('House Address'),
        data.get('State'),
        data.get('City'),
        data.get('Zip Code'),
        data.get('Country')
    )
    cursor.execute(tableinsert, inserttable)
    mydb.commit()
    cursor.close()
    mydb.close()


@app.route("/")
def entry():
    #create the table
    return "<p>Welcome to Flask App</p>"


@app.route("/home")
def home():
    data = {
        'Username': 'anishpatel',
        'Password': 'anishpatel1000',
        'ID': 1,
        'Email Address': 'anishpatel@atlanta.com',
        'First Name': 'Anish',
        'Last Name': 'Patel',
        'Age': 24,
        'House Address': '1234 Welcome to Flask App St',
        'State': 'GA',
        'City': 'Atlanta',
        'Zip Code': '12345',
        'Country': 'United States of America'
    }
    with open('output.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    return jsonify(data)