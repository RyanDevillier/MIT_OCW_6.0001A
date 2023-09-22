# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:36:08 2023

@author: devil
"""


############ Examples ############
# =============================================================================
# ## 1.) Function that finds roots
# def find_root(x, power, epsilon):
#     
#     # Find interval containing answer
#     if x < 0 and power%2 == 0:
#         return None # Negative number has no even-powered roots
#     low = min(-1, x)
#     high = max(1, x)
#     
#     # Use bisection search
#     ans = (high + low) / 2
#     while abs(ans**power - x) >= epsilon:
#         if ans**power < x:
#             low = ans
#         else:
#             high = ans
#         ans = (high + low) / 2
#     return ans
# 
# print(find_root(9, 2, 0.01))
# =============================================================================



# =============================================================================
# ## 2.) Keywords
# def print_name(first_name, last_name, reverse = False):
#     if reverse:
#         print(last_name + ', ' + first_name)
#     else:
#         print(first_name, last_name)
# 
# print_name('Ryan', 'Devillier')
# print_name('Ryan', 'Devillier', True)
# print_name('Ryan', 'Devillier', reverse = True)
# =============================================================================



# =============================================================================
# ## 3.) The unpacking operator, *, allows for a variable number of arguments to be passed into a function.
# def mean(*args):
#     # Assumes at least one argument exists and that all arguments are numbers
#     # Returns the mean of the arguments
#     total = 0
#     for a in args:
#         total += a
#     return total/len(args)
# 
# 
# print(mean(2,4))
# =============================================================================


# =============================================================================
# ## 4.) Scoping Part 1
# def f(x): # name x used as a formal parameter
#     y = 1
#     x = x + y
#     print('x =', x)
#     return x
# 
# x = 3
# y = 2
# z = f(x) # value of x used as actual parameter
# print(f'z = {z}')
# print(f'x = {x}')
# print(f'y = {y}')
# 
# =============================================================================

# =============================================================================
# ## 5.) Scoping Part 2
# def f(x):
#     def g():
#         x = 'abc'
#         print('x =', x)
#     def h():
#         z = x
#         print('z =', z)
#     x = x + 1
#     print('x =', x)
#     h()
#     g()
#     print('x =', x)
#     return g
# 
# x = 3
# z = f(x)
# print('x =', x)
# print('z =', z)
# z()
# =============================================================================



# =============================================================================
# ## 6.) Function that finds roots with a docstring
# def find_root(x, power, epsilon):
#     '''Assumes x and epsilon are ints or floats, power an int,
#             epsilon > 0, and power >= 1
#        Returns float y such that y**power is within epsilon of x.
#             If such a float does not exist, it returns None.'''
#     # Finding an interval containing answer
#     if x < 0 and power%2 == 0:
#         return None
#     low = min(-1, x)
#     high = max(1, x)
#     # Use bisection search
#     ans = (high + low) / 2
#     while abs(ans**power - x) >= epsilon:
#         if ans**power < x:
#             low = ans
#         else:
#             high = ans
#         ans = (high + low) / 2
#     return ans
# 
# print(find_root(-1, 3, 0.01))
# =============================================================================



# =============================================================================
# # 7.) Lecture example of function scopes
# def func_a():
#     print('inside func_a')
#     
# def func_b(y):
#     print('inside func_b')
#     return y
# 
# def func_c(z):
#     print('inside func_c')
#     return z()
# 
# print(func_a())
# print(5 + func_b(2))
# print(func_c(func_a))
# =============================================================================



# =============================================================================
# # 8.) Harder lecture example of function scopes (with nested functions)
# def g(x):
#     def h():
#         x = 'abc'
#     x = x + 1
#     print('g: x =', x)
#     h()
#     return x
# 
# x = 3
# z = g(x)
# =============================================================================







############ Finger Exercises for Chapter 4: ############ 
# =============================================================================
# 1.) Use the find_root function to print the sum of approximations to the square root 
# of 25, the cube root of -8, and the fourth root 0f 16.  Use 0.001 as epsilon.
# 
# print(f' Approximate sum of the square root of 25, cube root of -8, and fourth root of 16: \
# {find_root(25, 2, 0.01) + find_root(-8, 3, 0.01) + find_root(16, 4, 0.01)}')
# =============================================================================



# =============================================================================
# 2.) Write a function, is_in, that accepts two strings as arguments and returns True if either
#     string occurs anywhere in the other, and False otherwise.  Hint: you might want to use the
#     built-in str operator: in.
# 
# # Doesn't exactly do what the problem asked, but close enough.
# def shared_char(str1, str2):
#     letter_list = []
#     
#     for i in str1:
#         for j in str2:
#             if (i == j) and (i != ' '):
#                 letter_list.append(i)
#                 
#     lower_letters_list = [letter.lower() for letter in letter_list]
#     unique_letters = set(lower_letters_list)
#     print(f'There were {len(unique_letters)} shared characters between the two strings inputted.')
#     return unique_letters
# 
# sen1 = 'Bill'
# sen2 = 'Bob'
# print(shared_char(sen1, sen2))
# =============================================================================




# =============================================================================
# # 3.) Write a function, mult, that accepts either one or two ints as arguments.  If called
# # with two arguments, the function prints the product of the two arguments.  If called
# # with one argument, it prints that argument.
# 
# 
# def mult(int1, int2 = None): # int1 is a required positional argument, int2 is a preset default keyword argument
#     if int1 == None and int2 != None:
#         print(int2)
#     elif int1 != None and int2 == None:
#         print(int1)
#     else:
#         print(int1 * int2)
# 
# mult(2873, 2873)
# =============================================================================



# =============================================================================
# # 4.) Using bisection search, write a function that satisfies the specification
# # def log(x, base, epsilon):
# #    '''Assumes x and epsilon are ints or floats, base an int,
# #            x > 1, epsilon > 0, and power >= 1
# #      Returns float y such that base**y is within epsilon of x.'''
# 
# 
# def log(x, base, epsilon):
#     '''Assumes x and epsilon are ints or floats, base an int,
#          x > 1, epsilon > 0, and power >= 1
#        Returns float y such that base**y is within epsilon of x.'''
#     high = max(1, base)
#     low = min(-1, base)
#     ans = (high + low) / 2
#     while abs(base**ans - x) >= epsilon:
#         if base**ans < x:
#             low = ans
#         else:
#             high = ans
#         ans = (high + low) / 2
#     if abs(base**ans - x) >= epsilon:
#         print(f'Unable to find power within the upper bound {high} and lower bound {low}')
#     return ans
# 
# print(log(2, 80, 0.01))
# =============================================================================



# =============================================================================
# # 5.) Write a lambda expression that has two numeric parameters.  If the second argument equals zero,
# # it should return None.  Otherwise, it should return the value of dividing the first argument by
# # the second argument.  Hint: use a conditional expression.
# 
# lambda_func = lambda x,y: x/y if y != None else None
# print(lambda_func(10, 5))
# print(lambda_func(10, None))
# =============================================================================



# =============================================================================
# # 6.) Use find to implement a function staisfying the specification 
# # def find_last(s, sub):
# #     '''s and sub are non-empty strings
# #        Returns the index of the last occurrence of sub in s.
# #        Returns None if sub does not occur in s.'''
#        
# def find_last(s, sub):
#     '''s and sub are non-empty strings
#     Returns the index of the last occurrence of sub in s.
#     Returns None if sub does not occur in s.'''
# 
#     if sub in s:
#         return s.find(sub)
#     else:
#         return None
#     
# print(find_last('There is a grocery store down the block.', 'store'))
# print(find_last('There is a grocery store down the block.', 'zebra'))
# =============================================================================
