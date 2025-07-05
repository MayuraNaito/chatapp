rooms = []
room_owners = {}  # 部屋名: ユーザーID

def add_room(room_name, owner_id=None):
    if room_name and room_name not in rooms:
        rooms.append(room_name)
        if owner_id:
            room_owners[room_name] = owner_id

def get_rooms():
    return rooms

def get_room_owner(room_name):
    return room_owners.get(room_name)

def delete_room(room_name, owner_id=None):
    if room_name in rooms:
        if owner_id is None or room_owners.get(room_name) == owner_id:
            rooms.remove(room_name)
            room_owners.pop(room_name, None)
            return True
    return False
