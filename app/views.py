from flask import Blueprint, render_template, redirect, url_for, request
from .models import db, Movie
from .forms import MovieForm, FindMovieForm
from .api import search_movie_data, get_movie_data
from config import TMDB_IMAGE_URL


views = Blueprint("views", __name__)


@views.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@views.route("/edit", methods=["GET", "POST"])
def update():
    form = MovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)

    if form.validate_on_submit():
        movie.rating = request.form["rating"]
        movie.review = request.form["review"]
        db.session.commit()

        return redirect(url_for("views.home"))

    return render_template("edit.html", movie=movie, form=form)


@views.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for("views.home"))


@views.route("/add", methods=["GET", "POST"])
def add():
    form = FindMovieForm()

    if form.validate_on_submit():
        movie_to_add = request.form["title"]
        movie_data = search_movie_data(movie_to_add)
        return render_template("select.html", options=movie_data)

    return render_template("add.html", form=form)


@views.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")

    if movie_api_id:
        movie_data = get_movie_data(movie_api_id)
        new_movie = Movie(
            title=movie_data["title"],
            year=movie_data["release_date"].split("-")[0],
            description=movie_data["overview"],
            img_url=f"{TMDB_IMAGE_URL}{movie_data['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("views.home"))
