# ユーザー情報の管理（SQLAlchemyモデル版）

from app.extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

def register_user(username, password):
    if User.query.filter_by(username=username).first():
        return False
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return True

def authenticate_user(username, password):
    user = User.query.filter_by(username=username, password=password).first()
    return user is not None
