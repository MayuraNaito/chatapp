# 認証関連のルーティング
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models.user import register_user, authenticate_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if register_user(username, password):
            flash('登録が完了しました。ログインしてください。')
            return redirect(url_for('auth.login'))
        else:
            flash('そのユーザー名は既に使われています。')
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if authenticate_user(username, password):
            session['user_id'] = username
            flash('ログインしました')
            return redirect(url_for('room.index'))
        else:
            flash('ユーザー名またはパスワードが違います')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('ログアウトしました')
    return redirect(url_for('auth.login'))
