from Question import Question
questionList = [Question('Who is the first US President?', 'George Washington', 'Donald Trump', 'Barrack Obama','Ronald Raegan', 1),
                Question('Who is the current President?', 'George Washington', 'Donald Trump', 'Barrack Obama','Ronald Raegan', 2),
                Question('Who the the last World Cup?', 'Spain', 'Sweden', 'France','Germany', 3),
                Question('Who won the last SuperBowl?', 'Eagles', 'Patriots', 'Packers','Bengals', 2),
                Question('Who invented Facebook?', 'Steve Jobs', 'Mark Zuckerburg', 'Vint Cerf','Robert E.Kahn', 2),
                Question('What is an example of a MOBA game?', 'DOTA 2', 'Halo', 'Age of Empires','StarCraft', 1),
                Question('Who published the first Halo?', 'Microsoft', 'Activision', 'EA','Bungie Studios', 4),
                Question('How many Dark Souls games are there?', '3', '4', '5','2', 2),
                Question('Who is the second US President?', 'George Washington', 'John Adams', 'Barrack Obama','Ronald Raegan', 2),
                Question('How many letters in the alphabet?', '26', '25', '27','30', 1)]
if __name__ == '__main__':
    
    player1Score = 0
    player2Score = 0
    print('Welcome to the Python intro programming quiz')
    print('--------------------------------------------')
    print('')
    everyAnswer = True
    for i in questionList:
        try:
            print('Player 1 here is your question:')
            print(i)
            inputAnswer = int(input('Enter answer:\n'))
        except:
            
        
        
        
        