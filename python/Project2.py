#Name: Joseph Svintsitsky
#Module: Project 2
#Assignment: Find a plugin or module that you find useful 
#and implement it into a script in a unique and creative way.
#Due Date: 10/31/2021
#Resources: Coworker Matt West and https://cuny.manifoldapp.org/read/how-to-code-in-python-3/section/a07cdae8-713a-4c9a-adb1-63cf5b0006b5
 
import time
import random

# Open the text file storing the words to be randomly picked.
my_file = open("C:\it3038c-scripts\python\wordlist.txt","r")
options = my_file.readlines()
done = "n"

# This function declares if the end user guessed the correct word and prints Winner!
def winner():
    print("")
    print('Winner!', end=' ')

# This function determines the randomly chosen word an hides it until each word is fully guessed.
def guesser():
    word = random.choice((options))
    word = word.strip()
    
    #These variables control the total number of guesses/ hiding the word/ guesses used/ display letter chosen.
    num_guesses = 6
    hidden_word = '-' * len(word)
    guess = 1
    guessed_letters = ""

    # While loop runs condition of seeing if the letter guessed is in the hidden word of not.
    # If letter is incorrect it will notify end user letter guessed is incorrect.
    while guess <= num_guesses and '-' in hidden_word:
        print("Hidden word is:",hidden_word)
        print("")
        user_input = input('Enter a letter (Guess #%d): ' % guess).lower()
        if not user_input.isalpha():
            print("That's not a letter.")
            print("")
            time.sleep(1)
        elif user_input in guessed_letters:
            
            # Prints message when the same letter is entered multiple times.
            print("You already guessed that letter.")
            time.sleep(1)
            print("Letters Guessed:", guessed_letters)
            print("")
        elif user_input == word:
            break
        elif len(user_input) == 1:

            # Keeps list of guessed letters.
            guessed_letters += user_input
            print("Letters Guessed:", guessed_letters)

            # Count the number of times the character occurs in the word.
            num_occurrences = word.count(user_input)

            # Replace the appropriate positions in hidden_word with the actual character.
            position = -1
            for occurrence in range(num_occurrences):

                # Find the position of the next occurrence.
                position = word.find(user_input, position + 1)

                # Rebuild the hidden word string.
                hidden_word = hidden_word[:position] + user_input + hidden_word[position + 1:]

            # If letter guessed is incorrect add one guess used.
            if  user_input not in hidden_word:
                    guess += 1

        # Ensures only one character is entered per guess.
        elif len(user_input) != 1:
            print("Please enter one character at a time.")
            time.sleep(1)
    # If all blanks are missing end user has guessed the hidden word
    if not '-' in hidden_word or user_input == word:
        winner()

    # If blanks are still in hidden word end user ends up being a Loser!    
    else:
        print("")
        print('Loser!', end=' ')

    # Displays the hidden word
    print('The word was %s.' % word)
    time.sleep(2)

# Gives the end user an option to play again
while done != "y":
    guesser()
    print("\n")
    input("Press Enter to play again")
