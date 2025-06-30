import random
from hangman_art import stages, logo
from hangman_words import word_list


lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

display = ""
for position in range(len(chosen_word)):
    display += "_"
print(f"Word to guess {display}")


game_over = False
guessed_letter = set()

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in guessed_letter:
        print(f"\"{guess}\" is already guessed. Please enter a different letter.")
        guessed_letter.add(guess)
        continue
    guessed_letter.add(guess)


    # Replace "_" with the guessed letter if guess is correct
    display = list(display)
    i = 0
    for letter in chosen_word:
        if letter == guess:
            display[i] = letter
        i += 1       
    # make displace back into a string
    placeholder =  ''
    for char in display:
        placeholder += char
    display = placeholder
    print(f"Your guess {display}")

    

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************")
            print(f"The word to guess was \"{chosen_word}\"")

    if display == chosen_word:
        print("****************************YOU WIN****************************")
        game_over = True
        continue

    print(stages[lives])
