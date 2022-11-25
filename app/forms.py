from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired


class MovieForm(FlaskForm):
    rating = FloatField("Rating")
    review = StringField("Review")
    submit = SubmitField("Submit")


class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")