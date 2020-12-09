from . import auth
from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,login_required,logout_user
from .forms import RegistrationForm,LoginForm
from ..models import User
from .. import db
from ..email import mail_message



@auth.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next')or url_for('main.index'))
        flash('invalid username or password')
    return render_template('auth/login.html',login_form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        user=User(email=form.email.data, username=form.username.data,password=form.password.data)
        user.save_u()
        # mail_message("Welcome to this Blog","email/welcome_user",user.email,user=user)
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',registration_form=form)