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
    def __str__(self):
        return 'Name: ' + self.__name + '\nRating:'+self.__rating + '\nType:' + self.__typeOf

a = Media('4/10', 'Song', 'Alex')
print(a)
b = a.getRating()
print(b)