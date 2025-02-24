import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://astrotalk.com/freekundli/basic-detail"

# Headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0 Safari/537.36"
}

# Sending a GET request
response = requests.get(url, headers=headers)

# Check response status
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    # Replace this with the actual tag/class/id you want to scrape
    data = soup.find_all('div', class_='desired-class')
    for item in data:
        print(item.text)
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
