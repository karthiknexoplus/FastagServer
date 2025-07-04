from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FieldList, FormField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 120)])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 128)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LocationForm(FlaskForm):
    site_name = StringField('Site Name', validators=[DataRequired(), Length(1, 128)])
    contact_details = StringField('Contact Details', validators=[DataRequired(), Length(1, 128)])
    site_address = StringField('Site Address', validators=[DataRequired(), Length(1, 256)])
    submit = SubmitField('Save')

class ReaderForm(FlaskForm):
    reader_ip = StringField('Reader IP', validators=[DataRequired(), Length(1, 64)])
    reader_type = SelectField('Reader Type', choices=[('entry', 'Entry'), ('exit', 'Exit')], validators=[DataRequired()])

class LaneForm(FlaskForm):
    lane_name = StringField('Lane Name', validators=[DataRequired(), Length(1, 128)])
    lane_type = SelectField('Lane Type', choices=[('entry', 'Entry'), ('exit', 'Exit')], validators=[DataRequired()])
    controller_ip = StringField('Controller IP', validators=[DataRequired(), Length(1, 64)])
    location_id = SelectField('Location', coerce=int, validators=[DataRequired()])
    readers = FieldList(FormField(ReaderForm), min_entries=1, max_entries=4)
    submit = SubmitField('Save') 