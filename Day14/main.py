##TODO 1: Print logo

##TODO 2: Get options A and B from the game data to compare.
##TODO 2.1: Generate a random integer, from 0 to len(data - 1), use random.randrange( len(data) )
##TODO 2.2 Use those random integers to obtain the dictionary of the options A and B, respectively. Assign to dict_A, and dict_B
##TODO 2.3 Print the "name", "description", and "country" of the options for users.

#TODO 3: Get user input.

#TODO 4: Compare the follower count of each option.
#TODO 4.1: If the user is correct, let the user's choice be option A. Score + 1. Get option B using the method in TODO 2.
#TODO 4.2: If the user is wrong, print final score.

from random import randrange
import art
from game_data import data


def get_options():
    idx_A = 0
    idx_B = 0
    # avoid getting the same index
    while idx_A == idx_B:
        idx_A = randrange(len(data))
        idx_B = randrange(len(data))

    # Get the dictionary for A and B, respectively
    dict_A = data[ idx_A ]
    dict_B = data[ idx_B ]
    return dict_A, dict_B


def get_guess(dict_A, dict_B):
    print(f"Compare A: {dict_A['name']}, a {dict_A['description']}, from {dict_A['country']}.")
    print(art.vs)
    print(f"Against B: {dict_B['name']}, a {dict_B['description']}, from {dict_B['country']}.")
    while True:
        guess = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
        if guess == 'A':
            dict_guess = dict_A
            dict_compare = dict_B
            break
        elif guess == 'B':
            dict_guess = dict_B
            dict_compare = dict_A
            break
        else:
            print("Please type 'A' or 'B'.")
    return dict_guess, dict_compare


# def check_answer(dict_guess, dict_compare, score):
#     if dict_guess['follower_count'] >= dict_compare['follower_count']:
#         score += 1
#         print(f"You are right! Current score: {score}.")
#         return True
#     else:
#         print(f"Sorry, that's wrong. Final score: {score}")
#         return False
    
        
    
def game():

    run_game = True
    score = 0

    print(art.logo)

    dict_A, dict_B = get_options()
    print("dict_A:\n", dict_A)
    print("dict_B:\n", dict_B)
    while run_game:        
        dict_guess, dict_compare = get_guess(dict_A, dict_B)    
        print("dict_guess:\n", dict_guess)
        print("dict_compare:\n", dict_compare)

        if dict_guess['follower_count'] >= dict_compare['follower_count']:
            score += 1
            print(f"You are right! Current score: {score}.")
            dict_A = dict_guess
            _ , dict_B = get_options()
            print("dict_A:\n", dict_A)
            print("dict_B:\n", dict_B)
            run_game = True
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            run_game = False

    
    
    # while run_game:
               
    #     run_game = check_answer(dict_guess, dict_compare, score)
    #     dict_A, _ = get_options()
    #     dict_B = dict_guess
        
    #     dict_guess, dict_compare = get_guess(dict_A, dict_B)

    #     print(dict_guess)
    #     print(dict_compare)
        
game()