import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QFontDatabase
import requests
import json
import os
from bs4 import BeautifulSoup



class new_game_data:
    def __init__(self):
        self.name = ""
        self.link=""
        self.price_range=0.00
        self.price=0.00

Game=new_game_data()

# Create a JSON file to store the games
json_filename = "games.json"

# Check if the JSON file exists
if os.path.exists(json_filename):
    # Load the existing data from the JSON file
    with open(json_filename, "r") as file:
        game_data = json.load(file)
else:
    # Create an empty list to represent the game objects
    game_data = []




class InputFieldApp :
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.window.setGeometry(100, 100, 1000, 500)
        self.window.setWindowTitle("Input Field Example")
        self.window.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:0, y2:1, "
            "stop:0 #FF087B, stop:1 #246EB9);")

        self.central_widget = QWidget()
        self.layout = QVBoxLayout()

         # Load and set the Roboto font
        font = QFont()
        font.setFamily("Dubai")  # Replace with the actual font family name
        font.setPointSize(25)  # Set the font size
        font.setBold(True)


        self.input_field1 = QLineEdit()
        self.input_field1.setFont(font)
        self.input_field1.setPlaceholderText("Enter link of the game here")
        
        self.input_field1.setStyleSheet("background-color:Transparent; border:none; color:white")
        self.input_field1.returnPressed.connect(self.scrap_data)

        self.input_field2 = QLineEdit()
        self.input_field2.setFont(font)
        self.input_field2.setPlaceholderText("Enter price of the game here")

        self.input_field2.setStyleSheet("background-color:Transparent; border:none; color:white")
        self.input_field2.returnPressed.connect(self.scrap_data)

        self.layout.addWidget(self.input_field1)
        self.central_widget.setLayout(self.layout)

        self.layout.addWidget(self.input_field2)
        self.central_widget.setLayout(self.layout)

        self.window.setCentralWidget(self.central_widget)
        self.window.show()

#        fonts = QFontDatabase()
#       names = fonts.families()


    def scrap_data(self):

        self.Link = self.input_field1.text()
        self.Price_range = self.input_field2.text()
        # Define headers to mimic a browser request
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
        }

        # Send an HTTP GET request with headers to the URL
        response = requests.get(self.Link, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the page content with BeautifulSoup

            print("Good")

            soup = BeautifulSoup(response.text, "html.parser")

            # Example: Extract the titles of games

            Game.name = soup.find("h1", class_="game-title").text
            Game.price = soup.find("div", class_="total").text     

        else:
            print("Failed to retrieve the page. Status code:", response.status_code)

            # Append the new game data to the existing game data
        game_data.append({"price_range": self.Price_range,"link":self.Link, "name":Game.name, "price":Game.price})

        # Save the updated data to the JSON file
        with open(json_filename, "w") as file:
            json.dump(game_data, file, indent=2)
        
        self.app.quit()

    
    def run(self):
        sys.exit(self.app.exec_())
    

if __name__ == "__InsertGame__":
    app = InputFieldApp()
    app.run()

    