# -*- coding: utf-8 -*-

# Notes for Chapter 2:

### All objects have a type: scalar or non-scalar.  Scalars are indivisible (int, flaot, bool, None).
### Non-scalars are divisible and have some internal structure.

### f-strings have modifiers that can control the appearance of the output string
### f'{3.14159:.2f} evaluates to the string '3.14' b/c .2f truncates the string
### representation of a float to two digits after the decimal point.

### {:,.0f instructs Python to use commas as thousands separators}

import pandas as pd

# Examples from book:
    
# 1.)
'''m = int(input('Please input a value: '))   
if m % 2 == 0:
    print('Even')
else:
    print('Odd')
print('Done with conditional.')   
'''

# 2.)
'''x = 3
for j in range(x):
    print('Iteration of the outer loop.')
    for i in range(x):
        print('     Iteration of the inner loop.')
        x = 2
    
x = 1
for i in range(x):
    print(i)
    x = 4
'''

############ Finger Exercises for Chapter 2: ############ 
# 1.)
## (Bottom of Page 24)
'''Write a program that examines three variables - x, y, and z - and prints the
largest odd number among them.  If none of them are odd, it should print the
smallest value of the three.
'''

'''
### Defining x, y, and z
x = int(input("Value for x: "))
y = int(input("Value for y: "))
z = int(input("Value for z: "))

answer = min(x,y,z)
if x%2 != 0:
    answer = x
if y%2 != 0 and y > answer:
    answer = y
if z%2 !=0 and z > answer:
    answer = z
print(answer)
'''



#2.)
## (Top of Page 32)
'''Write code that asks the user to enter their birthday in the form mm/dd/yyyy 
and then prints a string of the form 'You were born in the year yyyy.'
'''

'''
# Defining the birthdate variable
birthdate = input('Enter your birthdate (mm/dd/yyyy): ')

# Displaying the year the user was born via slicing the inputted birthdate
print(f'You were born in the year {birthdate[6:]}.')

'''



#3.)
## (Top of Page 36)
'''Replace the comment in the following code with a while loop.
num_x = int(input('How many times should I print the letter X? '))
to_print = ''
#concatenate X to to_print num_x times
print(to_print)
'''

'''
# Asks the user for how many Xs
num_x = str(input('How many times should I print the letter X? '))
to_print = ''
iterations = 0

# Iterates using inputted value
while (iterations < int(num_x)):
    to_print = to_print + 'X'
    iterations += 1
    
# Prints the number of Xs the user desired
print(to_print)
'''



#4.)
## (Bottom of Page 36)
'''Write a program that asks the user to input 10 integers, and then prints
the largest odd number that was entered.  If no odd number was entered, it
should print a message to that effect.
'''

'''
# Defining lists that hold the inputted integers,
# the inputted odd integers, and the odd checker
integers = []
odd_integers = []
checker_list = []
odd_checker = True

# Creating for loop that asks the user to input integers
for i in range(0, 10):
    user_int = int(input('Please enter an integer: '))
    integers.append(user_int)
    if (user_int % 2) != 0:
        odd_checker = False
        checker_list.append(odd_checker)
        odd_integers.append(user_int)
 
# Displays the largest odd integer or that there were no odd integers inputted
if len(checker_list) > 0:
    print(f'{max(odd_integers)} is the largest odd number')
else:
    print('There were no odd integers inputted.')
'''


 
#5.)
## (Bottom of Page 40)
'''
Write a program that prints the sum of the prime numbers greater than 2 and less than 1000.
Hint: you probably want to use a for loop that is a primality test nested inside a for loop
that iterates over the odd integers between 3 and 999.
'''
'''
# All primes must end in 1, 3, 7, or 9 (0, 2, 4, 5, 6, 8 are all divisible by either 2 or 5)
possible_primes = []

# Iterating over the odd numbers and keeping only the numbers ending in 1, 3, 7, or 9
for i in range(3, 1000, 2):
    string_i = str(i)
    if (int(string_i[-1]) != 5):
        possible_primes.append(i)
        
# The numbers we want to generate primes within is bounded by the square root of 1000.
# i.e., we care about all numbers that are not divisible by 1-31.

primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31] + [i for i in possible_primes if (i % 3 != 0 and i % 7 != 0 and i % 11 != 0 and i % 13 != 0 and i % 17 != 0 and i % 19 != 0 and i % 23 != 0 and i % 27 != 0 and i % 29 != 0 and i % 31 != 0)]
print(primes)

# Iterating to add the primes together
counter = 0
total = 0
while counter < len(primes) - 1:
    total = total + primes[counter]
    counter += 1
print(total)
'''