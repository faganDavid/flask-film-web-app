from flask import Blueprint, render_template, redirect, url_for, request
from .models import db, Movie
from .forms import MovieForm


views = Blueprint("views", __name__)


@views.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html", movies=all_movies)


@views.route("/edit/<int:id>", methods=["GET", "POST"])
def update(id):
    movie = Movie.query.get(id)
    form = MovieForm()
    form.title.data = movie.title
    form.year.data = movie.year
    form.description.data = movie.description
    form.rating.data = movie.rating
    form.ranking.data = movie.ranking
    form.review.data = movie.review
    form.img_url.data = movie.img_url
    if form.validate_on_submit():
        movie.title = request.form['title']
        movie.year = request.form['year']
        movie.description = request.form['description']
        movie.rating = request.form['rating']
        movie.ranking = request.form['ranking']
        movie.review = request.form['review']
        movie.img_url = request.form['img_url']
        db.session.commit()
        return redirect(url_for('views.home'))
    return render_template("edit.html", movie=movie, form=form)
