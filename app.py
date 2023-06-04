from flask import Flask, render_template, request, url_for, redirect, session
import pymongo
import bcrypt
#set app as a Flask instance 
app = Flask(__name__)
#encryption relies on secret keys so they could be run
# app.secret_key = ""
#connoct to your Mongo DB database
client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.epqxvmj.mongodb.net/?retryWrites=true&w=majority")

#get the database name
db = client.get_database('total_records')
#get the particular collection that contains the data
records = db.register

@app.route('/')
def index():
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)