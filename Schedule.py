import schedule
import time
import subprocess
import datetime



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

# Schedule the updatePrice and Notifications tasks at specific times
schedule.every().day.at("15:09").do(check_prices)
schedule.every().day.at("15:10").do(notify_changes)

while True:
    print(f"Checking schedule at {datetime.datetime.now()}")
    schedule.run_pending()
    time.sleep(1)