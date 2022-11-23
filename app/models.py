from flask_sqlalchemy import SQLAlchemy


# globally accessible database library
db = SQLAlchemy()


class Movie(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(250))
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer(), nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"<Movie {self.title}"