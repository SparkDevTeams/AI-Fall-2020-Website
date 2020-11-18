from flask_wtf import FlaskForm
from wtforms import StringField

class rowForm(FlaskForm):
    field1 = StringField("rowNumber")