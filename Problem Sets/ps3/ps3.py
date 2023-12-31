# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <Ryan Devillier>
# Collaborators : <Me and me only bruh>
# Time spent    : <'bout 5 minutes>

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.
    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 
	The score for a word is the product of two components:
	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played
	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.
    word: string
    n: int >= 0
    returns: int >= 0
    """

    # Converting the word to lowercase & appending all the letters values to a list
    letter_vals = []
    for letter in word.lower():
        if letter in SCRABBLE_LETTER_VALUES:
            letter_vals.append(SCRABBLE_LETTER_VALUES[letter])

    first_score = sum(letter_vals)  # Summing the letter values to get the first score component

    second_score = (7 * (len(word))) - (3 * (n - len(word))) # Calculating the second score component 
    if second_score < 0: # Accomodating for a negative second score component
        second_score = 1

    final_score = first_score * second_score

    return final_score



#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')        # print all on the same line
    print('(Current hand) ', end = '')
    print('')                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    if '*' not in hand:
        for letter in hand:
            if letter in VOWELS:
                letter = letter.replace(letter, '*')
                break

    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.
    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    new_hand = hand.copy() # copying the original hand to a new hand (so that the original hand is unchanged after picking a word)
    for letter in word.lower(): # Iterating through the letters in the picked word...
        if letter in new_hand.keys():
            new_hand[letter] -= 1 # and reducing the # of instances in the new hand of letters based on the word picked
            if new_hand[letter] < 0: # if the number of instances of a letter is already 0, keep it 0
                new_hand[letter] = 0

    return new_hand


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    validity_checker = [] # container that holds the checks to see if a letter is valid to be played based on the hand dealt (appends True if so, False if not)
    wildcard_checker = [] # container that holds the checks to see if replacing the wildcard with a vowel would yield a valid word (appends True if so, False if not)
    vowels = VOWELS.lower()
    word = word.lower()

    # Check if the word has a wildcard
    if "*" in word:
        wildcard_idx = word.find('*')
        for vowel in vowels:
            if word[0:wildcard_idx] + vowel + word[(wildcard_idx + 1): ] in word_list: # check if the word is valid when the wildcard is replaced with one of the vowels
                wildcard_checker.append(True)
                if len(set(word)) < len(list(word)): # checking if the word has duplicate letters

                    word_dict = dict()

                    for letter in word: # Creating a dict of the frequency of letters in our word
                        if letter not in word_dict: 
                            word_dict[letter] = 1 # make the number of letters one in the dictionary if the loop finds a new letter while iterating (there must be only one of this letter)
                        else:
                            word_dict[letter] += 1 # if the letter is in the word dictionary, then increase the value by one (there must be multiple of this letter)

                    for letter in word_dict: # Checking the letters in our dict to see if...
                        if letter not in hand: # they are in the dealt hand
                            validity_checker.append(False)
                            continue
                        if word_dict[letter] > hand[letter]: # if they've been used more than the hand has available to us
                            validity_checker.append(False)
                        else:
                            validity_checker.append(True)
                            
                else: # If there are no duplicated values...
                    for letter in word: 
                        if letter not in hand: # check if each letter is in the dealt hand
                            validity_checker.append(False)
                            continue
                        else:
                            validity_checker.append(True)  
            else: # If replacing the wildcard with a vowel does not produce a valid word...
                wildcard_checker.append(False)
            

        if True in wildcard_checker:
            return True
        elif False in wildcard_checker:
            return False


        if False in validity_checker:
            return False
        elif False not in validity_checker:
            return True
        
    if "*" not in word: # if there is no wildcard in our word...
        if word not in word_list: # is the word in the valid words list?
            return False
        else: # if the word is in the valid word list...
            if len(set(word)) < len(list(word)): # checking if the word has duplicate letters

                word_dict = dict()

                for letter in word: # Creating a dict of the frequency of letters in our word
                    if letter not in word_dict: 
                        word_dict[letter] = 1 # make the number of letters one in the dictionary if the loop finds a new letter while iterating (there must be only one of this letter)
                    else:
                        word_dict[letter] += 1 # if the letter is in the word dictionary, then increase the value by one (there must be multiple of this letter)

                for letter in word_dict: # Checking the letters in our dict to see if...
                    if letter not in hand: # they are in the dealt hand
                        validity_checker.append(False)
                        continue
                    if word_dict[letter] > hand[letter]: # if they've been used more than the hand has available to us
                        validity_checker.append(False)
                    else:
                        validity_checker.append(True)

            else: # If there are no duplicated values...
                for letter in word: 
                    if letter not in hand: 
                        validity_checker.append(False)
                        continue
                    else:
                        validity_checker.append(True) 

        if False in validity_checker:
            return False
        if False not in validity_checker:
            return True

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    letter_quantities = []
    for letter in hand:
        letter_quantities.append(hand[letter])

    no_of_letters = sum(letter_quantities)
    return no_of_letters

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    no_of_letters_in_hand = sum(hand.values())

    # Keep track of the total score
    total_score = 0

    # As long as there are still letters left in the hand:
    while no_of_letters_in_hand > 0:

        # Display the hand
        display_hand(hand)

        # Ask user for input
        user_guess = input(f'Enter word, or "!!" to indicate you are finished: ')

        # If the input is two exclamation points:
        if user_guess == '!!':

            break # End the game (break out of the loop)
            
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(user_guess, hand, word_list) == True:

                # Tell the user how many points the word earned,
                # and the updated total score
                word_score = get_word_score(user_guess, no_of_letters_in_hand)
                total_score = total_score + word_score
                print(f'"{user_guess}" earned {word_score} points.  Total: {total_score} points')

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
            elif is_valid_word(user_guess, hand, word_list) == False:
                print('That is not a valid word.  Please choose another word.')


            # update the user's hand by removing the letters of their inputted word & calculate the length of the hand
            hand = update_hand(hand, user_guess)

        no_of_letters_in_hand = calculate_handlen(hand)


    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    if user_guess != '!!':
        print(f'\nRan out of letters.  Total score for this hand: {total_score}')
    else:
        print(f'Total score for this hand: {total_score}')
    # Return the total score as result of function
    return total_score


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If the user provides a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    letter = letter.lower() # Make the letter lowercase
    if letter.lower() in hand: # if the letter is in the hand...
        new_letter = random.choice(list(SCRABBLE_LETTER_VALUES.keys())) # get a new letter randomly
        hand[new_letter] = hand[letter] # make it a key/value pair in the dictionary
        del hand[letter] # delete the original key/value pair in the dictionary

    return hand

       
    
def play_game(word_list, hand_size):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    # Initializing a variable to keep track of how many hands have been played
    hands_played = 1

    # Ask the user how many hands they want to play
    no_of_hands = input('Enter total number of hands: ')

    # List that keeps the scores for each hand
    scores_per_hand = []

    # List that stores if the user substituted a letter in one of the played hands
    substitute_list = []

    # List that holds each hand in a given game
    hand_list = []

    while hands_played <= int(no_of_hands): # if the number of hands played is less than the specified number of desired hands to play...

        # Deal the hand & put it in the hand list
        hand = deal_hand(hand_size)
        hand_list.append(hand)

        # Display the hand
        display_hand(hand)

        if True not in substitute_list: # If the user has not already substituted a letter in a hand... 

            # Ask if the user wants to subsitute a letter
            substitute = input('Do you want to substitute a letter in the hand?: ')
            print() # Newline to separate the prompts in the terminal

            if substitute.lower() == 'yes': # If they do want to replace a letter...
                # Make subtitute_checker True to prevent adding the user if they want to substitute again in a future hand
                substitute_checker = True
                substitute_list.append(substitute_checker)

                # Ask the user which letter they want to replace
                letter_to_sub = input('Which letter would you like to replace?: ')
                substitute_hand(hand, letter_to_sub)
                display_hand(hand) # Display the hand again after substituting a letter
            
        total_score = play_hand(hand, word_list) # Ask the user to input a word from the letters

        replay_hand = input('Would you like to replay the hand?: ') # Ask the user if they want to replay the previous hand
        if replay_hand.lower() == 'yes': # If they do want to replay the hand...
           
            display_hand(hand_list[-1]) # display the last hand that was played (a.k.a the last hand that was appended to the list)
            
            if True not in substitute_list: # If the user has not already substituted a letter in a hand... 

                # Ask if the user wants to subsitute a letter
                substitute = input('Do you want to substitute a letter in the hand?: ')
                print() # Newline to separate the prompts in the terminal

                if substitute.lower() == 'yes': # If they do want to replace a letter...
                    # Make subtitute_checker True to prevent adding the user if they want to substitute again in a future hand
                    substitute_checker = True
                    substitute_list.append(substitute_checker)

                    # Ask the user which letter they want to replace
                    letter_to_sub = input('Which letter would you like to replace?: ')
                    substitute_hand(hand, letter_to_sub)
                    display_hand(hand) # Display the hand again after substituting a letter
        
            total_score = play_hand(hand, word_list) # Ask the user to input a word from the letters

        scores_per_hand.append(total_score) # Put the hand's score in a list so that all the scores can be added up at the end of the game
        hands_played += 1 # increase hands_played by one
        
    final_score = sum(scores_per_hand)

    print('Game over, final score: ' + str(final_score))
    return final_score

    #TODO ask the user if they want to replay the previous hand 
    #TODO that means youll have to find a way to store the previous hand so that it can be recalled
    #TODO fuckin' ugh


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':

    import math
    import random
    import string

    VOWELS = 'aeiou*'
    CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
    HAND_SIZE = 7

    SCRABBLE_LETTER_VALUES = {
        '*': 0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }

    WORDLIST_FILENAME = r"C:\Users\devil\OneDrive\Desktop\MIT Courses\6.0001A - Introduction_To_Computer_Science_And_Programming_In_Python\MIT_OCW_6.0001A\Problem Sets\ps3\words.txt"
    word_list = load_words()
    
    play_game(word_list, HAND_SIZE)