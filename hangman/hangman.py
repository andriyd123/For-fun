import random 
import hangman_wordbank
import hangman_ascii

chosen_word = random.choice(hangman_wordbank.word_list)

placeholder = ""
for letter in range(len(chosen_word)):
    placeholder += "_ "

game_over = False

print("Welcome to Hangman! Please guess a letter:")
print(hangman_ascii.hangman_art[0] + "\n")
print(placeholder.rstrip() + "\n")

correct_letters = []

lives = 0
while not game_over:
    print(f"-------------------------------- LIVES LEFT: {6 - lives} --------------------------------")
    guess = input("Guess a letter: ").lower()
    print()

    if guess in correct_letters:
        print(f"You've already guessed: {guess}. Please try again.\n")
        continue
    
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter + " "
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter + " "
        else:
            display += "_ "
    
    if guess not in chosen_word:
        lives += 1
        print(f"You guessed: {guess}, thats not in the word. You lose a life.\n")
        if lives == 6:
            game_over = True
            print(f"You lose! The word was: {chosen_word}\n")

    print(hangman_ascii.hangman_art[lives] + "\n")
    print(display.rstrip() + "\n")

    if "_ " not in display:
        game_over = True
        print(f"You win! The word was: {chosen_word}\n")
