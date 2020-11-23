from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class NameInput(FlaskForm):
    """Contact form."""
    firstname1 = StringField(
        'Person 1: first name',
        [
            DataRequired(),
            length(max=25,
            message='This name is too long.')
        ]
    )
    lastname1 = StringField(
        'Person 1: last name',
        [
            DataRequired(),
            length(max=25,
            message='This name is too long.')
        ]
    )
    firstname2 = StringField(
        'Person 1: first name',
        [
            DataRequired(),
            length(max=25,
            message='This name is too long.')
        ]
    )
    lastname2 = StringField(
        'Person 1: first name',
        [
            DataRequired(),
            length(max=25,
            message='This name is too long.')
        ]
    )
    submit = SubmitField('Submit')