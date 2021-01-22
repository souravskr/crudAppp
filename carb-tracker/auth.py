from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/signup')
def signup():
    return '<h1>Sign up Page</h1>'


@auth.route('/login')
def login():
    return '<h1>Login Page</h1>'


@auth.route('/signout')
def signout():
    return '<h1>signout Page</h1>'
