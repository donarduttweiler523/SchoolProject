import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', {'class': 'content'}).get_text()
        return content
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    url = "https://www.example.com"
    page_content = fetch_webpage(url)
    if page_content:
        print(page_content)
