# Problem Set 2, hangman.py
# Name: Ryan Devillier
# Collaborators: Just me baabyyy
# Time spent: An unhealthy amount

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = r"C:\Users\devil\OneDrive\Desktop\MIT Courses\6.0001A - Introduction_To_Computer_Science_And_Programming_In_Python\Problem Sets\ps2\words.txt"


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
    print("  ", len(wordlist), "words loaded.\n")
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
secret_word = choose_word(wordlist)
print("TO BEGIN PLAYING THE NORMAL VERSION OF HANGMAN, TYPE INTO THE CONSOLE: hangman(secret_word)\nTO BEGIN PLAYING HANGMAN WITH HINTS, TYPE INTO THE CONSOLE: hangman_with_hints(secret_word)")

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    word_checker = True # checker for if a letter in letters_guessed is in secret_word -- initialized as True
    for i in secret_word:
        if i not in letters_guessed:
            word_checker = False
    
    if word_checker == False: 
        return False
    else:
        return True

    
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    display_letters = []
    for i in secret_word:
        if i not in letters_guessed:
            display_letters.append('_')
        else:
            display_letters.append(i)
    
    return ' '.join([str(j) for j in display_letters])
    

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = list(string.ascii_lowercase) # all lowercase English letters
    for i in letters_guessed:
        alphabet.remove(i)
    remaining_letters = ''.join(str(j) for j in alphabet)
    
    
    return remaining_letters
    
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
    num_guesses = 6
    letters_guessed = []
    print(f"\nIT'S HANGMAN TIME!!!! \nThe secret word is {len(secret_word)} letters long.") 
    while is_word_guessed(secret_word, letters_guessed) == False and num_guesses > 0:
        
        #print(f"TEST: {letters_guessed}")
        print(f"You have {num_guesses} guesses left. \nAvailable letters: {get_available_letters(letters_guessed)} \n__________________________________________")
        user_guess = str(input('Please guess a letter: '))
        alphabet = list(string.ascii_lowercase)
        
        if (user_guess in alphabet) and (user_guess not in letters_guessed): # Conditional for normal letter, not already guessed
            letters_guessed.append(user_guess)
            if user_guess in secret_word: # Conditional for good guesses
                print(f"Good guess! {get_guessed_word(secret_word, letters_guessed)}")
            else: # Conditional for bad guesses
                print(f"Nope! That letter is not in my word.\n{get_guessed_word(secret_word, letters_guessed)}")
                num_guesses = num_guesses - 1
            
        elif (user_guess not in alphabet):  # Conditional for symbols entered that are not in the alphabet
            if len(user_guess) > 1: # Conditional for if user enters more than one letter
                print("Have you not played Hangman before?  Only guess one letter at a time, dumbass.  Try again.")
                user_guess = str(input('Please guess a letter: '))
                num_guesses = num_guesses - 1
                if user_guess in alphabet:
                    letters_guessed.append(user_guess)
                else: # If the user repeatedly enters invalid inputs, game over.
                    print("Stop screwin' around.  Game over.")
                    break
            else: # Conditional for if the user enters anything that isn't a letter
                print("Have you not played Hangman before?  Only guess letters, dumbass.  Try again.")
                user_guess = str(input('Please guess a letter: '))
                num_guesses = num_guesses - 1
                if user_guess in alphabet:
                    letters_guessed.append(user_guess)
                else: # If the user repeatedly enters invalid inputs, game over.
                    print("Stop screwin' around.  Game over.")
                    break
                
        elif (user_guess in alphabet) and (user_guess in letters_guessed): # Conditional for normal letters that have already been guessed
            print(f"Oh my god.  You just guessed '{user_guess}'.  Try again.")
            print(f"Current guesses: {get_guessed_word(secret_word, letters_guessed)}")
            user_guess = str(input('Please guess a letter: '))
            num_guesses = num_guesses - 1
            if user_guess in letters_guessed:
                print("Stop screwin' around.  Game over.")
                break
            else:            
                letters_guessed.append(user_guess)
    
    if is_word_guessed(secret_word, letters_guessed) == True: # Conditional for when the user wins (by guessing all the letters)
        print(f"\nCONGRATULATIONS! You guessed the secret word! ({secret_word})\n\n ┏(･o･)┛♪┗ (･o･) ┓   ┏(･o･)┛♪┗ (･o･) ┓    ┏(･o･)┛♪┗ (･o･) ┓")
    
    if num_guesses == 0:
        print(f"GAME OVER.\nThe word was {secret_word}.")
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


# def match_with_gaps(my_word, other_word)
# def match_with_gaps(get_guessed_word(letters_guessed, secret_word), secret_word)
def match_with_gaps(letters_guessed, secret_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    match_checker_list = []
   
    if len(letters_guessed) != len(secret_word): # letters_guessed cannot match secret_word if their lengths differ
        return False
    
    for i in range(len(letters_guessed)):
        if letters_guessed[i] != secret_word[i]: # Are the letters equivalent?
            if letters_guessed[i] == "_": # If not, is it because letters_guessed is a blank?
                for j in letters_guessed: # Checking to see if letter is present in the rest of letters_guessed
                    if secret_word[i] == j: # If it is present, the words must not match, so break.
                        match_checker_list.append(False)
                        break
            else: # If letters_guessed is not a blank, the letters must not match...False
                match_checker_list.append(False)
                break
            
        
    if False in match_checker_list:
        return False
    else:
        return True


def show_possible_matches(letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    no_matches_list = [] # checker for matches
    for i in wordlist: # checking the words in wordlist for matches and then printing them
        if ' ' in letters_guessed: 
            letters_guessed = letters_guessed.replace(' ', '') # removing the whitespace in letters guessed
        elif match_with_gaps(letters_guessed, i) == True:
            print(i)
            no_matches_list.append(i)
    if len(no_matches_list) == 0: # list is empty, i.e., no matches found
        print("No matches found.")
                
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
    num_guesses = 6
    letters_guessed = []
    print(f"\nIT'S HANGMAN TIME!!!! \nThe secret word is {len(secret_word)} letters long.") 
    while is_word_guessed(secret_word, letters_guessed) == False and num_guesses > 0:
        
        #print(f"TEST: {letters_guessed}")
        print(f"You have {num_guesses} guesses left. \nAvailable letters: {get_available_letters(letters_guessed)} \n__________________________________________")
        user_guess = str(input('Please guess a letter: '))
        alphabet = list(string.ascii_lowercase)
        
        if (user_guess in alphabet) and (user_guess not in letters_guessed): # Conditional for normal letter, not already guessed
            letters_guessed.append(user_guess)
            if user_guess in secret_word: # Conditional for good guesses
                print(f"Good guess! {get_guessed_word(secret_word, letters_guessed)}")
            else: # Conditional for bad guesses
                print(f"Nope! That letter is not in my word.\n{get_guessed_word(secret_word, letters_guessed)}")
                num_guesses = num_guesses - 1
            
        elif (user_guess not in alphabet):  # Conditional for symbols entered that are not in the alphabet
            if user_guess == "*":
                print("--------------------------------\nPossible word matches are:")
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
                print('--------------------------------')
            elif len(user_guess) > 1: # Conditional for if user enters more than one letter
                print("Have you not played Hangman before?  Only guess one letter at a time, dumbass.  Try again.")
                user_guess = str(input('Please guess a letter: '))
                num_guesses = num_guesses - 1
                if user_guess in alphabet:
                    letters_guessed.append(user_guess)
                else: # If the user repeatedly enters invalid inputs, game over.
                    print("Stop screwin' around.  Game over.")
                    break
            else: # Conditional for if the user enters anything that isn't a letter
                print("Have you not played Hangman before?  Only guess letters, dumbass.  Try again.")
                user_guess = str(input('Please guess a letter: '))
                num_guesses = num_guesses - 1
                if user_guess in alphabet:
                    letters_guessed.append(user_guess)
                else: # If the user repeatedly enters invalid inputs, game over.
                    print("Stop screwin' around.  Game over.")
                    break
                
        elif (user_guess in alphabet) and (user_guess in letters_guessed): # Conditional for normal letters that have already been guessed
            print(f"Oh my god.  You just guessed '{user_guess}'.  Try again.")
            print(f"Current guesses: {get_guessed_word(secret_word, letters_guessed)}")
            num_guesses = num_guesses - 1
            print(f'You have {num_guesses} guesses left.')
            user_guess = str(input('Please guess a letter: '))
            if user_guess in letters_guessed:
                print("Stop screwin' around.  Game over.")
                break
            else:            
                letters_guessed.append(user_guess)
    
    if is_word_guessed(secret_word, letters_guessed) == True: # Conditional for when the user wins (by guessing all the letters)
        print(f"\nCONGRATULATIONS! You guessed the secret word! ({secret_word})\n\n ┏(･o･)┛♪┗ (･o･) ┓   ┏(･o･)┛♪┗ (･o･) ┓    ┏(･o･)┛♪┗ (･o･) ┓")
    
    if num_guesses == 0:
        print(f"GAME OVER.\nThe word was {secret_word}.")