from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class NameInput(FlaskForm):
    """Contact form."""
    firstname1 = StringField(
        'First name',
        [DataRequired()]
    )
    lastname1 = StringField(
        'Last name',
        [DataRequired()]
    )
    firstname2 = StringField(
        'First name',
        [DataRequired()]
    )
    lastname2 = StringField(
        'Last name',
        [DataRequired()]
    )
    submit = SubmitField('Submit')