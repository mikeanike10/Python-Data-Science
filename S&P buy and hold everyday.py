#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:15:06 2023

@author: Michael Glass
CS 677
Question 4
Using only positive return days calculate money gained with SPY and personal(GAB)
"""

x=linesGAB[0].split(",") #creates list to determine location of each value
w=x.index("Weekday") #index value for weekdays
r=x.index("Return") #index value for returns
y=x.index("Year") #index value for year
#index values are same for GAB and SPY
#1        
s=100
for i in range(1,len(linesGAB)):
    t=linesGAB[i].split(",")
    if eval(t[r])>0: 
        s=s+s*eval(t[r])
print("Money made is",s) #GAB $33820.81

#2
s=100
for i in range(1,len(linesSPY)):
    t=linesSPY[i].split(",")
    if eval(t[r])>0: 
        s=s+s*eval(t[r])
print("Money made is",s) #Spy $10486.89
