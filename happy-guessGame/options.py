import os

def write_file(context) :
    with open("myfile.txt", "w") as writeFile:
        writeFile.write(context)

def read_file():
    with open("myfile.txt", "r") as readFile:
        username = readFile.read()
    return username

'''
Player can change username and it modify context inside myfile.txt    
'''
def change_username():
    username = read_file()
    print(f'Your current name is {username}')
    username = input("Please insert your new name: ")
    write_file(username)
    print("Your new name is", username, "\n")

def exit_game():
    print("==== Exiting Game ====")
    os.system('cls')
    exit()