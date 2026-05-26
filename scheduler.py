import time

def run_scheduler():
    while True:
        print("Checking for new files...")
        time.sleep(120)

if __name__ == "__main__":
    run_scheduler()
