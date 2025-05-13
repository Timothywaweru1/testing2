class Songs:
    all = []
    def __init__(self,name):
        self.name = name
        Songs.store_songs(self)
        Songs.show_names()

    @classmethod
    def store_songs(cls,songs):
        cls.all.append(songs)

    @classmethod
    def show_names(cls):
        print([song.name for song in cls.all])  


song_1 = Songs("Thriller Bark")
song_2 = Songs("Goosebumps")
song_3 = Songs("Fein")
song_4 = Songs("Franchise")
song_5 = Songs("Boom") 
song_6 = Songs("One Dance")