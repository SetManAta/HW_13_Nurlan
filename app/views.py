from flask import render_template, request, redirect, url_for,flash
from .models import Transactions, User
from app import db
from .forms import TransactionsForm, UserForm
from flask_login import login_user, logout_user, login_required

def trans_view():
    trans = Transactions.query.all()
    return render_template('transactions_list.html', trans=trans)

def transactions_create():
    form = TransactionsForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            trans = Transactions()
            form.populate_obj(trans)
            db.session.add(trans)
            db.session.commit()
            flash('Студент сохранен')
            return redirect(url_for('transactions_list'))
    return render_template('transaction_form.html', form=form)


def transactions_detail(id):
    trans = Transactions.query.get(id)
    return render_template('transaction_detail.html', trans=trans)


def transactions_update(id):
    trans = Transactions.query.get(id)
    form = TransactionsForm(request.form, obj=trans)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(trans)
            db.session.add(trans)
            db.session.commit()
            return redirect(url_for('transactions_list'))
    return render_template('transaction_form.html', form=form)


def transactions_delete(id):
    trans = Transactions.query.get(id)
    if request.method == 'POST':
        db.session.delete(trans)
        db.session.commit()
        return redirect(url_for('transactions_list'))
    return render_template('transaction_delete.html', trans=trans)
###########################################################################################
def register_view():
    form = UserForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User()
            form.populate_obj(user)
            db.session.add(user)
            db.session.commit()
            flash(f'Ползователь {user.username} save!','success')
            return redirect(url_for('login'))
    return render_template('user_form.html', form=form)

def login_view():
    logout_user()
    form = UserForm()
    if request.method == "POST":
        if form.validate_on_submit():
            # user = User()
            # form.populate_obj(user)
            user = User.query.filter_by(username=request.form.get('username')).first()
            if user and user.check_password(request.form.get('password')):
                login_user(user)
                flash('Успешно авторизован!', 'primary')
                return redirect(url_for('transactions_list'))
            else:
                flash('не правильно введен логин или пароль','danger')
    return render_template('user_form.html', form=form)

def logout_view():
    logout_user()
    return redirect(url_for('login'))