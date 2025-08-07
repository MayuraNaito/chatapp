# run.py
# Flaskアプリケーションを起動する
import os
from app import create_app, socketio

app, is_sqlite = create_app()

# アプリの起動
if __name__ == '__main__':
    # SQLiteの場合
    if is_sqlite:
        # DBがなければ作成
        db_path = app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', '')
        if not os.path.exists(db_path):
            with app.app_context():
                from app.extensions import db
                db.create_all()
                print("SQLiteデータベース作成完了")

    debug_mode = app.config.get('DEBUG_MODE', 'False')
    socketio.run(app, debug=debug_mode)
