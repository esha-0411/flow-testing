import time

def run_scheduler():
    while True:
        print("Checking for new emails...")
        time.sleep(120)

if __name__ == "__main__":
    run_scheduler()
