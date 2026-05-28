API_KEY = "SECRET-12345-DO-NOT-SHARE"

def process_payment(amount):
    if amount > 0:
        return "Payment processed with key: " + API_KEY
    return "Invalid amount"
