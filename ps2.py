# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:43:39 2017

@author: lmanzhula
"""

# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    is_word = False
    for letter in letters_guessed:
        if letter not in secret_word:
            is_word = False
            break
        else: 
            is_word = True
    return is_word



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secret_word_list = list(secret_word)
    for i in range(len(secret_word_list)):
        if secret_word_list[i] not in letters_guessed:
            secret_word_list[i] = '_'
    secret_word_after_guessed = ''.join(secret_word_list)
    return secret_word_after_guessed


def get_available_letters(letters_guessed=[]):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    allletters_lowercase_list = list(string.ascii_lowercase)
    available_letters_list = allletters_lowercase_list[:]
    for i in range(len(allletters_lowercase_list)):
        if allletters_lowercase_list[i] in letters_guessed:
            available_letters_list.remove(allletters_lowercase_list[i])
    available_letters_string = ''.join(available_letters_list)
    return available_letters_string
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)


print('Welcome to the game Hangman!')
#game_word = choose_word(wordlist)
secret_word = "tact"
print("I am thinking of a word that is "+str(len(secret_word))+" letters long.")

letters_guessed = []
count_guesses = 6
warnings = 3
available_letter = get_available_letters()

letter_unique = ()
for l in list(secret_word):
    if l not in letter_unique:
        letter_unique = letter_unique + (l,)

print("You have "+str(warnings)+" warnings left.")


while count_guesses > 0:
    print("-------------")
    print("You have "+str(count_guesses)+" guesses left.")
    print("Available letters: "+str(available_letter))
    letter = str.lower(raw_input("Please guess a letter:"))
    if letter not in get_available_letters():
        warnings =- 1
        if warnings>=0:
            print("Oops! That is not a valid letter. You have"+str(warnings)+" warnings left:"+get_guessed_word(secret_word, letters_guessed))
        else:
            print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:"+get_guessed_word(secret_word, letters_guessed))
            count_guesses -= 1
    elif letter in letters_guessed:
        warnings =- 1
        if warnings>=0:
            print("Oops! You've already guessed that letter. You have "+str(warnings)+" warnings left:"+get_guessed_word(secret_word, letters_guessed))
        else:
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:"+get_guessed_word(secret_word, letters_guessed))
            count_guesses -= 1        
    else:
        letters_guessed.append(letter)
        if is_word_guessed(secret_word,letters_guessed):
            print("Good guess: "+get_guessed_word(secret_word, letters_guessed))
            if get_guessed_word(secret_word, letters_guessed) == secret_word:
                break
        else:
            print("Oops! That letter is not in my word:"+get_guessed_word(secret_word, letters_guessed))
            if letter in ['a', 'e', 'i' , 'o', 'u']:
                count_guesses -= 2
            else:
                count_guesses -= 1

total_score = count_guesses*len(letter_unique)

if get_guessed_word(secret_word, letters_guessed) == secret_word:
    print("Congratulations, you won!")
    print("Your total score for this game is: "+str(total_score))
