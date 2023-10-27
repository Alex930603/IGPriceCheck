import requests
import json
from bs4 import BeautifulSoup

new_price = 0.00

json_filename = "games.json"

try:
    with open(json_filename, "r") as file:
        game_data = json.load(file)

    for game in game_data:
        link = game["link"]
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
        }

        # Send an HTTP GET request with headers to the URL
        response = requests.get(link, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the page content with BeautifulSoup

            soup = BeautifulSoup(response.text, "html.parser")

            new_price = soup.find("div", class_="total").text

            with open(json_filename, "w") as file:
                game["price"] = new_price
                json.dump(game_data, file, indent=2)
                print(f"Updated price for {game['name']} to {new_price}")

        else:
            print(f"Failed to retrieve the page for {game['name']}. Status code:", response.status_code)

except FileNotFoundError:
    print(f"JSON file '{json_filename}' not found.")
except json.JSONDecodeError:
    print(f"Error decoding JSON in '{json_filename}'.")
except Exception as e:
    print(f"An error occurred: {e}")
