# ユーザーモデル（簡易的なメモリ管理）
users = {}  # username: password

def register_user(username, password):
    if username in users:
        return False
    users[username] = password
    return True

def authenticate_user(username, password):
    return users.get(username) == password
