import random
from words import words #import the list from the file
#step 1 - the computer figures out a word to guess - randomly select a word
#some words are invalid - create a function to find a valid word
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list and sets it to the variable word
    while '-' in word or ' ' in word: #loops through until 
        word = random.choice(words)

    return word #returns valid word


def hangman():
    #assign necessary variables
    word = get_valid_word(words) #gets a valid word from the get_valid_word function
    word_letters = set(word) #creates a set for the different types of unique letters. When this set has length 0, the user has found the word
    alphabet = set(string.ascii_lowercase) #create a set of the lowercase alphabet
    used_letters = set() #the letters that the user has guessed
    word_list = [] #create an empty set. Letters not guessed will be displayed as "-" to the user
    lives = 6 #set the number of lives to 6
    while lives > 0 and len(word_letters)> 0: #while statement - keeps user in a loop until they die, or they solve the word
        print('You have', lives, 'lives left and you have used these letters: ', ' ' .join(used_letters)) #display lives and letters used
        #loop that will display the hidden word, with guessed letters
        for i in word:
            if i in used_letters:
                word_list.append(i)
            else:
                word_list.append("- ")
        print('Current word: ', ' '.join(word_list)) #display hidden word with guessed letters
        user_input_letter = input("Guess a letter: ").lower() #user input
        print("")
        if user_input_letter in alphabet: #check if letter is a valid letter in the alphabet
            if user_input_letter in used_letters: #check if the letter has been used already
                print("You have used that letter, try again ")
                print ("")
            else:
                if user_input_letter in word_letters: #check if the letter is in the word
                    used_letters.add(user_input_letter) #add to the set of used letters
                    word_letters.remove(user_input_letter) #remove the unique letter they guessed
                else:
                    print ("Incorrect choice. Try again.")
                    print ("")
                    lives = lives - 1
        else:
            print ("Invalid choice, try again")
            print ("")
    if lives == 0:
            print("You have died")
    else:
        print("Congratulations, you have won the game! The word was", word)


hangman()

