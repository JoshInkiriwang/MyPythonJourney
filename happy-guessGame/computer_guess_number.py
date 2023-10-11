from random_number import randomizer, low_limit, high_limit

'''
Computer guessing a random number generated randomly and player will give clue).
The random number range is from 1 to 50.
Player can give a feedback on number   
'''

def computer_guessGame(): 
    com_random = randomizer(low_limit, high_limit)
    answer_num = randomizer(low_limit, high_limit)
    respon = []
    temp_low, temp_high = low_limit, high_limit
    print(f"ANSWER : {answer_num} \n")

    while(respon != "e") :
        respon = input(f"is {com_random} lower(L) OR greater(G) OR Equal(E) than/to answer ?").lower()
        print("");
    
        if respon == "l" : 
            temp_low = com_random
            com_random = randomizer(temp_low,temp_high)

        elif respon == "g" : 
            temp_high = com_random
            com_random = randomizer(temp_low,temp_high)

        elif respon == "e":
            if com_random != answer_num :
                print("Ha! You cheated \n")
                break
            elif com_random == answer_num:
                print("==== Congratulations! ==== \n")
                break
        else :
            print("Please enter valid response : L for Lower than, G for Greater than, E for Equal")
            continue