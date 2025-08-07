# app/models/room.py
# チャットルームのデータ管理（SQLAlchemyモデル版）

from app.extensions import db

class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    owner_id = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<Room {self.name}>'

def add_room(room_name, owner_id=None):
    if Room.query.filter_by(name=room_name).first():
        return
    room = Room(name=room_name, owner_id=owner_id)
    db.session.add(room)
    db.session.commit()

def get_rooms():
    return [room.name for room in Room.query.all()]

def get_room_owner(room_name):
    room = Room.query.filter_by(name=room_name).first()
    return room.owner_id if room else None

def delete_room(room_name, owner_id=None):
    room = Room.query.filter_by(name=room_name).first()
    if room:
        if owner_id is None or room.owner_id == owner_id:
            db.session.delete(room)
            db.session.commit()
            return True
    return False

def get_room_id(room_name):
    room = Room.query.filter_by(name=room_name).first()
    return room.id if room else None
