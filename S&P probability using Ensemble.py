#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:42:01 2023

@author: Michael Glass
CS 677
Question 3
create ensemble method for predicting true labels of year 4 and 5
"""



#part 1

#for GAB
Ltrain=df_GAB["True Label"].where((df_GAB["Year"]==2016) | (df_GAB["Year"]==2017) | (df_GAB["Year"]==2018) ).dropna().values.tolist()
Ltest=df_GAB["True Label"].where((df_GAB["Year"]==2019) | (df_GAB["Year"]==2020) ).dropna().values.tolist()
for i in range(753,750,-1): #adds rows to allow W prediction method 
    Ltest.insert(0,Ltrain[i])


predEG=[] #stored balues for predicted ensemble GAB

for i in range(3,len(Ltest)): 
#w=2
    u=0 #count of up predictions
    d=0 #count of down predictions
    m=0 #count of sequences ending in + with previous matching sequence
    n=0 #count of sequences ending in - with previous matching sequence
    for j in range(len(Ltrain)-2):
        if Ltrain[j]==Ltest[i-1]:
            if Ltrain[j+1]==Ltest[i]:
                if Ltrain[j+2]=='+':
                    m+=1
                elif Ltrain[j+2]=='-':
                    n+=1
    if m/(m+n) > 0.5:
        u+=1
    elif m/(m+n) < 0.5:
        d+=1
    else:
        u+=1
#w=3
    m=0
    n=0
    for j in range(len(Ltrain)-3):
        if Ltrain[j]==Ltest[i-2]:
            if Ltrain[j+1]==Ltest[i-1]:
                if Ltrain[j+2]==Ltest[i]:
                    if Ltrain[j+3]=='+':
                        m+=1
                    elif Ltrain[j+3]=='-':
                        n+=1
    if m/(m+n) > 0.5:
        u+=1
    elif m/(m+n)<0.5:
        d+=1
    else:
        u+=1 #p* is 61%
#w=4
    m=0
    n=0
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
        u+=1
    elif m/(m+n)<0.5:
        d+=1
    else:
        u+=1 #p* is 61%
        
    if u > d:
        predEG.append('+')
    elif u < d:
        predEG.append('-')
        

#for spy
Ltrain=df_SPY["True Label"].where((df_SPY["Year"]==2016) | (df_SPY["Year"]==2017) | (df_SPY["Year"]==2018) ).dropna().values.tolist()
Ltest=df_SPY["True Label"].where((df_SPY["Year"]==2019) | (df_SPY["Year"]==2020) ).dropna().values.tolist()
for i in range(753,750,-1):
    Ltest.insert(0,Ltrain[i])
predES=[] #stored balues for predicted ensemble GAB

for i in range(3,len(Ltest)): 
#w=2
    u=0 #count of up predictions
    d=0 #count of down predictions
    m=0
    n=0
    for j in range(len(Ltrain)-2):
        if Ltrain[j]==Ltest[i-1]:
            if Ltrain[j+1]==Ltest[i]:
                if Ltrain[j+2]=='+':
                    m+=1
                elif Ltrain[j+2]=='-':
                    n+=1
    if m/(m+n) > 0.5:
        u+=1
    elif m/(m+n) < 0.5:
        d+=1
    else:
        u+=1 #p* is 55% being "+"
#w=3
    m=0
    n=0
    for j in range(len(Ltrain)-3):
        if Ltrain[j]==Ltest[i-2]:
            if Ltrain[j+1]==Ltest[i-1]:
                if Ltrain[j+2]==Ltest[i]:
                    if Ltrain[j+3]=='+':
                        m+=1
                    elif Ltrain[j+3]=='-':
                        n+=1
    if m/(m+n) > 0.5:
        u+=1
    elif m/(m+n)<0.5:
        d+=1
    else:
        u+=1 #p* is 55% being "+"
#w=4
    m=0
    n=0
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
        u+=1
    elif m/(m+n)<0.5:
        d+=1
    else:
        u+=1 #p* is 55%
        
    if u > d:
        predES.append('+')
    elif u < d:
        predES.append('-')
        

#part 2
#for GAB
Ltest=df_GAB["True Label"].where((df_GAB["Year"]==2019) | (df_GAB["Year"]==2020) ).dropna().values.tolist()
for i in range(len(Ltest)):
    if Ltest[i]==predEG[i]:
        m+=1
    else:
        n+=1
print("accuracy of ensemble is",m/(m+n)) #59% accuracy 

#for SPY
Ltest=df_SPY["True Label"].where((df_SPY["Year"]==2019) | (df_SPY["Year"]==2020) ).dropna().values.tolist()
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]==predES[i]:
        m+=1
    else:
        n+=1
print("accuracy of ensemble is",m/(m+n))#49% accuracy 

#part 3
#for GAB
Ltest=df_GAB["True Label"].where((df_GAB["Year"]==2019) | (df_GAB["Year"]==2020) ).dropna().values.tolist()
#W=2
m=0 #count of matching '-'
n=0 #count of '-' in test
for i in range(len(Ltest)):
    if Ltest[i]=="-":
        n+=1
        if Ltest[i]==pred2G[i]:
            m+=1
print("Ratio of accurately predicted '-' is",m/n) #0%

#w=3
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]=="-":
        n+=1
        if Ltest[i]==pred3G[i]:
            m+=1
print("Ratio of accurately predicted '-' is",m/n) #0

#w=4
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]=="-":
        n+=1
        if Ltest[i]==pred4G[i]:
            m+=1
print("Ratio of accurately predicted '-' is",m/n) #17%

#ensemble
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]=="-":
        n+=1
        if Ltest[i]==predEG[i]:
            m+=1
print("Ratio of accurately predicted '-' is",m/n) #0

#ensemble did not improve over W=4 '-' prediction rate

#for spy
Ltest=df_SPY["True Label"].where((df_SPY["Year"]==2019) | (df_SPY["Year"]==2020) ).dropna().values.tolist()
#w=2
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]=="-":
        n+=1
        if Ltest[i]==pred2S[i]:
            m+=1
print("Ratio of accurately predicted '-' is",m/n) #0

#w=3
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]=="-":
        n+=1
        if Ltest[i]==pred3S[i]:
            m+=1
print("Ratio of accurately predicted '-' is",m/n) #0

#w=4
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]=="-":
        n+=1
        if Ltest[i]==pred4S[i]:
            m+=1
print("Ratio of accurately predicted '-' is",m/n) #0.8%

#ensemble
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]=="-":
        n+=1
        if Ltest[i]==predES[i]:
            m+=1
print("Ratio of accurately predicted '-' is",m/n) #0
#ensemble did not improve prediction rate of '-'



#part 4
Ltest=df_GAB["True Label"].where((df_GAB["Year"]==2019) | (df_GAB["Year"]==2020) ).dropna().values.tolist()
#W=2
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]=="+":
        n+=1
        if Ltest[i]==pred2G[i]:
            m+=1
print("Ratio of accurately predicted '+' is",m/n) #100%

#w=3
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]=="+":
        n+=1
        if Ltest[i]==pred3G[i]:
            m+=1
print("Ratio of accurately predicted '+' is",m/n) #100%

#w=4
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]=="+":
        n+=1
        if Ltest[i]==pred4G[i]:
            m+=1
print("Ratio of accurately predicted '+' is",m/n) #100%

#ensemble
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]=="+":
        n+=1
        if Ltest[i]==predEG[i]:
            m+=1
print("Ratio of accurately predicted '+' is",m/n) #100%
#ensemble was not able to improve prediction of '+'

#for spy
Ltest=df_SPY["True Label"].where((df_SPY["Year"]==2019) | (df_SPY["Year"]==2020) ).dropna().values.tolist()
#w=2
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]=="+":
        n+=1
        if Ltest[i]==pred2S[i]:
            m+=1
print("Ratio of accurately predicted '+' is",m/n) #100%

#w=3
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]=="+":
        n+=1
        if Ltest[i]==pred3S[i]:
            m+=1
print("Ratio of accurately predicted '+' is",m/n) #67%

#W=4
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]=="+":
        n+=1
        if Ltest[i]==pred4S[i]:
            m+=1
print("Ratio of accurately predicted '+' is",m/n) #67%



#ensemble
m=0
n=0
for i in range(len(Ltest)):
    if Ltest[i]=="+":
        n+=1
        if Ltest[i]==predES[i]:
            m+=1
print("Ratio of accurately predicted '+' is",m/n) #83%

#ensemble is the second best of the four, but with w=2 being 100% it is likely faulty






