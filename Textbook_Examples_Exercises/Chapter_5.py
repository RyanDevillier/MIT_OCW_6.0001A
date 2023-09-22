# -*- coding: utf-8 -*-
"""
Created on Sat May  6 19:04:39 2023

@author: devil
"""
#import copy
############ Examples ############
# 1.) 
# =============================================================================
# # # Doesn't work...min_val is always None (dumb)
# # def find_extreme_divisors(n1, n2):
# #     '''Assumes that n1 and n2 are positive ints
# #         Returns a tuple containing the smallest common divisor > 1 and
# #           the largest common divisor of n1 & n2.  If no common divisor,
# #           other than 1, returns (None, None)'''
# #     min_val, max_val = None, None
# #     for i in range(2, min(n1, n2) + 1):
# #         if (n1 % i == 0) and (n2 % i == 0):
# #             if min_val == None:
# #                 min_val == i
# #             max_val = i
# #     return min_val, max_val
#     
# # min_divisor, max_divisor = find_extreme_divisors(100, 200)
# # print(min_divisor, max_divisor)
# =============================================================================



# =============================================================================
# #2.) Mutability of lists
# # Techs = ['MIT', 'Caltech']
# # Ivys = ['Harvard', 'Yale', 'Brown']
# 
# # Univs = [Techs, Ivys]
# # Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
# 
# # Techs.append('RPI')
# 
# =============================================================================



#3.) List aliasing
# =============================================================================
# L1 = [[]] * 2
# L2 = [[], []]
# for i in range(len(L1)):
#     L1[i].append(i)
#     L2[i].append(i)
# print(f'L1 = {L1} but L2 = {L2}')
# =============================================================================

#4.) Part 2
# =============================================================================
# L = [1,2,3]
# L.append(L)
# print(L is L[-1])
# =============================================================================



#5.) Part 3
# =============================================================================
# def append_val(val, list_1 = []):
#     list_1.append(val)
#     print(list_1)
# 
# append_val(3)
# append_val(4)
# 
# =============================================================================


# =============================================================================
# #6.) List concatenation
# L1 = [1,2,3]
# L2 = [4,5,6]
# L3 = L1 + L2
# print(f'L3 = {L3}')
# 
# L1.extend(L2)
# print(f'L1 = {L1}')
# 
# L1.append(L2)
# print(f'L1 = {L1}')
# =============================================================================



# =============================================================================
# #7.) List Cloning (skips the 2nd item in L1 because we are mutating the first list whilst iterating through it.)
# def remove_dups(L1, L2):
#     '''Assumes that L1 and L2 are lists.
#        Removes any element from L1 that also occurs in L2.'''
#     for e1 in L1:
#         if e1 in L2:
#             L1.remove(e1)
# 
# L1 = [1,2,3,4]
# L2 = [1,2,5,6]
# remove_dups(L1, L2)
# print(f'L1 = {L1}')
# =============================================================================



# =============================================================================
# #8.) Shallow copy 
# L = [2]
# L1 = [L]
# L2 = L1[:]
# 
# L2 = L1.copy()
# L.append(3)
# print(f'L1 = {L1}, L2 = {L2}')
# 
# =============================================================================


# =============================================================================
# #9.) Deep copy
# L = [2]
# L1 = [L]
# L2 = L1[:]
# 
# L2 = copy.deepcopy(L1)
# L.append(3)
# print(f'L1 = {L1}, L2 = {L2}')
# =============================================================================



# =============================================================================
# #10.) List comprehension with two for loops
# L = [(x,y)
#      for x in range(6) if x%2 == 0
#      for y in range(6) if y%3 == 0]
# =============================================================================



# =============================================================================
# #11.) Nested list comprehension
# nested_comp = [[(x,y) for x in range(6) if x%2 == 0] for y in range(6) if y%3 == 0]
# print(f'Nested list comprehension: {nested_comp}') 
# =============================================================================



# =============================================================================
# #12.) Nested list comprehension to find the primes from 1 to 100
# nested_comp_primes = [x for x in range(2, 100) if all(x % y != 0 for y in range(3, x))]
# print(f'Primes from 1 to 100: {nested_comp_primes}')
# =============================================================================



# =============================================================================
# # #13.) Higher-order orperations on lists
# # def apply_to_each(L, f):
# #     '''Assumes L is a list, f is a function
# #        Mutates L by replacing each element, e, of L by f(e)'''
# #     for i in range(len(L)):
# #         L[i] = f(L[i])
# 
# # L = [1, -2, 3.33]
# # print(f'L = {L}')
# 
# # print(f'Apply abs to each element of {L}:')
# # apply_to_each(L, abs)
# # print(f'L = {L}')
# 
# # print(f'Apply int to each element of {L}:')
# # apply_to_each(L, int)
# # print(f'L = {L}')
# 
# # print(f'Squares each element of {L}:')
# # apply_to_each(L, lambda x: x**2)
# # print(f'L = {L}')
# =============================================================================



# =============================================================================
# #14.) The map function
# # print(list(map(str, range(10))))
# # print([str(e) for e in range(10)])
# =============================================================================



# =============================================================================
# #15.) Lecture example -- iterating over a nested tuple with a function
# def get_data(aTuple):
#     '''Accepts tuples of the form: ( (int, str), (int, str), ... , (int, str))
#     Returns min num, max num, and length of the list containing string(s)'''
#     nums = ()
#     words = ()
#     for t in aTuple:
#         nums = nums + (t[0],)
#         if t[1] not in words:
#             words = words + (t[1],)
#     min_n = min(nums)
#     max_n = max(nums)
#     unique_words = len(words)
#     return (min_n, max_n, unique_words)
# 
# (bob, dill, bobby) = get_data(((21, 'Ryan'), (24, 'Hailey'), (50, 'Paw')))
# =============================================================================



 



############ Finger Exercises for Chapter 5: ############ 
# =============================================================================
# # 1. ) Write an expression that evaluates to the mean of a tuple of numbers.  
# # Use the function sum.
# 
# # def tuple_mean(tuple1):
#     # avg = sum(tuple1) / len(tuple1)
#     # return avg
# =============================================================================



#2.) Write a list comprehension that generates all non-primes between 2 and 100.
# What



#3.) Implement a function satisfying the following specification.  Hint: it will be convenient
# to use lambda in the body of the implementation.
# =============================================================================
# def f(L1, L2):
#     '''L1, L2 are lists of numbers of the same length 
#     Returns the sum of raising each element in L1 to the
#     power of the element at the same index in L2.  
#     Example: f([1,2], [2,3]) returns 9.'''
#     
#     exp_list = list(map(lambda x,y: x**y, L1, L2))
#     for i in range(len(exp_list)):
#         return exp_list[i] + exp_list[i+1]
# =============================================================================
