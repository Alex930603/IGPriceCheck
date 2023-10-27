import schedule
import time
import subprocess
import datetime
import requests


def notify_local_computer():
    webhook_url = "http://192.168.1.112:5000/trigger_notifications"  # Replace with your local IP or domain
    response = requests.post(webhook_url)
    if response.status_code == 200:
        print("Notifications triggered successfully on your local computer")
        # Schedule the updatePrice and Notifications tasks at specific times
# Schedule the notify_local_computer function at a specific time
schedule.every(1).minutes.do(notify_local_computer)


# Map the system timezone identifier to the corresponding pytz identifier
system_timezone_identifier = 'W. Europe Standard Time'
pytz_mapping = {
            'W. Europe Standard Time': 'Europe/Amsterdam'
        }
expected_timezone_identifier = pytz_mapping.get(system_timezone_identifier, 'Europe/Amsterdam')

while True:
    print(f"Checking schedule at {datetime.datetime.now()}")
    schedule.run_pending()
    time.sleep(60)