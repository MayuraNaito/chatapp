# routes/room_routes.py
# チャットルーム関連のルーティング（URLとコントローラーの対応）をまとめたファイル。
# Blueprintでルート定義し、コントローラー関数を呼び出す。

from flask import Blueprint
from app.controllers import roomController

room_bp = Blueprint('room', __name__)

# ユーザー識別用のセッションIDをセット
room_bp.before_app_request(roomController.set_user)

# トップページ（ユーザー名設定またはログイン選択）
room_bp.route('/', methods=['GET', 'POST'])(roomController.index)

# 部屋一覧・作成・名前設定
# room_bp.route('/rooms', methods=['GET', 'POST'])(roomController.login)

# 部屋削除（オーナーのみ許可）
room_bp.route('/delete_room/<room_name>', methods=['POST'])(roomController.delete_room_route)

# 部屋ごとのチャットページ表示
room_bp.route('/room/<room_name>')(roomController.room)
