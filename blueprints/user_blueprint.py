from flask import Blueprint
import requests
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from flask import abort

from helpers import hash_password,check_password

# from helpers import check_password
from helpers import login_required
# from helpers import get_review_counts

from db import db


user_blueprint = Blueprint("user_blueprint", __name__)


@user_blueprint.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("confirmpassword")

        print(password)
        print(password2)

        missing_fields = []
        if name is None:
            missing_fields.append("Name")
        if username is None:
            missing_fields.append("Username")
        if password is None:
            missing_fields.append("Password")
        if password2 is None:
            missing_fields.append("ConfirmPassword")

        error = ""
        if missing_fields:
            error = " ".join(missing_fields) + " are required. "

        if not password == password2:
            error += "Passwords don't match"

        if error:
            return render_template("register.html", error=error)

        # checking if the username already exists in the database
        user = db.execute(
            """
            SELECT *
            FROM users
            WHERE username = :username
            """,
            {"username": username},
        ).first()

        if not user:
            encrypt_password = hash_password(password)
            db.execute(
                """INSERT INTO users (name, username, password)
                VALUES (:name, :username, :password)""",
                {"name": name, "username": username, "password": encrypt_password},
            )
            db.commit()

            message = "User created successfully"
            print(message)
            return redirect(url_for('book_blueprint.search'))
        else:
            error = f"Sorry, Username {username} is taken. Please use another Username"
            return render_template("register.html", error=error)

    # if not post the else will be GET Method
    else:
        return render_template("register.html")


@user_blueprint.route("/login", methods=["GET", "POST"])
def login():
    ...
    """
    if 'user_id' in session:
        user is already logged in
        redirect to dashboard
    if username and password match
        get the user from db
        session['user_id'] = user.id
    else
        bhul login ache, hobe na
    """
    username=request.form.get('username')

    if request.method =='POST':

        missing_val=[]
        password=request.form.get('password')
        if not username:
            missing_val.append('username')
        elif not password:
            missing_val.append("password")

        error=' '
        if missing_val:
            error=(' ').join(missing_val) +" are required"
            return render_template('login.html' , error= error)
        
        userrow= db.execute('''
                            Select password from users where username=:username
                            ''',{"username":username}).fetchone()
    
        if not userrow:
           error=" Sorry {username} doesn't exist. Please register."
           return redirect( url_for('user_blueprint.register'),error= error)

        for row in userrow:
            hash_password=row

        if not check_password(hash_password,password):
            return render_template('login.html', error="Password Doesn't match ")
        else:
            session['username'] = username
            return redirect(url_for('book_blueprint.search'))
    else:
        # session['username']=username
        # return redirect( url_for('user_blueprint.login'))
        return render_template('login.html')


@user_blueprint.route("/logout")
@login_required
def logout():
    if 'username' in session:
        session.clear()
        return redirect(url_for("user_blueprint.login"))
    else:
        abort(404)
