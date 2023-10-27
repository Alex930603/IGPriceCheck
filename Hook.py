from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/trigger_notifications', methods=['POST'])
def trigger_notifications():
    # Execute your notifications.py script
    subprocess.run(["python", "notifications.py"])
    return "Notifications triggered"

if __name__ == '__Hook__':
    app.run(host='0.0.0.0', port=5000) 