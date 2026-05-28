API_KEY = "sk_test_1234567890"  # intentional security issue

def process_payment(amount):
    if amount > 0:
        return f"Processed payment of {amount}"
    return "Invalid amount"
