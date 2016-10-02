import bs4


class Venue:
    def __init__(self, name, url, func):
        self.name = name
        self.url = url
        self.scrape_func = func
        
        
    def __str__(self):
        return "{}: {} ... {}".format(self.name, self.url, self.scrape_func)
        
    
    def RioTheatre(html):
        """
        This is the specific call for the Rio Theatre website
        """
        soup = bs4.BeautifulSoup(html, 'html.parser')
        for litag in soup.find_all('li', {'class': 'event'}):
            for h5tag in litag.find('h5'):
                print(h5tag)
    
