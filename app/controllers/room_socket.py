from flask_socketio import join_room, emit
from app.extensions import socketio

@socketio.on('join')
def on_join(room):
    join_room(room)

@socketio.on('room_message')
def handle_room_message(data):
    room = data['room']
    msg = data['msg']
    emit('room_message', {'room': room, 'msg': msg}, room=room)
