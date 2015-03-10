from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required

from sclab_sites import app, login_manager
from onco_forms import OncoLoginForm, OncoEntryForm
from onco_models import User


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


@app.route("/logout")
@login_required
def onco_logout():
    logout_user()
    return redirect(url_for('onco_login'))


@app.route('/entry', methods=['GET', 'POST'])
@login_required
@login_manager.needs_refresh_handler
def onco_entry():
    form = OncoEntryForm()
    if form.validate_on_submit():
        return render_template('onco_success_entry.html')
    return render_template('onco_entry.html', form=form)


@app.route('/oncotyping', methods=['GET', 'POST'])
def onco_login():
    form = OncoLoginForm()
    if form.validate_on_submit():
        requested_user = User.query.filter_by(username=form.username.data).first()
        if requested_user is None:
            form.username.errors.append("Username doesn't exist")
        elif form.password.data != requested_user.password:
            form.password.errors.append("Password is incorrect")
        else:
            flash('Welcome %s. You have successfully logged in' % requested_user.username)
            login_user(requested_user)
            return redirect(url_for('onco_entry'))
    return render_template('onco_login.html', title='Sign In', form=form)

login_manager.login_view = 'onco_login'
