# TODO 1: Print greetings

# TODO 2: Get input to decide "Hard" or "Easy" model. Decide number of turns accordingly.

# TODO 3: Randomly generate the number to guess: num_to_guess.

# TODO 4: Get input, num_guessed.
# TODO 5: Compare the numbers. If too high or too low, print it, and attempts - 1. If num_guessed = num_to_guess, print "You got it. The number was num_to_guess".
# TODO 6: When run out of attempt. print "You've run out of guesses. Refresh the page to run again.".

import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def greetings():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100. See if you can guess it!")


def set_mode():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        if difficulty == 'easy':
            print(f"You have {EASY_LEVEL_TURNS} attempts to guess the number.")
            return EASY_LEVEL_TURNS
        elif difficulty == 'hard':
            print(f"You have {HARD_LEVEL_TURNS} attempts to guess the number.")
            return HARD_LEVEL_TURNS
        else:
            print("Please type 'easy' or 'hard.")
        

def check_answer(guess, answer, turns):
    if guess == answer:
        print(f"You got it! The number was {answer}.")
        return -1
    elif guess > answer:
        print("Too high.")     
        return turns - 1
    else:
        print("Too low.")
        return turns - 1


def game():
    greetings()

    turns = set_mode()

    answer = random.randint(1,100)
    #print("answer", answer)

    while turns > 0:
        raw = input("Make a guess: ").strip()
        if not raw.isdigit():
            print("Please enter an integer between 1 and 100.")
            continue
        guess = int(raw)

        turns = check_answer(guess, answer, turns)
        
        if turns == 0: 
            print("You've run out of guesses. Rerun the code to play again.")
        elif turns == -1:
            break
        else:
            print("Guess again.")
            print(f"You have {turns} attempts remaining to guess the number.")
        
           
game()
