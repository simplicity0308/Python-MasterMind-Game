#import random module
import random

#User defined function for game title and instructions
def op():
    print('| ==================== |')
    print('|                      |')
    print('|  M A S T E R M I N D |')
    print('|                      |')
    print('| ==================== |')
    print('')
    print('Welcome Player! This is Mastermind, a simple code breaking game.')
    print('')
    print('How to play: ')
    print('1. A random sequence of 4 fruits will be generated from a list of 4 fruits (Apple, Orange, Grape, Banana).')
    print('')
    print('2. The player shall guess the generated fruit sequence, after each round of guessing, the player will receive hints based on their guesses. ')
    print('   The player will receive hints on:')
    print('   - Number of correct fruits in the correct positions.')
    print('   - Number of correct fruits but in the incorrect position.')
    print('')
    print('3. The game will go on till the player guesses the correct sequence, the number of attempts taken will also be displayed at the end.')
    print('')
    print('4. During entering guesses, take note to only enter the correct fruit types with no extra spacing.')
    print('')
    print('5. If the player wishes to exit the game, please enter "exit" during the guessing phase.')
    print('')
    print('It is as simple as it sounds! Have fun guessing!')

#user defined function for ending message
def ed():
    print('=================================')
    print('Game terminated, Have a nice day!')
    print('=================================')

#create default fruit list
fruit_list = ['Apple', 'Orange', 'Grape', 'Banana']

#game starting message
head = op()

#condition for while loop to repeat the game
restart = True

#generate random fruit list
fruit_list_random = [random.choice(fruit_list), random.choice(fruit_list), random.choice(fruit_list), random.choice(fruit_list)]

count = 0
while restart:
    #player guess input, check each input for keyword 'exit'
    print('=============================================================')
    print('')
    print('Input guesses below: ')
    print('Available inputs: [Apple, Orange, Grape, Banana]')
    print('')

    guess_1 = str.capitalize(input('Please enter guess for position 1: '))
    while guess_1 == 'Exit':
        placeholder_1 = ''
        while placeholder_1 != 'cont':
            if guess_1 == 'Exit':
                exit_game = input('Are you sure to exit? [Y/N]: ')
                if exit_game == 'Y' or exit_game == 'y':
                    end = ed()
                    quit()
                elif exit_game == 'n' or exit_game == 'N':
                    print('<-------------------------------------->')
                    print('<  Game resumed, have fun guessing :)  >')
                    print('<-------------------------------------->')
                    guess_1 = str.capitalize(input('Please enter guess for position 1: '))
                    break
                else:
                    print('<-------------------------------------------------->')
                    print('< Invalid input, please choose between "Y" or "N"! >')
                    print('<-------------------------------------------------->')
                    continue
    
    guess_2 = str.capitalize(input('Please enter guess for position 2: '))
    while guess_2 == 'Exit':
        placeholder_2 = ''
        while placeholder_2 != 'cont':
            if guess_2 == 'Exit':
                exit_game = input('Are you sure to exit? [Y/N]: ')
                if exit_game == 'Y' or exit_game == 'y':
                    end = ed()
                    quit()
                elif exit_game == 'n' or exit_game == 'N':
                    print('<-------------------------------------->')
                    print('<  Game resumed, have fun guessing :)  >')
                    print('<-------------------------------------->')
                    guess_2 = str.capitalize(input('Please enter guess for position 2: '))
                    break
                else:
                    print('<-------------------------------------------------->')
                    print('< Invalid input, please choose between "Y" or "N"! >')
                    print('<-------------------------------------------------->')
                    continue

    guess_3 = str.capitalize(input('Please enter guess for position 3: '))
    while guess_3 == 'Exit':
        placeholder_3 = ''
        while placeholder_3 != 'cont':
            if guess_3 == 'Exit':
                exit_game = input('Are you sure to exit? [Y/N]: ')
                if exit_game == 'Y' or exit_game == 'y':
                    end = ed()
                    quit()
                elif exit_game == 'n' or exit_game == 'N':
                    print('<-------------------------------------->')
                    print('<  Game resumed, have fun guessing :)  >')
                    print('<-------------------------------------->')
                    guess_3 = str.capitalize(input('Please enter guess for position 3: '))
                    break
                else:
                    print('<-------------------------------------------------->')
                    print('< Invalid input, please choose between "Y" or "N"! >')
                    print('<-------------------------------------------------->')
                    continue

    guess_4 = str.capitalize(input('Please enter guess for position 4: '))
    while guess_4 == 'Exit':
        placeholder_4 = ''
        while placeholder_4 != 'cont':
            if guess_4 == 'Exit':
                exit_game = input('Are you sure to exit? [Y/N]: ')
                if exit_game == 'Y' or exit_game == 'y':
                    end = ed()
                    quit()
                elif exit_game == 'n' or exit_game == 'N':
                    print('<-------------------------------------->')
                    print('<  Game resumed, have fun guessing :)  >')
                    print('<-------------------------------------->')
                    guess_4 = str.capitalize(input('Please enter guess for position 4: '))
                    break
                else:
                    print('<-------------------------------------------------->')
                    print('< Invalid input, please choose between "Y" or "N"! >')
                    print('<-------------------------------------------------->')
                    continue
    print('')
    print('=============================================================')
    print('')
            
    #check user input for invalid inputs
    if guess_1 not in fruit_list or guess_2 not in fruit_list or guess_3 not in fruit_list or guess_4 not in fruit_list:
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print('/Invalid input detected, please make sure to input the correct fruit types (Apple, Orange, Grape or Banana)/')
        print('/                           Also take note to not enter extra spacing                                      /')
        print('////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print('')
        #restart input process if there exists any invalid inputs
        restart = True
    else:    
        #input user guess into list
        guess_list = [guess_1, guess_2, guess_3, guess_4]

        #print user guess
        print('')
        print('Your guesses:')
        print('[Position 1: ',   guess_list[0],  ' ]')
        print('[Position 2: ',   guess_list[1],  ' ]')
        print('[Position 3: ',   guess_list[2],  ' ]')
        print('[Position 4: ',   guess_list[3],  ' ]')
        print('')
        print('')

        #check user input with generated fruit list using two empty lists
        check_1 = []
        check_2 = []
        
        i = 0
        j = 0
        position_correct_type_corect = 0
        position_wrong_type_correct = 0

        for i in range(len(guess_list)):
            if guess_list[i] == fruit_list_random[i]:
                position_correct_type_corect = position_correct_type_corect + 1
            else:
                check_1.append(guess_list[i])
                check_2.append(fruit_list_random[i])
        while j < (len(check_1)):
            t = 0
            while t < (len(check_2)):
                if check_1[j] == check_2[t]:
                    check_2.pop(t)
                    position_wrong_type_correct = position_wrong_type_correct + 1
                    break 
                else:
                    t = t + 1
            j = j + 1
        
        #display hints based on player guess
        print('')
        print('Number of correct fruits in the correct position: ',position_correct_type_corect)
        print('Number of correct fruits in the wrong position: ',position_wrong_type_correct)
        
        #accumulator for attempt count, prompt player on their attempt count
        count = count + 1
        print('Attempts: ',count)
        print('')

        #check for winning condition, display winning message if conditions are met
        if position_correct_type_corect == 4 and position_wrong_type_correct == 0:
            print('****************************************')
            print('****************************************')
            print('**                                    **')
            print('** Congragulations! You got it right! **')
            print('**       You are the MASTERMIND       **')
            print('**       You took ',count,' attempts        **')
            print('**                                    **')
            print('****************************************')
            print('****************************************')
            print('')
            #ask if the player wants to play again or exit
            while True:
                again = input('Play again? [Y/N]: ')
                if again == 'y' or again == 'Y':
                    restart = True
                    fruit_list_random = [random.choice(fruit_list), random.choice(fruit_list), random.choice(fruit_list), random.choice(fruit_list)]
                    count = 0
                    break
                elif again == 'n' or again == 'N':
                    end = ed()
                    quit()
                else:
                    print('< Invalid input! Please choose between "Y" or "N"! >')
                    continue





    