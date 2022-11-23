from flask import Blueprint, render_template
from .models import db, Movie


views = Blueprint("views", __name__)


@views.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html", movies=all_movies)
