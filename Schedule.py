import schedule
import time
import subprocess
import datetime
import requests


def notify_local_computer():
    webhook_url = "http://your-local-ip:5000/trigger_notifications"  # Replace with your local IP or domain
    response = requests.post(webhook_url)
    if response.status_code == 200:
        print("Notifications triggered successfully on your local computer")
        # Schedule the updatePrice and Notifications tasks at specific times
        schedule.every().day.at("21:30").do(check_prices)
        schedule.every().day.at("21:31").do(notify_changes)

# Schedule the notify_local_computer function at a specific time
schedule.every().day.at("15:10").do(notify_local_computer)


# Map the system timezone identifier to the corresponding pytz identifier
system_timezone_identifier = 'W. Europe Standard Time'
pytz_mapping = {
    'W. Europe Standard Time': 'Europe/Amsterdam'
}
expected_timezone_identifier = pytz_mapping.get(system_timezone_identifier, 'Europe/Amsterdam')


# Function to execute the daily_task.py script
def check_prices():
    subprocess.run(["python", "UpdatePrice.py"])

def notify_changes():
    subprocess.run(["python","Notifications.py"])

while True:
    print(f"Checking schedule at {datetime.datetime.now()}")
    schedule.run_pending()
    time.sleep(14400)