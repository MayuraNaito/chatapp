# チャット部屋のリストとオーナー管理用辞書
rooms = []
room_owners = {}  # 部屋名: ユーザーID

# 部屋を追加（オーナーIDも記録）
def add_room(room_name, owner_id=None):
    if room_name and room_name not in rooms:
        rooms.append(room_name)
        if owner_id:
            room_owners[room_name] = owner_id

# すべての部屋名リストを返す
def get_rooms():
    return rooms

# 指定部屋のオーナーIDを返す
def get_room_owner(room_name):
    return room_owners.get(room_name)

# 部屋を削除（オーナーのみ可能）
def delete_room(room_name, owner_id=None):
    if room_name in rooms:
        if owner_id is None or room_owners.get(room_name) == owner_id:
            rooms.remove(room_name)
            room_owners.pop(room_name, None)
            return True
    return False
