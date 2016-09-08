class Band:
    def __init__(self, name, url, band_id):
        self.name = name
        self.url = url
        self.band_id = band_id
        
    def __str__(self):
        return "{}: {} ... {}".format(self.name, self.url, self.band_id)
        
