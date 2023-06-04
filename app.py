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

@app.route("/", methods=['post', 'get'])
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
        user_found = records.find_one({"name": user})
        email_found = records.find_one({"email": email})
        
        if user_found:
            message = 'There already is a user by that name'
            return render_template('index.html', message=message)
        if email_found:
            message = 'This email already exists in database'
            return render_template('index.html', message=message)
        if password1 != password2:
            message = 'Passwords should match!'
        else:
            #hash the password and encode it
            hashed = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
            #assing them in a dictionary in key value pairs
            user_input = {'name': user, 'email': email, 'password': hashed}
            #insert it in the record collection
            records.insert_one(user_input)

            #find the new created account and its email
            user_data = records.find_one({"email": email})
            new_email = user_data['email']
            #if registered redirect to logged in as the registered user
            return render_template('logged_in.html', email=new_email)
         # Check if any of the variables is None
 
    return render_template('index.html')
    
def login():
    message = 'Please login to your account'
    if "email" in session:
        return redirect(url_for({}))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        #check if email exists in database
        email_found = records.find_one({"email": email})
        if email_found:
            email_val = email_found['email']
            passwordcheck = email_found['password']
            #encode the password and check if it matches
            if bcrypt.checkpw(password.encode('utf-8'), passwordcheck):
                session["email"] = email_val
                return redirect(url_for('client-side'))
            else:
                if "email" in session:
                    return redirect(url_for("client-side"))
                message = 'Wrong password'
                return render_template('client-side.html', message=message)
        else:
            message = 'Email not found'
            return render_template('client-side.html', message=message)
    return render_template('client-side.html', message=message)

def logged_in():
    if "email" in session:
        email = session["email"]
        return render_template('client-side.html', email=email)
    else:
        return redirect(url_for("client-side"))


def logout():
    session.pop("email", None)
    return render_template("signout.html")






if __name__=="__main__":
    app.run(debug=True)