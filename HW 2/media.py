class Media:
    def __init__(self, rating, typeOf, name):
        self.__rating = rating
        self.__typeOf = typeOf
        self.__name = name
    def getRating(self):
        return self.__rating
    def getTypeOf(self):
        return self.__typeOf
    def getName(self):
        return self.__name
    def setName(self):
        self.__name = name
    def __str__(self):
        return 'Name: ' + self.__name + '\nRating: '+self.__rating + '\nType: ' + self.__typeOf
    
class Movie(Media):
    def __init__(self, rating, typeOf, name, running, director):
        super().__init__(rating, typeOf, name)
        self.__director = director
        self.__running = running
    def getRunning(self):
        return self.__running
    def getDirector(self):
        return self.__director
    def play():
        print(self.__name + 'is playing now.')
    def __str__(self):
        newSt = super().__str__()
        newSt += ' ' + '\nRunning Time: ' + self.__running + '\nDirector: ' +self.__director
        return newSt

class Song(Media):
    def __init__(self, rating, typeOf, name, album, artist):
        super().__init__(rating, typeOf, name)
        self.__album = album
        self.__artist = artist
    def play(self):
        print(self.__name + 'is playing now.')
    def getAlbum(self):
        return self.__album
    def getArtist(self):
        return self.__artist
    def setAlbum(self):
        self.__album = album
    def __str__(self):
        newSt = super().__str__()
        newSt += ' ' + '\nAlbum: ' + self.__album + '\nArtist: ' +self.__artist
        return newSt
class Picture(Media):
    def __init__(self, rating, typeOf, name, resolution):
        super().__init__(rating, typeOf, name)
        self.__resolution = resolution
    def play(self):
        print(self.__name + 'is playing now.')
    def getResolution(self):
        return self.__resolution
    def __str__(self):
        newSt = super().__str__()
        newSt += ' ' + '\nResolution: ' + self.__resolution
        return newSt
    

        
        
        

        

a = Movie('4/10','Movie','Transformer', '2:00:00', 'Michael Bay')
b = Song('10/10','Song','Carnival of Rust', '3:27', 'Something')
c = Picture('10/10','Picture','Monalisa','300')
print(a)
print('')
print(b)
print('')
print(c)


