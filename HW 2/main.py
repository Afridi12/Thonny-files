#Afridi Karim 3 #Lab 62
from media import *
import sys
mediaList = [Song('10/10','Song','Carnival of Rust', 'Carnival of Rust', 'Poets of the Fall'),
            Song('10/10','Song','Congratulations', 'Stoney', 'Post Malone'), # The list of everything, it contains all songs, movies and pictures.
            Song('10/10','Song','As if its your last', 'BlackPink in your area', 'BLACKPINK'),
            Song('10/10','Song','What is Love?', 'What is Love?', 'Twice'),
            Movie('4/10','Movie','Transformer', '2:00:00', 'Michael Bay'),
            Movie('6/10','Movie','Wild Wild West', '1:00:00', 'Barry Sonnenfeld'),
            Movie('9/10','Movie','Christopher Robin', '1:30:00', 'Marc Forster'),
            Movie('8/10','Movie','Lion King', '2:30:00', 'Jon Favreau'),
            Picture('9/10','Picture','Monalisa','300'),
            Picture('7/10','Picture','Starry Night','1022'),
            Picture('1/10','Picture','Migrant Mother','1080'),
            Picture('10/10','Picture','V-J Day','600')]

songList =[Song('10/10','Song','Carnival of Rust', 'Carnival of Rust', 'Poets of the Fall'),
           Song('10/10','Song','Congratulations', 'Stoney', 'Post Malone'),
           Song('10/10','Song','As if its your last', 'BlackPink in your area', 'BLACKPINK'),# this is a list of all the songs
           Song('10/10','Song','What is Love?', 'What is Love?', 'Twice')]

movieList =[Movie('4/10','Movie','Transformer', '2:00:00', 'Michael Bay'),# list of all the movie objects
            Movie('6/10','Movie','Wild Wild West', '1:00:00', 'Barry Sonnenfeld'),
            Movie('9/10','Movie','Christopher Robin', '1:30:00', 'Marc Forster'),
            Movie('8/10','Movie','Lion King', '2:30:00', 'Jon Favreau')]

pictureList =[Picture('10/10','Picture','Monalisa','300'),# list of all the picture objects
              Picture('10/10','Picture','Starry Night','1022'),
              Picture('10/10','Picture','Migrant Mother','1080'),
              Picture('10/10','Picture','V-J Day','600')]
emptyString = ''#the empty string the play/show function will be put into.
if __name__ == '__main__': # initially sets the boolean true to make it loop everytime. and asks for input.
    boolean = True
    print('Welcome')
    choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
    while boolean:
        if choice == '0':
            sys.exit(0)
        else: 
            try:
                if choice == '4':# 4 is the choice for looking at all the types of media so it prints out the first list. 

                    print(*mediaList, sep ='\n\n')
                    boolean = False
                elif choice == '1': #if they choose 1 for a list of songs it will print out all the songs and ask them whether they want to listen to it or not, if no it will bring them back to the menu if not they can choose which song from the names and writing the names down. 
                    print(*songList, sep = '\n\n')
                    boolean = False
                    inputChoice = input('Would you like to listen to a song?(Y/N):\n')
                    if inputChoice == 'Y' or inputChoice == 'y':
                        songChoice = input('Which song would you like to listen to?\n')
                        for i in range(0, len(songList)):
                            if songChoice.lower() == songList[i].getName().lower():
                                                                                        # based on the song they pick, it will play and call the play function.
                                emptyString = songList[i].play()
                                print(emptyString)
                                boolean = True
                                choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                            
                        for j in range(0, len(songList)):
                            if songList[j].getName().lower() != songChoice.lower():
                                print('Song not found. Try Again')
                                break
                    
                    elif inputChoice == 'N' or inputChoice == 'n': # if the they say n or N when asked whether they want to listen or watch something, then it goes back to asking them again from the main menu.
                        boolean = True
                        choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')

                elif choice == '2': # the second choice for movies
                    print(*movieList, sep = '\n\n')
                    boolean = False
                    inputChoice = input('Would you like to watch a movie?(Y/N):\n')
                    if inputChoice == 'Y' or inputChoice == 'y':
                        movieChoice = input('Which movie would you like to watch?\n')
                        for i in range(0, len(movieList)): # go through the list of movies
                            if movieChoice.lower() == movieList[i].getName().lower():
                                                                                        # based on the song they pick, it will play and call the play function.
                                emptyString = movieList[i].play()
                                print(emptyString)
                                boolean = True
                                choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        for j in range(0, len(movieList)): # checks for correct input, if not breaks out of the loop.
                            if movieList[j].getName().lower() != movieChoice.lower():
                                print('Movie not found. Try Again')
                                break
                    elif inputChoice == 'N' or inputChoice == 'n':
                        boolean = True
                        choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        
                elif choice == '3': #the third choice for pictures
                    print(*pictureList, sep = '\n\n')
                    boolean = False
                    inputChoice = input('Would you like to look at pictures?(Y/N):\n')
                    if inputChoice == 'Y' or inputChoice == 'y':
                        pictureChoice = input('What picture would you like to see?\n')
                        for i in range(0, len(pictureList)):
                            if pictureChoice.lower() == pictureList[i].getName().lower():
                                emptyString = pictureList[i].show()
                                print(emptyString)
                                boolean = True
                                choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        for j in range(0, len(pictureList)): # checks whether the input is a valid a input if not it says so and quits out of the function
                            if pictureList[j].getName().lower() != pictureChoice.lower():
                                print('Picture not found. Try Again')
                                break  
                    elif inputChoice == 'N' or inputChoice == 'n':
                        boolean = True
                        choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
            except:
                    choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
            
        


