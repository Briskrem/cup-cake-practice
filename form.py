from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired



class AddCupcake(FlaskForm):

    flavor = StringField('flavor', validators=[InputRequired()])
    size = StringField('size')
    rating = FloatField('rating')
    image = StringField('image')