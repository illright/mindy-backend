# https://scotch.io/tutorials/authentication-and-authorization-with-flask-login
from flask import Blueprint, url_for, render_template, request, flash, jsonify
from .models import db
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Account
from flask_login import login_user, logout_user, login_required
from flask_cors import CORS
from flask import redirect

auth = Blueprint('auth', __name__)
CORS(auth, supports_credentials=True)
'''
@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/signup')
def signup():
    return render_template('signup.html')
'''

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['POST'])
def signup_post():
    json = request.get_json(force=True)
    mail = json['email']
    name = json['name']
    password = json['password']
    is_teacher = json['is_teacher']
    user = Account.query.filter_by(
        email=mail).first()  # if this returns a user, then the email already exists in database

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        # return redirect(url_for('auth.signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = Account(email=mail, name=name, password=generate_password_hash(password, method='sha256'),
                       is_teacher=is_teacher)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        'id': new_user.id,
        'email': new_user.email,
        'name': new_user.name,
        'is_teacher': new_user.is_teacher,
    })


@auth.route('/login', methods=['POST'])
def login_post():
    json = request.get_json(force=True)
    email = json['email']
    password = json['password']
    remember = True #if request.form.get('remember') else False

    user = Account.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        # if user doesn't exist or password is wrong, reload the page
        #return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    # if the above check passes, then we know the user has the right credentials
    return jsonify({
        'id': user.id,
        'email': user.email,
        'name': user.name,
        'is_teacher': user.is_teacher,
    })