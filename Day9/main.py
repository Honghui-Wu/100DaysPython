# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)

ask_bid = True
bids = {}
while ask_bid:
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    bids[name] = bid

    ask_another = True
    while ask_another:
        another = input("Are there any other bidder? Type 'yes' or 'no'").lower()
        if another == 'yes':
            ask_another = False
            print("\n" * 100)
        elif another == 'no':
            ask_bid = False
            ask_another = False
            print("\n" * 100)
        else:
            print("Please type 'yes' or 'no'")

#print(bids)

is_are = " is"

winner = ''
winning_price = 0
for key in bids:
    if bids[key] > winning_price:
        winner = key
        winning_price = bids[key]
    elif bids[key] == winning_price:
        winner += " and " + key
        is_are = "s are"

print(f"The winner{is_are} {winner} with a bid of ${winning_price:.2f}.")

