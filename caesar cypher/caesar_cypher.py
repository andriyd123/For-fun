from art import logo

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print(logo)

def caesar(original_text, shift_amount, decode_or_encode):
    output_text = ""
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            position = alphabet.index(letter)
            if decode_or_encode == "decode":
                new_position = (position - shift_amount) % 26
            else:
                new_position = (position + shift_amount) % 26
            output_text += alphabet[new_position]
    print(f"The {decode_or_encode}d text is {output_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text, shift, direction)

    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if choice == "no":
        should_continue = False
        print("Goodbye!")
