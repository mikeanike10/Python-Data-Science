#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:24:31 2023

@author: Michael Glass
CS 677
Question 5
calculate final money return for holding day 1 of 2016 to final day of 2020
"""

#1
 s=100
 for i in range(1,len(linesGAB)):
     t=linesGAB[i].split(",")
     s=s+s*eval(t[r])
 print("Money made is",s) #GAB $205.28
 
 s=100
 for i in range(1,len(linesSPY)):
     t=linesSPY[i].split(",")
     s=s+s*eval(t[r])
 print("Money made is",s) #spy $197.96
 
 