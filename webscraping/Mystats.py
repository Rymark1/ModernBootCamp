# https://rocketleague.tracker.network/rocket-league/profile/steam/76561198143627393/overview

import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://rocketleague.tracker.network/rocket-league/profile/steam/76561198143627393/overview")
print(response.text)
