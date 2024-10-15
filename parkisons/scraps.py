import requests
import uuid
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, target_url):
        self.uuid = uuid.uuid4()
        self.target_url = target_url

    def process_link(self):
        print('debugging at its finest this does nothing useful yet')
        response = requests.get(self.target_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # great more console wrappers
        for link in soup.find_all('a'):
            print(link.get('href'))

        find_these = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        for text in soup.find_all(find_these):
            print(text)
