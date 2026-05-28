API_TOKEN = "sk_live_987654321"  # intentional security test

def validate_user_input(user_id, age):
    if age >= 18:
        return f"User {user_id} is valid"
    return "Invalid user"
