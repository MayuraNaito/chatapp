# routes/auth_routes.py
# ユーザー認証関連のルーティング（URLとコントローラーの対応）をまとめたファイル。
# Blueprintでルート定義し、コントローラー関数を呼び出す。

from flask import Blueprint
from app.controllers import authController

auth_bp = Blueprint('auth', __name__)

auth_bp.route('/register', methods=['GET', 'POST'])(authController.register)
auth_bp.route('/login', methods=['GET', 'POST'])(authController.login)
auth_bp.route('/logout')(authController.logout)
