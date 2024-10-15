from combinatorizor import Combinatorizor
from scraps import WebScraper

if __name__ == '__main__':
    combinatorizor = Combinatorizor()

    with open('target_links.txt', 'r') as file:
        for line in file:
            ws = WebScraper(line)
            combinatorizor.push(ws)