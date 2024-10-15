from combinatorizor import Combinatorizor
from scraps import WebScraper
from graphorizor import Graphorizor

if __name__ == '__main__':
    graphorizor = Graphorizor()
    combinatorizor = Combinatorizor()

    with open('target_links.txt', 'r') as file:
        for line in file:
            ws = WebScraper(line)
            combinatorizor.push(ws)