# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 14:53:16 2017

@author: lmanzhula
"""

annual_salary = int(input('Enter your annual salary:'))

portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))

total_cost = float(input('Enter the cost of your dream home:'))

semi_annual_raise = float(input('Enter the semi­annual raise, as a decimal::'))


current_savings = 0

portion_down = 0.25 * total_cost

r = 0.04

m = 0

while current_savings < portion_down: 
    current_savings += current_savings*r/12+(annual_salary/12)*portion_saved
    m += 1
    if m%6 == 0: 
        annual_salary = annual_salary*(1+semi_annual_raise)
    
print('Number of months:', m)