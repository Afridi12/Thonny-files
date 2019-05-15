#Afridi Karim 3 #Lab 62
from media import *
import sys
mediaList = [Song('10/10','Song','Carnival of Rust', 'Carnival of Rust', 'Poets of the Fall'), # The list of everything, it contains all songs, movies and pictures.
            Song('10/10','Song','Congratulations', 'Stoney', 'Post Malone'),
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

songList =[Song('10/10','Song','Carnival of Rust', 'Carnival of Rust', 'Poets of the Fall'), # this is a list of all the songs
           Song('10/10','Song','Congratulations', 'Stoney', 'Post Malone'),
           Song('10/10','Song','As if its your last', 'BlackPink in your area', 'BLACKPINK'),
           Song('10/10','Song','What is Love?', 'What is Love?', 'Twice')]


movieList =[Movie('4/10','Movie','Transformer', '2:00:00', 'Michael Bay'), # list of all the movie objects
            Movie('6/10','Movie','Wild Wild West', '1:00:00', 'Barry Sonnenfeld'),
            Movie('9/10','Movie','Christopher Robin', '1:30:00', 'Marc Forster'),
            Movie('8/10','Movie','Lion King', '2:30:00', 'Jon Favreau')]

pictureList =[Picture('10/10','Picture','Monalisa','300'), # list of all the picture objects
              Picture('10/10','Picture','Starry Night','1022'),
              Picture('10/10','Picture','Migrant Mother','1080'),
              Picture('10/10','Picture','V-J Day','600')]
emptyString = '' #the empty string the play/show function will be put into.
if __name__ == '__main__': # initially sets the boolean true to make it loop everytime. and asks for input.
    boolean = True
    print('Welcome')
    choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
    while boolean:
        if choice == '0':
            sys.exit(0)
        else: 
            try:
                if choice == '4': # 4 is the choice for looking at all the types of media so it prints out the first list. 
                    print(*mediaList, sep ='\n\n')
                    boolean = False
                    

                elif choice == '1': #if they choose 1 for a list of songs it will print out all the songs and ask them whether they want to listen to it or not, if no it will bring them back to the menu if not they can choose which song from the names and writing the names down. 
                    print(*songList, sep = '\n\n')
                    boolean = False
                    inputChoice = input('Would you like to listen to a song?(Y/N):\n')
                    if inputChoice == 'Y' or inputChoice == 'y':
                        songChoice = input('Which song would you like to listen to?\n\n')
                        if songChoice.lower() == songList[0].getName().lower():# based on the song they pick, it will play and call the play function.
                            emptyString = songList[0].play()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                            continue
                        elif songChoice.lower() != songList[0].getName().lower():
                            print('Sorry could not find that song, try again\n')
                            boolean = True # if they input the wrong thing then it will tell them and send them back to the menu.
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                            
                            continue
                        if songChoice.lower() == songList[1].getName().lower(): # this is the second song and functions the same way as the last if/else statement.
                            emptyString = songList[1].play()# sets the empty string into the name and calls the play function.
                            print(emptyString)
                            boolean = True # it sets the boolean equal to true so that it will loop.
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                            continue
                        elif songChoice.lower() != songList[1].getName().lower():
                            boolean = True
                            print('Sorry could not find that song, try again\n')
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                            continue
                        if songChoice.lower() == songList[2].getName().lower(): # third song choice does same thing as everything else
                            emptyString = songList[2].play()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                            continue
                        elif songChoice.lower() != songList[2].getName().lower():
                            boolean = True
                            print('Sorry could not find that song, try again\n')
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                            continue
                        if songChoice.lower() == songList[3].getName().lower(): #4th song choice
                            emptyString = songList[3].play()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                            continue
                        elif songChoice.lower() != songList[3].getName().lower():
                            boolean = True
                            print('Sorry could not find that song, try again\n')
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                            continue
                    elif inputChoice == 'N' or inputChoice == 'n':
                        boolean = True
                        choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        continue
                elif choice == '2': # this elif does the same thing the song stuff does.
                    print(*movieList, sep = '\n\n') # prints all the items in the movieList based on the string from the class
                    boolean = False
                    inputChoice = input('Would you like to watch a movie?(Y/N):\n')
                    if inputChoice == 'Y' or inputChoice == 'y':
                        movieChoice = input('Which movie would you like to watch?\n')
                        if movieChoice.lower() == movieList[0].getName().lower(): # first movie choice, names are not case sensitive but have to be written correctly, otherwises it will just kick you out.
                            emptyString = movieList[0].play()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        else:
                            boolean = True
                            print('Sorry could not find that movie, try again\n')
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        if movieChoice.lower() == movieList[1].getName().lower():
                            emptyString = movieList[1].play() # second movie choice.
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        else:
                            boolean = True
                            print('Sorry could not find that movie, try again\n')
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        if movieChoice.lower() == movieList[2].getName().lower(): # third song choice
                            emptyString = movieList[2].play()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        else:
                            boolean = True
                            print('Sorry could not find that movie, try again\n')
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        if movieChoice.lower() == movieList[3].getName().lower(): # 4th song choice
                            emptyString = movieList[3].play()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        else:
                            boolean = True
                            print('Sorry could not find that movie, try again\n')
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                    elif inputChoice == 'N' or inputChoice == 'n':
                        boolean = True
                        choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        
                elif choice == '3': # works the same as all other, if statements, if they pick 3 it will ask them for which picture they want
                    print(*pictureList, sep = '\n\n')
                    boolean = False
                    inputChoice = input('Would you like to look at pictures?(Y/N):\n')
                    if inputChoice == 'Y' or inputChoice == 'y':
                        pictureChoice = input('What picture would you like to see?\n')
                        if pictureChoice.lower() == pictureList[0].getName().lower(): # first picture choice
                            emptyString = pictureList[0].show()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        else:
                            boolean = True
                            print('Sorry could not find that picture, try again\n')
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        if pictureChoice.lower() == pictureList[1].getName().lower(): # second choice
                            emptyString = pictureList[1].show()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        else:
                            boolean = True
                            print('Sorry could not find that picture, try again\n')
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        if pictureChoice.lower() == pictureList[2].getName().lower(): # third picture
                            emptyString = pictureList[2].show()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        else:
                            boolean = True
                            print('Sorry could not find that picture, try again\n')
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        if pictureChoice.lower() == pictureList[3].getName().lower(): #fourth choice
                            emptyString = pictureList[3].show()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        else:
                            boolean = True
                            print('Sorry could not find that picture, try again\n')
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                    elif inputChoice == 'N' or inputChoice == 'n': # if they say no at all then it brings them back to the menu
                        boolean = True
                        choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
            
                    
            except: # if any errors are come across it will just ask them for an input
                    choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
            
        

