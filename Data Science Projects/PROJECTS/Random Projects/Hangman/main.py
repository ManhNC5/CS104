import random

def choose_word():
    # Choose a random word from a list of words
    words = ["apple", "banana", "orange", "strawberry", "grape"]
    return random.choice(words)

def play_hangman():
    word = choose_word()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()
    tries = 5

    print("Hangman Game")
    print("You have {} tries to guess the word".format(tries))

    while tries > 0:
        # Display the current state of the game
        print("You have used the following letters:", ' '.join(used_letters))
        print("Word:", ' '.join([letter if letter in used_letters else '_' for letter in word]))

        # Get the player's next guess
        guess = input("Enter a letter: ").lower()
        if guess in alphabet - used_letters:
        used_letters.add(guess)
        if guess in word_letters:
            print("Correct!")
            if set(word_letters) == used_letters:
                print("You win!")
                print("The word was", word)
        
        else:
            print("Incorrect!")
            tries -= 1
        elif guess in used_letters:
            print("You have already used that letter.")
        else:
            print("Invalid input. Enter a letter.")

    print("You lose!")
    print("The word was", word)

if __name__ == "__main__":
    play_hangman()
