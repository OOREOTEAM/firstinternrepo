from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Photo, Hunter
from . import db
from passlib.hash import sha256_crypt
import os

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = bool(request.form.get('remember'))

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flash('Невірні дані для входу. Спробуйте ще раз.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username')
    password = request.form.get('password')

    if User.query.filter_by(username=username).first():
        flash('Користувач з таким іменем вже існує')
        return redirect(url_for('auth.signup'))

    new_user = User(
        username=username,
        password=generate_password_hash(password)
    )

    db.session.add(new_user)
    db.session.commit()

    flash('Реєстрація успішна! Тепер можете увійти.')
    return redirect(url_for('auth.login'))

@auth.route('/success', methods=['POST'])
@login_required
def success():
    if 'file' not in request.files:
        flash('Файл не знайдено')
        return render_template('profile.html', name=current_user.username)


    f = request.files['file']
    if f.filename == '':
        flash('Ви не обрали файл')
        return render_template('profile.html', name=current_user.username)

    filename = secure_filename(f.filename)

    upload_path = os.path.join(current_app.root_path, 'static', filename)
    f.save(upload_path)

    caption_text = request.form.get('caption', '')

    new_photo = Photo(filename=filename, caption=caption_text, user_id=current_user.id)
    db.session.add(new_photo)
    db.session.commit()

    current_user.profile_image = filename
    db.session.commit()

    flash('Файл успішно завантажено!')
    return redirect(url_for('main.profile'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/report_page')
def report_page():
    return render_template('report-page.html')


@auth.route('/report_page', methods=['POST'])
def report_page_post():
    ip = request.form.get('ip')
    ip_hash =sha256_crypt.hash(ip)
    hunters_ip_hash = Hunter(ip_hash=ip_hash)
    db.session.add(hunters_ip_hash)
    db.session.commit()
    return redirect(url_for('main.index'))

