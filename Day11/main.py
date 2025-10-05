import random
from art import logo


def initial_hand():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choices(cards, k=2)


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards)==2:
        return 0 # 0 for black jack    
    while sum(cards) > 21 and 11 in cards:
        idx= cards.index(11)
        cards[idx] = 1
    
    return sum(cards)


def check_black_jack(computer_cards, user_score, computer_score):
    '''If computer and user both have a black jack, computer wins.'''
    if computer_score == 0 and user_score == 0:      
        print("Both have Black Jack! House rule: Computer wins!")
        print(f"Computer cards: {computer_cards}")
        return True
    if computer_score == 0:
        print("Black Jack! Computer wins!")
        return True
    if user_score == 0:
        print("Black Jack! You win!")
        return True
    return False


def user_play(user_score, user_cards):
    if user_score > 21:
        return user_score, user_cards
    while True:
        get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if get_another_card == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f"    Your cards: {user_cards}, current score: {user_score}")
        elif get_another_card == 'n':
            return user_score, user_cards
        else:
            print("Please type 'y' or 'n'.")


def computer_play(computer_score, computer_cards):
    while True:
        if computer_score == 0 or computer_score >= 17:
            return computer_score, computer_cards
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


def compare(user_cards, user_score, computer_cards, computer_score):
    print(f"    Your cards: {user_cards}, current score: {user_score}")
    print(f"    Computer cards: {computer_cards}, computer score: {computer_score}")

    if user_score > 21:
        print("You went over. You lose.")
        return
    
    if computer_score > 21:
        print("Computer went over. You win!")
        return

    if user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("You lose.")
    else:
        print("It is a draw.")


def play_game():
    # Ask play game or not
    while True:
        play_or_not = input("Do you want to play a game of Blackjack? Type 'y' or 'n: ").lower()
        if play_or_not == 'y':
            print(logo)
            break
        elif play_or_not == 'n':
            print("Bye-bye!")
            return
        else:
            print("Please type 'y' or 'n'.")
    # User and Computer intitial hands
    user_cards = initial_hand()
    computer_cards = initial_hand() 
    # user_cards = [11, 10]
    # computer_cards = [11, 10]
    # print(user_cards)
    # print(computer_cards)
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    if check_black_jack(computer_cards, user_score, computer_score):
        return
    
    print(f"    Your cards: {user_cards}, current score: {user_score}")
    print(f"    Computer's first card {computer_cards[0]}")

    user_score, user_cards = user_play(user_score, user_cards)
    computer_score, computer_cards = computer_play(computer_score, computer_cards)


    compare(user_cards, user_score, computer_cards, computer_score)




play_game()
