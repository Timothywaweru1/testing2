class Album:
    GENRES = ["Hip-hop","Jaz","Pop"]
    album_count = 0
    def __init__(self,genre,date):
        self.date = date
        self.genre = genre
        self.number_of_album()
    @classmethod
    def number_of_album(cls):
        cls.album_count += 1   
travis_scott = Album(2024,"Hip-hop")
future = Album(2025,"Hip-hop")  
drake = Album(2024,"Hip-hop")   
weeknd = Album(2024,"Pop")          
print(Album.album_count)