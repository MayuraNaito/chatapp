# app/__init__.py
# 初期化や設定を行う
import os
from flask import Flask
from dotenv import load_dotenv
from app.config import const
from .extensions import db, socketio
from app.routes.room_routes import room_bp
from app.routes.auth_routes import auth_bp

# SQLiteかどうかを判定
def is_sqlite_bool(uri: str)->bool:
    return uri.startswith('sqlite:///')

# Flaskのセットアップ
def create_app():
    # .envファイルから環境変数を読み込む
    load_dotenv()

    # Flaskアプリケーションのインスタンスを作成
    app = Flask(
        __name__,
        instance_path = os.path.join(os.path.dirname(__file__), 'instance'),
        instance_relative_config = True,
    )

    # Flaskの設定
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret')

    # SQLAlchemyの設定
    default_sqlite_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'instance', 'chat.db'))
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', f'sqlite:///{default_sqlite_path}')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # SQLiteの場合
    is_sqlite = is_sqlite_bool(app.config['SQLALCHEMY_DATABASE_URI'])
    if is_sqlite:
        # インスタンスディレクトリがなければ作成
        if not os.path.exists(app.instance_path):
            os.makedirs(app.instance_path, exist_ok=True)

    # アプリ名・バージョン・デバッグモードの設定
    app.config['APP_TITLE'] = const.APP_TITLE
    app.config['VERSION'] = const.VERSION
    app.config['DEBUG_MODE'] = os.getenv('DEBUG_MODE', 'False').lower() in ['true', '1', 'yes']
    app.debug = app.config['DEBUG_MODE']
    # チャットログの保存日数（通常・バックアップ）の設定
    app.config['CHAT_LOG_DAYS'] = int(const.CHAT_LOG_DAYS)
    app.config['CHAT_BACKUP_DAYS'] = int(const.CHAT_BACKUP_DAYS)

    # SQLAlchemy、SocketIOをFlaskアプリに紐付け
    db.init_app(app)
    socketio.init_app(app)

    # ルーム関連のBlueprintを登録
    app.register_blueprint(room_bp)
    app.register_blueprint(auth_bp)

    return app, is_sqlite
