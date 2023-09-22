# # Problem 2 scratch work
# test_dict = {'s': 1, 'o': 1, 'c': 3, 'k': 5}

# word = 'sock'

# letter_vals = []

# for letter in word:
#     if letter in test_dict:
#         letter_vals.append(test_dict[letter])

# print(sum(letter_vals))



# # Problem 3 scratch work [VERSION 1]
# test_word = 'sassy'
# test_dict = {'s': 3, 'a': 1, 'y': 1, 'b': 1}
# unique_letters = set()
# not_unique_letters = []
# for letter in test_word:
#     if letter not in unique_letters:
#         unique_letters.update(letter)
#     else:
#         not_unique_letters.append(letter)

# test_hand = {'s': 3, 'a': 1, 'y': 1, 'b': 1}

# test_word = 'convenient' # original word made from hand dealt
# sorted_test_word = ''.join(sorted(test_word)) # original word in alphabetical order
# duplicate_counter = 1 # number of times a letter appears in the original word
# duplicated_letters = set() # holds the unique letters in the original word that appear more than once
# num_of_duplicates = [] # holds the number of times a letter appears in the original word

# test_dict = dict()

# for index in range(1, len(sorted_test_word)): # iterating over each letter in the original word...
#     if sorted_test_word[index - 1] == sorted_test_word[index]: # and checking if there was a duplicated letter
#         duplicate_counter += 1 # if so, increase the counter by 1 
#         duplicated_letters.update(sorted_test_word[index]) # append the letter that appears more than once to the set
#     else:
#         num_of_duplicates.append(duplicate_counter) # append the number of times the letter appears in the list
#         duplicate_counter = 1

# test_dict[list(duplicated_letters)[0]] = max(num_of_duplicates)



# Problem 3 scratch work [VERSION 2] 
# TODO
# COMPLETE THE ENTIRE THIRD PROBLEM IN HERE
# REFACTOR THIS TO ACCOMODATE FOR WILDCARDS (PROBLEM 4)
test_hand = {'c': 1, 'k': 1, 'n': 3, 'v': 1, 'e': 2, 'i': 1, 't': 1}

test_word = 'convenient' # original word made from hand dealt
test_word = test_word.lower()

test_word_dict = dict()

validity_checker = []

for letter in test_word:
    if letter not in test_word_dict:
        test_word_dict[letter] = 1
    else:
        test_word_dict[letter] += 1

for letter in test_word_dict:
    if letter not in test_hand:
        print(f"Not a valid word.  {letter.upper()} is used in {test_word}, but {letter.upper()} is not in the dealt hand.")
        validity_checker.append(False)
        continue
    if test_word_dict[letter] > test_hand[letter]:
        print(f"Not a valid word.  {letter.upper()} is used {test_word_dict[letter]} times, but the dealt hand has only {test_hand[letter]} {letter.upper()}'s")
        validity_checker.append(False)
    else:
        validity_checker.append(True)

if False in validity_checker:
    print("LOL NO THIS DIDNT WORK HAHHAHHAHHA")
else:
    print('HOLY MOLY THAT IS A VERY VERY VERY VALID WORD')

print('asduashd')
