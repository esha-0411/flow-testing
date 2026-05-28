JWT_SECRET = "super_secret_123456"

def encode_user(user_id):
    return f"token-{user_id}-{JWT_SECRET}"
