from plyer import notification
import json


# Create a notification
def notify (name,price):
    title = name
    message =" Now cost " + price 
    notification.notify(
        title=title,
        message=message,
        app_name="Your App Name",  # You can customize the app name
        timeout=4  # The notification will disappear after 10 seconds
    )

# Open and read the JSON file
with open("games.json", "r") as file:
    game_data = json.load(file)

for game in game_data:
    if game["price"]<=game["price_range"]:
        name=game["name"]
        price=game["price"]
        print(name)
        notify(name,price)
    else:
        continue


