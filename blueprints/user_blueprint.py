from flask import Blueprint
from flask import request
from flask import render_template


user_blueprint = Blueprint( 'user_blueprint',__name__,)


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        ...


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        ...
