from flask import Blueprint, render_template


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return '<h1>Main Page</h1>'


@main.route('/profile')
def profile():
    return '<h1>Profile Page</h1>'
