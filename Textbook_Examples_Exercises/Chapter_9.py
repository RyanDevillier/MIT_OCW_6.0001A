# Created 9/11/23 
# rdevillier

# Textbook Examples
# # 1.) def get_ratios(vect1, vect2):
#     '''
#     Assumes: vect1 and vect2 are equal length lists of numbers.
#     Returns: a list containing the meaningful values of vect1[i]/vect2[i]
#     '''
#     ratios = []
#     for index in range(len(vect1)):
#         try: 
#             ratios.append(vect1[index] / vect2[index])
#         except ZeroDivisionError:
#             ratios.append(float('nan')) #nan = Not a Number
#         except:
#             raise ValueError('get_ratios called with bad arguments')
#
#     return ratios





# Finger Exercises:
#
# 1.) Implement a function that meets the specification below.  Use a try-except block.  Hint: before starting to code,
# you might want to type something like 1 + 'a' into the shell to see what kind of exception is raised.
# def sum_digits(s):
# ''' Assumes s is a string, returns the sum of the decimal digits of s.
#     For example, if s is 'a2b3c' it returns 5
# '''
#
# def sum_digits(str):
#     '''
#     Assumes str is a string
#     Returns the sum of the decimal digits of s
#     For example, if s is 'a2b3c', it returns 5.
#     '''
#
#     char_container = []    
#     for char in str:
#         char_container.append(char)
#   
#     num_container = []
#     for char in char_container:
#         try:
#             char = int(char)
#             num_container.append(char)
#         except ValueError:
#             print(f'{char} cannot be cast as an integer')
#    
#     sum_nums = sum(num_container)
#     return sum_nums
    

# 2.) Implement a function that statisfies the specification
# def find_an_even(list_of_ints):
#     '''
#     Assumes list_of_ints is a list of integers
#     Returns the first even number in L
#     Raises ValueError: if list_of_ints does not contain an even number
#     '''
#
# def find_an_even(list_of_ints):
#     '''
#     Assumes list_of_ints is a list of integers
#     Returns the first even number in L
#     Raises ValueError: if list_of_ints does not contain an even number
#     '''
#     check_list = []
#     for val in list_of_ints:
#         even_checker = False
#         if val % 2 == 0:
#             even_checker = True
#             check_list.append(even_checker)
#             return val
#   
#     if check_list == []:
#         raise ValueError('find_an_even was called with bad arguments')


print('asjdhgbasdhj')