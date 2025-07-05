# ルーム関連のルーティング・SocketIOイベントをまとめたコントローラー
from app.models.room import add_room, get_rooms, get_room_owner, delete_room
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import uuid
from flask_socketio import send, join_room, emit
from app.extensions import socketio

# Blueprintの作成
room_bp = Blueprint('room', __name__)

# ユーザー識別用のセッションIDをセット
@room_bp.before_app_request
def set_user():
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())

# トップページ（部屋一覧・作成）
@room_bp.route('/', methods=['GET', 'POST'])
def index():
    user_id = session.get('user_id')
    username = session.get('username')
    if request.method == 'POST':
        if 'set_name' in request.form:
            username = request.form.get('username')
            if username:
                session['username'] = username
                flash('名前を設定しました')
            return redirect(url_for('room.index'))
        room_name = request.form.get('room_name')
        add_room(room_name, owner_id=user_id)
        return redirect(url_for('room.index'))
    rooms = get_rooms()
    return render_template('index.html', rooms=rooms, user_id=user_id, get_room_owner=get_room_owner, username=username)

# 部屋削除（オーナーのみ）
@room_bp.route('/delete_room/<room_name>', methods=['POST'])
def delete_room_route(room_name):
    user_id = session['user_id']
    if delete_room(room_name, owner_id=user_id):
        return redirect(url_for('room.index'))
    return '削除権限がありません', 403

# 部屋ごとのチャットページ
@room_bp.route('/room/<room_name>')
def room(room_name):
    rooms = get_rooms()
    if room_name not in rooms:
        return redirect(url_for('room.index'))
    return render_template('room.html', room_name=room_name)

# SocketIO: 部屋に参加
@socketio.on('join')
def on_join(room):
    join_room(room)

# SocketIO: 部屋ごとのメッセージ送信
@socketio.on('room_message')
def handle_room_message(data):
    room = data['room']
    msg = data['msg']
    emit('room_message', {'room': room, 'msg': msg}, room=room)
