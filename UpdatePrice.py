import requests
import json
from bs4 import BeautifulSoup

new_price=0.00

json_filename="games.json"

with open(json_filename, "r") as file:
    game_data = json.load(file)
    for game in game_data: 
                link=game["link"]
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

                    with open(json_filename,"w") as file:
                          game["price"]=new_price
                          json.dump(game_data,file,indent=2)

                else:
                    print("Failed to retrieve the page. Status code:", response.status_code)


