import random

words = ["apple", "tiger", "house", "plant", "chips"]

while True:  #  Outer loop for replay
    word = random.choice(words)
    #print("DEBUG WORD:",word )

    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    while wrong_guesses < max_wrong:
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_"
        print("\nWord:", display)

        print("Remaining guesses:", max_wrong - wrong_guesses)

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("Already guessed!")
        elif guess in word:
            print("Correct!")
            guessed_letters.append(guess)
        else:
            print("Wrong!")
            wrong_guesses += 1
            guessed_letters.append(guess)

        if all(letter in guessed_letters for letter in word):
            print("You won! The word was:", word)
            break

    if wrong_guesses == max_wrong:
        print("You lost! The word was:", word)

    #  Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing! ")
        break