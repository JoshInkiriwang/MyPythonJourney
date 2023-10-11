import random
from random_number import max_attempts, low_limit

'''
Player guessing a random colour name, generated randomly by computer)
The random colour name is preset by this list :
    ('Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Black', 'Brown', 'White')
'''
def colourGame():
    colors = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Black', 'Brown', 'White']
    answer_colour = random.choice(colors)
    attempts = low_limit

    while attempts < max_attempts:
        guess = input("Enter a color guess: ").strip().capitalize()
        
        if guess == answer_colour:
            print("Congratulations! You guessed the color. \n")
            break
        else:
            print("Keep guessing.")
            print(f"Hint: The color starts with '{answer_colour[0]}' and has {len(answer_colour)} letters. \n")
        
        attempts += 1
    else:
        print("Game Over. You've used all your attempts.")
        print(f"The answer was {answer_colour}.")
