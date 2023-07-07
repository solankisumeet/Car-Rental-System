from flask import Flask
from flask import render_template, redirect
#Step – 1(import necessary library)
from flask import (render_template, request, redirect, session)
from db import rentaldb

db = rentaldb()


app = Flask(__name__, static_url_path='/static')

app.secret_key = 'ItShouldBeAnythingButSecret'     #you can set any secret key but remember it should be secret


@app.route("/")
def hello_world():
    return render_template("index.html", username=""), 200

#Step – 4 (creating route for login)
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        check_exisiting = db.get_user(username)
        if len(check_exisiting) == 0:
            return "<h1>Wrong username or password</h1>"   
        else:
            user = check_exisiting[0]
            if username == user['username'] and password == user['password']:
                
                session['user'] = username
                return render_template('index.html', username=username)

        return "<h1>Wrong username or password</h1>"    #if the username or password does not matches 

    return render_template("login.html")


#Step – 4 (creating route for login)
@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')     
        save_data = {
            "firstname": request.form.get('firstname'),
            "lastname": request.form.get('lastname'),
            "username": username,
            "password": password,
        }
        check_exisiting = db.get_user(username)
        print("check_exisiting", check_exisiting)
        if len(check_exisiting) == 0:
            db.save_user(save_data)
            return redirect('/login')
        else:
            return "<h1>User already exists</h1>" 
    return render_template("signup.html")


#Step -6(creating route for logging out)
@app.route('/logout')
def logout():
    session.pop('user')         
    return redirect('/login')
