import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scissors = [rock, paper, scissors]
#print(rock_paper_scissors[2])

your_choice =  int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
your_choice = rock_paper_scissors[your_choice]

print(your_choice)

computer_choice = random.choice(rock_paper_scissors)
print(f"Computer chose: {computer_choice}")

if your_choice == computer_choice:
    print("It's a draw")
elif your_choice == rock and computer_choice == scissors:
    print("You win")
elif your_choice == rock and computer_choice == paper:
    print("You lose")
elif your_choice == paper and computer_choice == rock:
    print("You win")
elif your_choice == paper and computer_choice == scissors:
    print("You lose")
elif your_choice == scissors and computer_choice == rock:
    print("You lose")
elif your_choice == scissors and computer_choice == paper:
    print("You win")
