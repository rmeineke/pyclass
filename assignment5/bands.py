import bs4


class Band:
    def __init__(self, name, url, band_id, func):
        self.name = name
        self.url = url
        self.band_id = band_id
        self.scrape_func = func
        
    def __str__(self):
        return "{}: {} ... {}".format(self.name, self.url, self.band_id)
        
        
    # certain bands will have to have their tour pages scraped
    # manually ... they will have their own particular set of
    # html tags that will need to be handled individually
    def GetEventInfoForTSisters(html):
        """
        This is the specific call for the T-Sisters website
        """
        soup = bs4.BeautifulSoup(html, 'html.parser')
        for litag in soup.find_all('li', {'class': 'event'}):
            for h5tag in litag.find('h5'):
                print(h5tag)
    
