import schedule
import time
import os

def run_main():
    os.system("python main.py")

# to run every hour
schedule.every(1).hours.do(run_main)

if __name__ == "__main__":
    print("Scheduler running... Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
