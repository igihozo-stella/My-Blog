from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import Required
from ..models import User

class UpdateForm(FlaskForm):
    title=StringField('Title', validators=[Required()])
    category=SelectField('Category',choices=[('News','News'),('Job','Job'),('Relationships','Relationships')], validators=[Required()])
    post=TextAreaField('Your Post', validators=[Required()])
    submit=SubmitField('Save')

class PostForm(FlaskForm):
    title=StringField('Title', validators=[Required()])
    category=SelectField('Category',choices=[('News','News'),('Job','Job'),('Relationships','Relationships')], validators=[Required()])
    post=TextAreaField('Your Post', validators=[Required()])
    submit=SubmitField('Post')

class CommentForm(FlaskForm):
    comment=TextAreaField('Leave your comment here',validators=[Required()])
    submit=SubmitField('Comment')