from flask import render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from app import create_app


app = create_app()
Bootstrap(app)


if __name__ == '__main__':
    app.run(debug=True)
