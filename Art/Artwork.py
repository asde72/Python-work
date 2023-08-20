import Artist
class Artwork:
# TODO: Define constructor with parameters to initialize instance attributes
# (title, year_created, artist)
    def __init__(self,title='unknown',year_created = -1, artist = Artist.Artist()):
        self.title = title
        self.year_created = year_created
        self.artist = artist
# TODO: Define print_info() method
    def print_info(self):
        print(f'Title: {self.title}, ({str(self.year_created)})')