import random
from number_guess import numGame
from colour_guess import colourGame
from computer_guess_number import computer_guessGame as comGuessGame
from rock_paper_scissors import rpsGame
from options import change_username as changeUsername, exit_game as exitGame, read_file, write_file

# Define the menu options as a dictionary
menu_options = {
    '1': numGame,
    '2': colourGame,
    '3': comGuessGame,
    '4': rpsGame,
    '5': changeUsername,
    '6': exitGame
}

# Open the file for reading and writing
# Player name - if a name is in the file, take the name from the file
while True:
    username = read_file()
    if not username: 
        username="Player"
        writeFile(username)

    print(f'==== Welcome {username} ====')
    print('Menu : ')
    print('1. Number Guess')
    print('2. Colour Guess')
    print('3. Computer Guess Number')
    print('4. Rock Paper Scissor')
    print('5. Options')
    print('6. Exit Game')

    choice = input('Enter your choice: ').strip()

    if choice in menu_options :
        menu_options[choice]()
    else :
        print('Invalid choice. Please select a valid option. \n')