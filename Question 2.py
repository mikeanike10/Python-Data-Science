#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 22:38:40 2023

@author: Michael Glass
cs 677
question 2
using training data from year 1,2,3 to predict values in year 4,5
"""

#part 1
#gab
Ltrain=df_GAB["True Label"].where((df_GAB["Year"]==2016) | (df_GAB["Year"]==2017) | (df_GAB["Year"]==2018) ).dropna().values.tolist()
Ltest=df_GAB["True Label"].where((df_GAB["Year"]==2019) | (df_GAB["Year"]==2020) ).dropna().values.tolist()
for i in range(753,750,-1): #adds days for first index of test data
    Ltest.insert(0,Ltrain[i])

#w=2
pred2G=[] #list of pred w=2 labels
for i in range(3,len(Ltest)): #first i is index 2
    m=0 #count of matching sequence with + after
    n=0 #count of matching sequence with - after
    for j in range(len(Ltrain)-2): #reduced by two to keep in bounds of available sequence length
        if Ltrain[j]==Ltest[i-1]:
            if Ltrain[j+1]==Ltest[i]:
                if Ltrain[j+2]=='+':
                    m+=1
                elif Ltrain[j+2]=='-':
                    n+=1
    if m/(m+n) > 0.5:
        pred2G.append("+")
    elif m/(m+n)<0.5:
        pred2G.append("-")
    else:
        pred2G.append("+") #p* is 61%


#W=3
pred3G=[]
for i in range(3,len(Ltest)): #first i is index 2
    m=0 #count of matching sequence with + after
    n=0 #count of matching sequence with - after
    for j in range(len(Ltrain)-3):
        if Ltrain[j]==Ltest[i-2]:
            if Ltrain[j+1]==Ltest[i-1]:
                if Ltrain[j+2]==Ltest[i]:
                    if Ltrain[j+3]=='+':
                        m+=1
                    elif Ltrain[j+3]=='-':
                        n+=1
    if m/(m+n) > 0.5:
        pred3G.append("+")
    elif m/(m+n)<0.5:
        pred3G.append("-")
    else:
        pred3G.append("+") #p* is 61%
     
#w=4
pred4G=[]
for i in range(3,len(Ltest)): #first i is index 3
    m=0 #count of matching sequence with + after
    n=0 #count of matching sequence with - after
    for j in range(len(Ltrain)-4):
        if Ltrain[j]==Ltest[i-3]:
            if Ltrain[j+1]==Ltest[i-1]:
                if Ltrain[j+2]==Ltest[i-2]:
                    if Ltrain[j+3]==Ltest[i]:
                        if Ltrain[j+4]=='+':
                            m+=1
                        elif Ltrain[j+4]=='-':
                            n+=1
    if m/(m+n) > 0.5:
        pred4G.append("+")
    elif m/(m+n)<0.5:
        pred4G.append("-")
    else:
        pred4G.append("+") #p* is 61%   
      
#for spy
Ltrain=df_SPY["True Label"].where((df_SPY["Year"]==2016) | (df_SPY["Year"]==2017) | (df_SPY["Year"]==2018) ).dropna().values.tolist()
Ltest=df_SPY["True Label"].where((df_SPY["Year"]==2019) | (df_SPY["Year"]==2020) ).dropna().values.tolist()
for i in range(753,750,-1):#adds values for sequencing first value of test data
    Ltest.insert(0,Ltrain[i])
#w=2
pred2S=[]
for i in range(3,len(Ltest)): #first i is index 3
    m=0 #count of matching sequence with + after
    n=0 #count of matching sequence with - after
    for j in range(len(Ltrain)-2):
        if Ltrain[j]==Ltest[i-1]:
            if Ltrain[j+1]==Ltest[i]:
                if Ltrain[j+2]=='+':
                    m+=1
                elif Ltrain[j+2]=='-':
                    n+=1
    if m/(m+n) > 0.5:
        pred2S.append("+")
    elif m/(m+n)<0.5:
        pred2S.append("-")
    else:
        pred2S.append("+") #p* is 55%

        
#w=3
pred3S=[]
for i in range(3,len(Ltest)): #first i is index 2
    m=0 #count of matching sequence with + after
    n=0 #count of matching sequence with - after
    for j in range(len(Ltrain)-3):
        if Ltrain[j]==Ltest[i-2]:
            if Ltrain[j+1]==Ltest[i-1]:
                if Ltrain[j+2]==Ltest[i]:
                    if Ltrain[j+3]=='+':
                        m+=1
                    elif Ltrain[j+3]=='-':
                        n+=1
    if m/(m+n) > 0.5:
        pred3S.append("+")
    elif m/(m+n)<0.5:
        pred3S.append("-")
    else:
        pred3S.append("+") #p* is 61%

#W=4
pred4S=[]
for i in range(3,len(Ltest)): #first i is index 2
    m=0 #count of matching sequence with + after
    n=0 #count of matching sequence with - after
    for j in range(len(Ltrain)-4):
        if Ltrain[j]==Ltest[i-3]:
            if Ltrain[j+1]==Ltest[i-1]:
                if Ltrain[j+2]==Ltest[i-2]:
                    if Ltrain[j+3]==Ltest[i]:
                        if Ltrain[j+4]=='+':
                            m+=1
                        elif Ltrain[j+4]=='-':
                            n+=1
    if m/(m+n) > 0.5:
        pred4S.append("+")
    elif m/(m+n)<0.5:
        pred4S.append("-")
    else:
        pred4S.append("+") #p* is 61%   
      

#part 2
#gap
#w=2
Ltest=df_GAB["True Label"].where((df_GAB["Year"]==2019) | (df_GAB["Year"]==2020) ).dropna().values.tolist()
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]==pred2G[i]:
        m+=1
    else:
        n+=1
print("accuracy of w=2 is",m/(m+n)) #60% accuracy 

#w=3
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]==pred3G[i]:
        m+=1
    else:
        n+=1
print("accuracy of w=3 is",m/(m+n)) #60% accuracy 

#w=4
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]==pred4G[i]:
        m+=1
    else:
        n+=1
print("accuracy of w=4 is",m/(m+n))#67% accuracy 

#spy
Ltest=df_SPY["True Label"].where((df_SPY["Year"]==2019) | (df_SPY["Year"]==2020) ).dropna().values.tolist()
#w=2
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]==pred2S[i]:
        m+=1
    else:
        n+=1
print("accuracy of w=2 is",m/(m+n)) #59% accuracy 

#w=3
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]==pred3S[i]:
        m+=1
    else:
        n+=1
print("accuracy of w=3 is",m/(m+n))#39% accuracy 

x

#w=4
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]==pred4S[i]:
        m+=1
    else:
        n+=1
print("accuracy of w=2 is",m/(m+n)) #43% accuracy 

#part 3
#for GAB, W=4 was most accurate
#for SPY, W=2 was most accurate



















    

