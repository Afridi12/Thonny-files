from Question import Question
import sys
questionList = [Question('Who is the first US President?', 'George Washington', 'Donald Trump', 'Barrack Obama','Ronald Raegan', 1),
                Question('Who is the current President?', 'George Washington', 'Donald Trump', 'Barrack Obama','Ronald Raegan', 2),
                Question('Who won the last World Cup?', 'Spain', 'Sweden', 'France','Germany', 3),
                Question('Who won the last SuperBowl?', 'Eagles', 'Patriots', 'Packers','Bengals', 2),
                Question('Who invented Facebook?', 'Steve Jobs', 'Mark Zuckerburg', 'Vint Cerf','Robert E.Kahn', 2),
                Question('What is an example of a MOBA game?', 'DOTA 2', 'Halo', 'Age of Empires','StarCraft', 1),
                Question('Who published the first Halo?', 'Microsoft', 'Activision', 'EA','Bungie Studios', 4),
                Question('How many Dark Souls games are there?', '3', '4', '5','2', 2),
                Question('Who is the second US President?', 'George Washington', 'John Adams', 'Barrack Obama','Ronald Raegan', 2),
                Question('How many letters in the alphabet?', '26', '25', '27','30', 1)]
if __name__ == '__main__':
    counter = 0
    player1Score = 0
    player2Score = 0
    print('Welcome to the Python intro programming quiz')
    print('--------------------------------------------')
    print('')
    
    everyAnswer = True
    for i in questionList:
        counter += 1
        
        try:
            if(counter % 2 == 1):
                print('')
                print('Player 1 here is your question:')
                print('')
                print(i)
                print('')
                inputAnswer = int(input('Enter answer:'))
                while not (((inputAnswer <= 4) and (inputAnswer >= 1))):
                    print('Error: Your answer has to be a value between 1 and 4. Try again.')
                    inputAnswer = int(input('Enter answer:'))
                if(counter == 1 and inputAnswer == 1):
                    print('Excellent! You score!')
                    player1Score += 1
                elif(counter == 3 and inputAnswer == 3):
                    print('Excellent! You score!')
                    player1Score += 1
                elif((counter == 5 or counter == 9) and inputAnswer == 2):
                    print('Excellent! You score!')
                    player1Score += 1
                elif(counter == 7 and inputAnswer == 4):
                    print('Excellent! You score!')
                    
                    player1Score += 1
                else:
                    print('That is incorrect. Better luck with the next question.')

            if(counter % 2 == 0):
                print('')
                print('Player 2 here is your question:')
                print('')
                print(i)
                print('')
                inputAnswer = int(input('Enter answer:'))
                while not (((inputAnswer <= 4) and (inputAnswer >= 1))):
                    print('Error: Your answer has to be a value between 1 and 4. Try again.')
                    inputAnswer = int(input('Enter answer:'))
                if((counter == 2 or counter == 4 or counter == 8)  and inputAnswer == 2):
                    print('Excellent! You score!')
                    player2Score += 1
                elif((counter == 6 or counter == 10) and inputAnswer == 1):
                    print('Excellent! You score!')
                    player2Score += 1
                else:
                    print('That is incorrect. Better luck with the next question.')
    

        except:
            break
    print('')
    print('And the final scores are:')
    print('Player 1:', player1Score)
    print('Player 2:', player2Score)
    if(player1Score > player2Score):
        print('Player 1 wins!')
    elif(player2Score > player1Score):
        print('Player 2 wins!')
    else:
        print("It's a tie!")
            

        
        
        