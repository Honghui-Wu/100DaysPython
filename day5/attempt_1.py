from random import randrange
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


'''Easy Version'''
password_list = []
for _ in range(nr_letters):
    random_letter = letters[randrange( len(letters) )]
    password_list.append(random_letter)

for _ in range(nr_symbols):
    random_symbol = symbols[randrange( len(symbols) )]
    password_list.append(random_symbol)

for _ in range(nr_numbers):
    random_number = numbers[ randrange( len(numbers) )]
    password_list.append(random_number)

password = ''
for character in password_list:
    password += character

print(password)

'''Hard Version'''
password = ''
for _ in range(len(password_list)):
    character = random.choice(password_list)
    password += character
    password_list.remove(character)
print(password)
