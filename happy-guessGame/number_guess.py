from random_number import randomizer, low_limit, high_limit, max_attempts

'''
# Player guessing a random number generated randomly by computer)
# The random number range is from 1 to 10
'''
def numGame():
    attempt = 0
    answer_num = randomizer(low_limit, high_limit)

    while(attempt < max_attempts) :
        guess = int(input(f"Enter guess number between ({low_limit}-{high_limit}) : "))

        if guess == answer_num :
            print("==== Congratulations!  You guessed the number. ==== \n")
            break
        else :
            print(f'Attempt : {attempt + 1} / {max_attempts + 1}. Keep Guessing')
            if guess < answer_num :
                print(f"Hint : The answer is larger than {guess} \n")
            else : 
                print(f"Hint : The answer is lower than {guess} \n")
    else :
        print("Game Over. You've used all your attempts.")
        print(f"The answer was {answer_num}.")