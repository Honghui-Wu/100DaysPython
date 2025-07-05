from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")


print(logo)
restart = True
ask_direction = True
ask_restart = True

while restart:

    while ask_direction:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == 'encode' or direction == 'decode':
            break
        else:
            print('Please type "encode" or "decode".')

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n")) 

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    while ask_restart:
        again = input('Type "Yes" if you want to go again. Otherwise type "No".').lower()
        if again == 'no':
            restart = False
            print("Good Bye.")
            break
        elif again == 'yes':
            break
        else:
            print('Please type "Yes" or "No".')
