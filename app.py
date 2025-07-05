from flask import Flask
from flask_socketio import SocketIO
from app.controllers.room_controller import room_bp
from app.controllers.auth_controller import auth_bp
from dotenv import load_dotenv
import os

# .envファイルから環境変数を読み込む
load_dotenv()

# FlaskアプリとSocketIOのセットアップ
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret!')
socketio = SocketIO(app)

# ルーム関連のBlueprintを登録
app.register_blueprint(room_bp)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    socketio.run(app, debug=True)
