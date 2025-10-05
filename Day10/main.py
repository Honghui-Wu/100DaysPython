import random
from art import logo
import sys

while True:
    play_or_not = input("Do you want to play a game of Blackjack? Type 'y' or 'n: ").lower()
    if play_or_not == 'y':
        print(logo)
        break
    elif play_or_not == 'n':
        sys.exit()
    else:
        print("Please type 'y' or 'n'.")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Computer's hand
computer_cards = random.choices(cards, k=2)

computer_current_score = sum(computer_cards)

while True:
    if computer_current_score <= 10:
        computer_cards.append(random.choice(cards))
    elif computer_current_score <= 16:
        if random.random() < 0.5:
            computer_cards.append(random.choice(cards))
        else:
            break
    else:
        break
    computer_current_score = sum(computer_cards)

print(computer_cards)
print(computer_current_score)


# Player's hand
your_cards = random.choices(cards, k=2)
current_score = sum(your_cards)
print(f"    Your cards: {your_cards}, current score: {current_score}")
print(f"    Computer's first card {computer_cards[0]}")

while True:
    if current_score >= 21:
        break

    get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if get_another_card == 'y':
        your_cards.append(random.choice(cards))
        current_score = sum(your_cards)
        print(f"    Your cards: {your_cards}, current score: {current_score}")

    if get_another_card == 'n':
        break


# Compare and print result
print(f"    Your final hand: {your_cards}, final score: {current_score}")
print(f"    Computer's final hand: {computer_cards}, final score: {computer_current_score}")

if current_score == 21:
    if computer_current_score == 21:
        print("It is a draw.")
    else:
        print("Blackjack! You win!")
elif current_score > 21:
    if computer_current_score > 21:
        print("It is a draw.")
    else:
        print("You went over. You lose.")
elif current_score < 21:
    if current_score == computer_current_score:
        print("It is a draw.")
    elif computer_current_score > 21:
        print("Opponent went over. You win!")
    elif current_score > computer_current_score:
        print("You win!")
    else:
        print("You lose.")



