from media import *
import sys
mediaList = [Song('10/10','Song','Carnival of Rust', 'Carnival of Rust', 'Poets of the Fall'),
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

songList =[Song('10/10','Song','Carnival of Rust', 'Carnival of Rust', 'Poets of the Fall'),
           Song('10/10','Song','Congratulations', 'Stoney', 'Post Malone'),
           Song('10/10','Song','As if its your last', 'BlackPink in your area', 'BLACKPINK'),
           Song('10/10','Song','What is Love?', 'What is Love?', 'Twice')]


movieList =[Movie('4/10','Movie','Transformer', '2:00:00', 'Michael Bay'),
            Movie('6/10','Movie','Wild Wild West', '1:00:00', 'Barry Sonnenfeld'),
            Movie('9/10','Movie','Christopher Robin', '1:30:00', 'Marc Forster'),
            Movie('8/10','Movie','Lion King', '2:30:00', 'Jon Favreau')]

pictureList =[Picture('10/10','Picture','Monalisa','300'),
              Picture('10/10','Picture','Starry Night','1022'),
              Picture('10/10','Picture','Migrant Mother','1080'),
              Picture('10/10','Picture','V-J Day','600')]
emptyString = ''
if __name__ == '__main__':
    boolean = True
    print('Welcome')
    choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
    while boolean:
        if choice == '0':
            sys.exit(0)
        else: 
            try:
                if choice == '4':
                    print(*mediaList, sep ='\n\n')
                    boolean = False
                elif choice == '1':
                    print(*songList, sep = '\n\n')
                    boolean = False
                    inputChoice = input('Would you like to listen to a song?(Y/N):\n')
                    if inputChoice == 'Y' or inputChoice == 'y':
                        songChoice = input('Which song would you like to listen to?\n')
                        if songChoice.lower() == songList[0].getName().lower():
                            emptyString = songList[0].play()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')

                        elif songChoice.lower() == songList[1].getName().lower():
                            emptyString = songList[1].play()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        elif songChoice.lower() == songList[2].getName().lower():
                            emptyString = songList[2].play()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        elif songChoice.lower() == songList[3].getName().lower():
                            emptyString = songList[3].play()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                    elif inputChoice == 'N' or inputChoice == 'n':
                        boolean = True
                        choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')

                elif choice == '2':
                    print(*movieList, sep = '\n\n')
                    boolean = False
                    inputChoice = input('Would you like to watch a movie?(Y/N):\n')
                    if inputChoice == 'Y' or inputChoice == 'y':
                        movieChoice = input('Which movie would you like to watch?\n')
                        if movieChoice.lower() == movieList[0].getName().lower():
                            emptyString = movieList[0].play()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        elif movieChoice.lower() == movieList[1].getName().lower():
                            emptyString = movieList[1].play()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        elif movieChoice.lower() == movieList[2].getName().lower():
                            emptyString = movieList[2].play()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        elif movieChoice.lower() == movieList[3].getName().lower():
                            emptyString = movieList[3].play()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                    elif inputChoice == 'N' or inputChoice == 'n':
                        boolean = True
                        choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        
                elif choice == '3':
                    print(*pictureList, sep = '\n\n')
                    boolean = False
                    inputChoice = input('Would you like to look at pictures?(Y/N):\n')
                    if inputChoice == 'Y' or inputChoice == 'y':
                        pictureChoice = input('What picture would you like to see?\n')
                        if pictureChoice.lower() == pictureList[0].getName().lower():
                            emptyString = pictureList[0].show()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        elif pictureChoice.lower() == pictureList[1].getName().lower():
                            emptyString = pictureList[1].show()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        elif pictureChoice.lower() == pictureList[2].getName().lower():
                            emptyString = pictureList[2].show()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                        elif pictureChoice.lower() == pictureList[3].getName().lower():
                            emptyString = pictureList[3].show()
                            print(emptyString)
                            boolean = True
                            choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
                    elif inputChoice == 'N' or inputChoice == 'n':
                        boolean = True
                        choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
            
                    
            except:
                    choice = input('If you would like to see a list of songs press 1\nFor Movies Press 2\nPictures press 3\nTypes of Media click 4:\nTo exit enter 0\n')
            
        


