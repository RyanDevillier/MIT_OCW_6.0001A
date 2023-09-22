# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:52:23 2023

Revisited Sept 8 4:48:00 2023

@author: devil
"""

############ Examples ############
# def fact_iter(n):
#     '''
#     Assumes n an int > 0 (a natural number)
#     Returns n!
#     '''
#     result = 1
#     for i in range(1, n+1):
#         result = result * i
#     return result


# def fact_rec(n):
#     '''
#     Assumes n an int > 0 (a natural number)
#     Returns n!
#     '''
#     if n == 1:
#         return n
#     else:
#         return n * fact_rec(n - 1)


# def fib(n):
#     '''
#     Assumes n is an int > 0
#     Returns Fibonacci of n
#     '''
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# def test_fib(n):
#     for i in range(n+1):
#         print(f'fib of: {i} = {fib(i)}')



# def is_palindrome(word):
#     '''
#     Assumes word is a str
#     Returns True if letters in word form a palindrome;
#     False otherwise.  Non-letters and capitalization are ignored.
#     '''

#     def to_chars(word):
#         word = word.lower()
#         letters = ''
#         for char in word:
#             if char in 'abcdefghijklmnopqrstuvwxyz':
#                 letters = letters + char
#         return letters
    
#     def is_pal(word):
#         print(f'is_pal called with {word}')
#         if len(word) <= 1:
#             print(' About to return True from the base case')
#             return True
#         else:
#             answer = word[0] == word[-1] and is_pal(word[1:-1]) 
#             print(f' About to return {answer} for {word}')
#             return answer
    
#     return is_pal(to_chars(word))


# def fib(x):
#     '''
#     Assumes x is an int >= 0
#     Returns Fibonacci of x
#     '''
#     global num_fib_calls
#     num_fib_calls += 1
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return fib(x-1) + fib(x-2)
    
# def test_fib(n):
#     for i in range(n+1):
#         global num_fib_calls
#         num_fib_calls = 0
#         print(f'fib of {i} = {fib(i)}')
#         print(f'fib called {num_fib_calls} times.')




############ Finger Exercises ############
# Finger Exercise:  The harmonic sum of an integer, n > 0, can be calculated using the formula 1 + (1/2) + (1/3) + ... + (1/n).
# Write a recursive function that computes this.

# def harmonic_sum(n):
#     '''
#     Takes an int > 0 (n)
#     Returns the harmonic sum of that int: 1 + (1/2) + (1/3) + ... + (1/n)
#     '''
#     if n == 1:
#         return 1/n
#     else:
#         return (1/n) + harmonic_sum((n-1))
