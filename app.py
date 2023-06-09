from flask import Flask, render_template, request, url_for, redirect, session, jsonify
from pymongo.mongo_client import MongoClient
import bcrypt
import certifi
#set app as a Flask instance 
app = Flask(__name__)
#encryption relies on secret keys so they could be run
app.secret_key = "canteen123"
#connoct to your Mongo DB database
uri = "mongodb+srv://admin:admin@cluster0.epqxvmj.mongodb.net/"
# cart_uri="mongodb+srv://admin:admin@cluster0.epqxvmj.mongodb.net/cart"

# Create a new client and connect to the server
# client = MongoClient(uri)
client = MongoClient(uri,tlsCAFile=certifi.where())
db = client.get_database('total_records')
records = db["records"]
# cartclient=MongoClient(cart_uri)
# db = cartclient.get_database('cart')
# collection = db["cart_details"]

# @app.route("/add_to_cart", methods=['POST'])
# def add_to_cart():
#     cart_item = request.get_json()
#     collection.insert_one(cart_item)
#     print(cart_item)
#     return jsonify({'message': 'Item added to cart'})



# MongoDB connection
cart_uri = "mongodb+srv://admin:admin@cluster0.epqxvmj.mongodb.net"
cart_client = MongoClient(cart_uri,tlsCAFile=certifi.where())
# cart_client = MongoClient(cart_uri)
db = cart_client.get_database('cart')
collection = db["cart_details"]

@app.route("/add_to_cart", methods=['POST'])
def add_to_cart():
    try:
        cart_item = request.get_json()
        collection.insert_one(cart_item)
        print(cart_item)
        return jsonify({'message': 'Item added to cart'})
    except Exception as e:
        print("Error adding item to cart:", str(e))
        return jsonify({'error': 'Failed to add item to cart'})



@app.route('/client-side.html')
def client_side():
    return render_template('client-side.html')
# def logout():
#      session.pop("email", None)
#      return render_template("index.html")

@app.route("/", methods=['POST', 'GET'])



def index():
    message = ''
    #if method post in index
    # if method post in index
  

   

    # Rest of your code...

    if request.method == "POST":
        user = request.form.get("fullname")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        #if found in database showcase that it's found 
        email_found = records.find_one({"email": email})
        
        if email_found != None:
            message = 'This email already exists in database'
            return render_template('index.html', message=message)
        if password1 != password2:
            message = 'Passwords should match!'
        else:
            #hash the password and encode it
            #assing them in a dictionary in key value pairs
            user_input = {'name': user, 'email': email, 'password': password1}
            #insert it in the record collection
            records.insert_one(user_input)

            #find the new created account and its email
            user_data = records.find_one({"email": email})
            new_email = user_data['email']
            #if registered redirect to logged in as the registered user
            return render_template('index.html', email=new_email)
         # Check if any of the variables is None
 
    return render_template('index.html')
def logout():
    session.pop("email", None)
    return render_template("index.html")
    
# def login():
#     message = 'Please login to your account'
#     if "email" in session:
#         return redirect(url_for('client_side'))

#     if request.method == "POST":
#         print(request.form)
#         email = request.form.get("email")
#         password = request.form.get("password")
#         print(email)
#         print(password)

#         #check if email exists in database
#         email_found = records.find_one({"email": email})
#         if email_found:
#             email_val = email_found['email']
#             passwordcheck = email_found['password']
#             #encode the password and check if it matches
#             if bcrypt.checkpw(password.encode('utf-8'), passwordcheck):
#                 session["email"] = email_val
#                 return redirect(url_for('client_side'))
#             else:
#                 if "email" in session:
#                     return redirect(url_for("client_side"))
#                 message = 'Wrong password'
#                 return render_template('index.html', message=message)
#         else:
#             message = 'Email not found'
#             return render_template('index.html', message=message)
#     return render_template('client-side.html', message=message)


# def logged_in():
#     if "email" in session:
#         email = session["email"]
#         return render_template('client-side.html', email=email)
#     else:
#         return redirect(url_for("client_side"))


@app.route("/client-side.html", methods=['POST','GET'])
def login():
    message = 'Please login to your account'
    # if "email" in session:
    #     return render_template('client-side.html')

    if request.method == "POST":
        print(request.form)
        email = request.form.get("email")
        password = request.form.get("password")
        print(email)
        print(password)

        #check if email exists in database
        email_found = records.find_one({"email": email})
        print("email found", email_found)
        
        if email_found:
            email_val = email_found['email']
            print(email_val)
            if(email_val=='admin@gmail.com'):
                passwordcheck = email_found['password']
                print(passwordcheck)
                #encode the password and check if it matches
                if password==passwordcheck:
                    session["email"] = email_val
                    print("Validation Successful")
                    return render_template('admin-side.html')
                else:
                    if "email" in session:
                        return render_template('admin-side.html')
                    message = 'Wrong password'
                    print(message)
                    return render_template('index.html', message=message)
                    
            else:
                passwordcheck = email_found['password']
                print(passwordcheck)
            #encode the password and check if it matches
                if password==passwordcheck:
                    session["email"] = email_val
                    print("Validation Successful")
                    return render_template('client-side.html')
                else:
                    if "email" in session:
                        return render_template('client-side.html')
                    message = 'Wrong password'
                    print(message)
                    return render_template('index.html', message=message)
        else:
            message = 'Email not found'
            return render_template('index.html', message=message)
    return render_template('index.html', message=message)


# def logout():
#     session.pop("email", None).
#     return render_template("index.html")
@app.route('/logout')
def logout():
    return render_template('index.html')


@app.route('/index.html')
def home():
    return render_template('index.html')
def logout():
    return render_template('index.html')

@app.route('/our-vision.html')
def our_vision():
    return render_template('our-vision.html')

@app.route('/admin-side.html')
def admin():
    return render_template('admin-side.html')

if __name__=="__main__":
    app.run(debug=True)