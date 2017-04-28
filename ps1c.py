# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 15:28:38 2017

@author: lmanzhula
"""

#annual_salary = int(input('Enter the starting salary:'))
annual_salary = 150000

portion_saved = 1

total_cost = 1000000

semi_annual_raise = 0.07


current_savings = 0

portion_down = 0.25 * total_cost

r = 0.04

m = 0


while m < 36: 
    current_savings += current_savings*r/12+(annual_salary/12)
    m += 1
    if m%6 == 0: 
        annual_salary = annual_salary*(1+semi_annual_raise)
        
if current_savings < total_cost:
        print('It is not possible to pay the down payment in three years')
else:
    portion_saved = 0.5
    while m < 36: 
        current_savings += current_savings*r/12+(annual_salary/12)*portion_saved
        m += 1
        if m%6 == 0: 
            annual_salary = annual_salary*(1+semi_annual_raise)
        
    
print('current_savings:', current_savings)