# ユーザー認証（登録・ログイン・ログアウト）関連のコントローラー（関数形式）
from flask import render_template, request, redirect, url_for, session, flash
from app.models.user import register_user, authenticate_user

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

def logout():
    session.pop('user_id', None)
    flash('ログアウトしました')
    return redirect(url_for('auth.login')
)
