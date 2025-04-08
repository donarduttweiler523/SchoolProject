import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        return soup
    else:
        raise Exception(f"Failed to retrieve data. Status code: {response.status_code}")

url = "https://www.example.com"
soup = fetch_data(url)
