# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 12:01:38 2017

@author: lmanzhula
"""

annual_salary = int(input('Enter your annual salary:'))

portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))

total_cost = float(input('Enter the cost of your dream home:'))


current_savings = 0

portion_down = 0.25 * total_cost

r = 0.04

m = 0

while current_savings < portion_down: 
    current_savings += current_savings*r/12+(annual_salary/12)*portion_saved
    m += 1
    
print('Number of months:', m)