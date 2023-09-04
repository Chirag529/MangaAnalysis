
import pandas as pd
import requests
import csv
from bs4 import BeautifulSoup as bs
import lxml
import urllib3
from fake_useragent import UserAgent

# Get the url for the page to be scrapped
url = "https://www.amazon.in/s?k=manga&ref=nb_sb_noss"

# # Get a fake user agent to avoid getting blocked by the website
# ua = UserAgent()

# # Get a random browser user-agent string
# print(ua.random)


# Headers for the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "language": "en-US,en;q=0.9",
}

# Suspend the warning for the SSL certificate verification using urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Lists to store scraped data
Manga_Name = []
Manga_Price = []
Manga_Rating = []
Manga_Desc = []


# Get the response from the website
try:
    response = requests.get(url, headers=headers, verify=False)

    # Print the response code
    response_code = response.status_code
    print("Response Code:", response_code)

    # Check the response code
    if response_code == 200:
        print("Connection Successful")
    else:
        print("Connection Failed")
except Exception as e:
    print("Error occurred:", e)

