# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:32:47 2023

@author: devil
"""


# AFTER 36 MONTHS, CALCULATE CURRENT SAVINGS
# DURING THE 36 MONTH PROCESS, CALCULATE THE PERCENT SAVED VIA INTEGER DIVISION BETWEEN 10000 and 0


'''
GOAL: Annual Salary: $150,000
Savings Rate: 0.441
Steps: 12
'''
# Fixed variables
down_payment = 250000

# Bisection variables
current_savings = 0
high = down_payment
low = 0
epsilon = 100
bisection_steps = 0

while abs(current_savings - down_payment) >= epsilon:
    
    bisection_steps += 1
       
    if current_savings < down_payment:
        low = current_savings
        
    elif current_savings >= down_payment:
        high = current_savings
        
    
    current_savings = (high + low) / 2
    print(f'High: {high}, Low: {low}, Current Savings: {current_savings}, Bisection Steps: {bisection_steps}')

    
  
    
  
    
  
    

