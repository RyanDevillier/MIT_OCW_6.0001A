# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 19:47:02 2023

@author: devil
"""


# =============================================================================
# # PART A - House Hunting
# 
# 
# # Initializing the variables defined by user input:
# annual_salary = float(input('Enter your starting annual salary: ')) # ANNUAL
# percent_saved = float(input('Enter the percent of your salary to save, as a decimal: ')) # PERCENTAGE APPLIED TO MONTHLY
# total_cost = float(input('Enter the cost of your dream home: ')) 
# 
# # Defining the down payment based on total cost:
# percent_down_payment = 0.25 * total_cost
# monthly_salary = annual_salary / 12 # MONTHLY
# 
# # Defining current savings (starts at $0):
# current_savings = 0.0
# 
# # Defining the annual return rate of the user's investments (as a decimal):
# r = 0.04
# 
# # Variable for how many months of saving for the down payment the user will have to wait:
# num_months = 0
# 
# # Determining the user's savings based on their investments and annual salary:
# while (current_savings < percent_down_payment):
#     current_savings = (current_savings + (current_savings * (r / 12))) + (monthly_salary * percent_saved)
#     num_months += 1
#     
# print(f'Number of months: {num_months}')
# =============================================================================




# =============================================================================
# # PART B - Saving, but with a Raise
# 
# 
# # Initializing the variables defined by user input:
# annual_salary = float(input('Enter your starting annual salary: ')) # ANNUAL
# percent_saved = float(input('Enter the percent of your salary to save, as a decimal: ')) # PERCENTAGE APPLIED TO MONTHLY
# total_cost = float(input('Enter the cost of your dream home: ')) 
# semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: ')) # PERCENTAGE APPLIED TO ANNUAL
# 
# # Defining the down payment based on total cost:
# down_payment = 0.25 * total_cost
# monthly_salary = annual_salary / 12 # MONTHLY
# 
# # Defining current savings (starts at $0):
# current_savings = 0.0
# 
# # Defining the annual return rate of the user's investments (as a decimal):
# r = 0.04
# 
# # Variable for how many months of saving for the down payment the user will have to wait:
# num_months = 0
# 
# # Determining the user's savings based on their investments and annual salary:
# while (current_savings < down_payment):
#     
#     current_savings = (current_savings + (current_savings * (r / 12))) + (monthly_salary * percent_saved)
#     num_months += 1
#     
#     if num_months % 6 == 0:
#         annual_salary = annual_salary + (semi_annual_raise * annual_salary)
#         monthly_salary = annual_salary / 12
# print(f'Number of months: {num_months}')
# =============================================================================




# PART C - Finding the Right Amount to Save Away

'''
GOAL: Annual Salary: $150,000
Savings Rate: 0.441
Steps: 12
'''


annual_salary = float(input('Enter your starting annual salary: ')) # ANNUAL
total_cost = 1000000 # total cost of house
semi_annual_raise = 0.07 # PERCENTAGE APPLIED TO ANNUAL
down_payment = 0.25 * total_cost # down payment on house
monthly_salary = annual_salary / 12 # MONTHLY
current_savings = 0.0
r = 0.04

# Bisection variables
num_months = 0
high = 1
low = 0
epsilon = 100
bisection_steps = 0
percent_saved = (high + low) / 2 # as a decimal 

# Determining the user's savings based on their investments and annual salary:
while abs(current_savings - down_payment) > epsilon:
    
    bisection_steps += 1
    num_months = 1
    current_savings = 0
    #current_savings = (current_savings + (current_savings * (r/12))) + (monthly_salary * percent_saved)

    print(f' --- OUTER (START) --- Month: {num_months},  High: {high}, Low: {low}, Percent Saved: {percent_saved}, Current Savings: {current_savings}, Down Payment: {down_payment}')
    
    while (num_months < 36):
        if num_months % 6 == 0:
            annual_salary = annual_salary + (semi_annual_raise * annual_salary)
            monthly_salary = annual_salary / 12
        current_savings = current_savings + (current_savings * (r/12)) + ((annual_salary / 12) * percent_saved)
        num_months += 1 
        print(f' --- INNER --- Month: {num_months},  High: {high}, Low: {low}, Percent Saved: {percent_saved}, Current Savings: {current_savings}, Down Payment: {down_payment}')

    if bisection_steps > 4:
        break
    if current_savings < down_payment:
        low = percent_saved
    elif current_savings >= down_payment:
        high = percent_saved
    percent_saved = (high + low) / 2
    print(f' --- OUTER (END) --- Month: {num_months},  High: {high}, Low: {low}, Percent Saved: {percent_saved}, Current Savings: {current_savings}, Down Payment: {down_payment}')

