from flask import Blueprint, render_template, redirect, url_for, request

comments_blueprint = Blueprint('comments_handler', __name__)
@comments_blueprint.route('/')
def index():
    return render_template('index.html')
