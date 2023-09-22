# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 13:58:57 2023

@author: devil
"""

# Examples
## 1.) #Figure 3-1 (Finding the integer cube root)
'''
# Find the cube root of a perfect cube
x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans += 1
if ans ** 3 != abs(x):
    print(x, 'is not a perfect cube.')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans)
'''



## 2.) Testing how large an integer the computer can quickly generate (starts to slow around 10,000,000)
'''
max_val = int(input('Enter a positive integer: '))
i = 0
while i < max_val:
    i += 1
print(i)
'''



## 3.) Using exhaustive enumeration to test primality
# Testing if an int > 2 is prime.  If not, print the smallest divisor
'''
x = int(input('Enter an integer greater than 2: '))
smallest_divisor = None
for guess in range(2, x):
    if x%guess == 0:
        smallest_divisor = guess
        break
if smallest_divisor != None:
    print('Smallest divisor of', x, 'is', smallest_divisor)
else:
    print(x, 'is a prime number.')
'''  



## 4.) A more efficient way to test for primality
# Testing if an int > 2 is prime.  If not, print smallest divisor
'''
x = int(input('Enter an integer greater than 2: '))
smallest_divisor = None
if x%2 == 0:
    smallest_divisor = 2
else:
    for guess in range(3, x, 2):
        if x%guess == 0:
            smallest_divisor = guess
            break
if smallest_divisor != None:
    print(f'Smallest divisor of x is {smallest_divisor}.')
else:
    print(f'{x} is a prime number.')
 '''   

  
 
## 5.) Approximating the square root using exhaustive enumeration
'''
x = float(input('Please enter an integer: '))
epsilon = 0.01
step = epsilon**2
num_guesses = 0
ans = 0.0

while abs(ans**2-x) >= epsilon and ans**2 <= x:
    ans += step
    num_guesses +=1
print('Number of guesses = ', num_guesses)

if abs(ans**2-x) >= epsilon:
    print('Failed on square root of', x)
else:
    print(ans, 'is close to the square root of', x)    
'''



## 6.) Approximating the square root using bisection search

'''
# Defining the variables for the input, max, min, answer, and epsilon interval
x = float(input('Please enter an integer: '))
epsilon = 0.01
num_guesses = 0
low = 0
high = max(1, x)
ans = (high + low) / 2
print(ans)

while abs(ans**2 - x) >= epsilon:
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
print(f'Number of guesses: {num_guesses}')
print(f'{ans} is close to the square root of {x}')
'''


## 7.) Using bisection search to estimate the log base 2
'''
# Defining initial variables
lower_bound = 0
epsilon = 0.00001
x = int(input('Please enter an integer: '))

# Finding the lower bound
while 2**lower_bound < x:
    lower_bound += 1
low = lower_bound - 1
high = lower_bound + 1

# Performing the bisection search
ans = (high + low) / 2
while abs(2**ans - x) >= epsilon:
    print(f'Low: {low}, High: {high}, Ans: {ans}')
    if 2**ans < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
print(f'{ans} is close to the log base 2 of {x}')
'''


## 8.) Understanding floats
'''
x = 0.0
for i in range(10):
    x = x + 0.1
    print(f'i: {i}, x: {x}')
if x == 1.0:
    print(x, '= 10')
else:
    print(x, 'is not 1.0')
'''


## 9.) Newton-Raphson Method for finding the square root
# Finding x such that x**2 - 24 is within epsilon of 0
'''
number = int(input('Enter a number: '))
epsilon = 0.01
guess = number/2
num_iterations = 0
while abs(guess**2 - number) >= epsilon:
    guess = guess - (((guess**2) - number) / (2*guess))
    num_iterations += 1
print(f'Approximation of square root: {guess}, Iterations: {num_iterations}')
'''

############ Finger Exercises for Chapter 3: ############ 
#1.) Refactoring the third example above to test for primality or generate the largest divisor of the given number 
'''
x = int(input('Enter an integer greater than 2: '))
smallest_divisor = None
for guess in range(2, x):
    if x%guess == 0:
        smallest_divisor = guess
        break
    
largest_divisor = int(x/smallest_divisor)

if smallest_divisor != None:
    print(f'The smallest divisor of x: {smallest_divisor}.  The largest divisor of x: {largest_divisor}')
else:
    print(x, 'is a prime number.')
'''



#2.) (Bottom of page 49)
'''Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 1 < pwr < 6
and root**pwr is equal to the integer entered by the user.  If no such pair of integers exists, it should print
a message to that effect.'''

'''
# Defining the variables
user_int = int(input('Please enter an integer: '))
base = 2
pwr = 2

# Iterating over all the bases (the base must be less than the square root of the int plus one)
# + 1 is to ensure we get the actual answer (since it's a while loop, the condition forces all values below the desired one)
while base < user_int**(1/2) + 1:
    
    # Iterating over all the powers that are worthy of checking
    while base**pwr < user_int + 1:
        
        # Printing the answer if we find a correct combination
        if base**pwr == abs(user_int):
            print(f'{base} to the {pwr} is equal to {user_int}')
        
        # Increasing the power by one
        pwr += 1
        
    # Resetting the power to 2 so that we can check each base from 2 onwards    
    pwr = 2
    
    print(f'No base-power combination yields {user_int} for the base {base}.')
    # Increasing the base by one to continue checking for pairs
    base += 1    
'''



#3.) (Top of page 56)
'''What would have to be changed to make the code in Figure 3-5 work for 
finding an approximation to the cube root of both negative and positive 
numbers?  Hint: think about changing 'low' to ensure that the answer lies
within the region being searched.'''

'''
# Defining the variables for the input, max, min, answer, and epsilon interval (fails for values between -1 and 1)
x = float(input('Please enter an integer: '))
epsilon = 0.01
num_guesses = 0
low = min(x, 1)
high = max(1, x)
approximation = (high + low) / 2

while abs(approximation**3 - x) >= epsilon:
    num_guesses += 1
    if approximation**3 < x:
        low = approximation
    else:
        high = approximation
    print(f'Answer: {approximation}, High: {high}, Low: {low}')
    approximation = (high + low) / 2
print(f'Number of guesses: {num_guesses}')
print(f'{approximation} is close to the cube root of {x}')
'''



# 4.) (Middle of page 56)
'''
The Empire State Building is 102 stories high.  A man wanted to know
the highest floor from which he could drop an egg without the egg breaking.
He proposed to drop an egg from the top floor.  If it broke, he would go down
a floor and try it again.  He would do this until the egg did not break.  At
worst, this method requires 102 eggs.  Implement a method that at worst uses 
seven eggs.
'''
# =============================================================================
# # Importing dependencies
# import math
# import random
# 
# # Initializing starter variables
# current_floor = int(input('Please enter a floor between 1 and 102: ')) 
# broken_floor = random.randint(1, 102)
# top_floor = 102 # high
# low_floor = 1 # low
# epsilon = 0.5 # within a floor of the answer
# eggs_used = 0
# 
# while abs(current_floor - broken_floor) > epsilon:
#     eggs_used += 1
#     print(f'Eggs Used: {eggs_used}, Current Floor: {current_floor}, Top: {top_floor}, Low: {low_floor}, Broken Floor: {broken_floor}')
#     if current_floor < broken_floor:
#         low_floor = current_floor
#         current_floor = math.floor((top_floor + low_floor) / 2)
#     else:
#         top_floor = current_floor
#         current_floor = math.floor((top_floor + low_floor) / 2)
# 
# print(f'Eggs Used: {eggs_used+1}, Current Floor: {current_floor}, Top: {top_floor}, Low: {low_floor}, Broken Floor: {broken_floor}')
# 
# =============================================================================

