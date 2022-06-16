""" 6 letter wordle game """

# correct letter correct place = 0
# correct letter wrong place = !
# letter not in word = x

import random


def check_guess(guess, word):
    """ checks the letters in the users word against the answer word """
    response = ""
    index = 0
    letters_list = ""
    for letter in guess:
        if letter == word[index]:
            response += "0"
        elif letter in word:
            if letter not in letters_list:
                response += "!"
            else:
                response += "x"
        else:
            response += "x"
        letters_list += letter
        index += 1
    return response


# reading from master txt doc and making a list of all potential words
six_letter_words = open("six_letter_words.txt", "r")
words_master = six_letter_words.read()
potential_words = words_master.split("\n")
six_letter_words.close()

# randomly selecting answer from possible answers
word = potential_words[random.randint(0, len(potential_words) - 1)]

# asking for a guess, 6 times
for guess in range(6):
    guess = input("What is your guess?\n")
    # checking the word is valid guess
    while guess not in potential_words:
        print("Sorry, that is not a valid guess, please try agian.")
        guess = input()
    # custom fuction which checks the guess word against answer word
    checked_guess = check_guess(guess.upper(), word.upper())
    print(f"{checked_guess}\n")
    if checked_guess == "000000":
        print("Congratulations, you got the correct word!")
        break

# if they didn't get the answer after six guesses
if checked_guess != "000000":
    print(f"Sorry, correct word was {word}")
