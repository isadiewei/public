from scraps import WebScraper

class Combinatorizor:
    def __init__(self):
        self.unprocessed = []
        self.processed = []

    def push(self, web_scraper: WebScraper):
        # seems redundant and memory inefficient but away we go
        self.unprocessed.append(web_scraper)

        # if you want add more threading or something here
        # this is just for demo but if i don't note it i'll get pissed off at myself
        web_scraper.process_link()

