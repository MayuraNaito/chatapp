# Flaskアプリ・SocketIOの初期化、Blueprint登録、環境変数の読み込み
from flask import Flask
from app.controllers.room_controller import room_bp
from app.controllers.auth_controller import auth_bp
from dotenv import load_dotenv
import os
from .extensions import socketio

# .envファイルから環境変数を読み込む
load_dotenv()

# Flaskアプリのセットアップ
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret!')

# SocketIOをFlaskアプリに紐付け
socketio.init_app(app)

# ルーム関連のBlueprintを登録
app.register_blueprint(room_bp)
app.register_blueprint(auth_bp)
