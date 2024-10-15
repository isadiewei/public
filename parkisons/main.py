from combinatorizor import Combinatorizor
from scraps import WebScraper

if __name__ == '__main__':
    combinatorizor = Combinatorizor()
    ws = WebScraper('https://www.genome.gov/Genetic-Disorders/Parkinsons-Disease')
    combinatorizor.push(ws)