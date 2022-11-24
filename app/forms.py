from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, URL


class MovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    year = IntegerField("Year Released", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    rating = FloatField("Rating", validators=[DataRequired()])
    ranking = IntegerField("Ranking", validators=[DataRequired()])
    review = StringField("Review", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    submit = SubmitField("Submit")