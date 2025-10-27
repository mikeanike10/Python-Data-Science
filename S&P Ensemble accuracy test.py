#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:13:10 2023

@author: Michael Glass
CS 677
question 4
calculate different rates of accuracy
For this question instead of seperating steps 1-6 I made each variable by its hyperparameter and which stock it came from
"""
import pandas as pd
    
#for GAB
Ltest=df_GAB["True Label"].where((df_GAB["Year"]==2019) | (df_GAB["Year"]==2020) ).dropna().values.tolist()


#W=2
TP=0
FN=0
TN=0
FP=0
pred=pred2G
for i in range(len(Ltest)):
    if Ltest[i]=="+":
        if Ltest[i]==pred[i]:
            TP+=1
        elif Ltest[i]!=pred[i]:
            FN+1
    if Ltest[i]=="-":
        if Ltest[i]==pred[i]:
            TN+=1
        elif Ltest[i]!=pred[i]:
            FP+=1
GW2=[2,"GAB",TP,FP,TN,FN,(TP+TN)/len(pred),TP/(TP+FN),TN/(TN+FP)]


#W=3
TP=0
FN=0
TN=0
FP=0
pred=pred3G
for i in range(len(Ltest)):
    if Ltest[i]=="+":
        if Ltest[i]==pred[i]:
            TP+=1
        elif Ltest[i]!=pred[i]:
            FN+1
    if Ltest[i]=="-":
        if Ltest[i]==pred[i]:
            TN+=1
        elif Ltest[i]!=pred[i]:
            FP+=1
GW3=[3,"GAB",TP,FP,TN,FN,(TP+TN)/len(pred),TP/(TP+FN),TN/(TN+FP)]

#w=4
TP=0
FN=0
TN=0
FP=0
pred=pred4G
for i in range(len(Ltest)):
    if Ltest[i]=="+":
        if Ltest[i]==pred[i]:
            TP+=1
        elif Ltest[i]!=pred[i]:
            FN+1
    if Ltest[i]=="-":
        if Ltest[i]==pred[i]:
            TN+=1
        elif Ltest[i]!=pred[i]:
            FP+=1
GW4=[4,"GAB",TP,FP,TN,FN,(TP+TN)/len(pred),TP/(TP+FN),TN/(TN+FP)]

#ensemble
TP=0
FN=0
TN=0
FP=0
pred=predEG
for i in range(len(Ltest)):
    if Ltest[i]=="+":
        if Ltest[i]==pred[i]:
            TP+=1
        elif Ltest[i]!=pred[i]:
            FN+1
    if Ltest[i]=="-":
        if Ltest[i]==pred[i]:
            TN+=1
        elif Ltest[i]!=pred[i]:
            FP+=1
GE=["ensemble","GAB",TP,FP,TN,FN,(TP+TN)/len(pred),TP/(TP+FN),TN/(TN+FP)]

#for spy
Ltest=df_SPY["True Label"].where((df_SPY["Year"]==2019) | (df_SPY["Year"]==2020) ).dropna().values.tolist()
#W=2
TP=0
FN=0
TN=0
FP=0
pred=pred2S
for i in range(len(Ltest)):
    if Ltest[i]=="+":
        if Ltest[i]==pred[i]:
            TP+=1
        elif Ltest[i]!=pred[i]:
            FN+1
    if Ltest[i]=="-":
        if Ltest[i]==pred[i]:
            TN+=1
        elif Ltest[i]!=pred[i]:
            FP+=1
SW2=[2,"S&P-500",TP,FP,TN,FN,(TP+TN)/len(pred),TP/(TP+FN),TN/(TN+FP)]


#W=3
TP=0
FN=0
TN=0
FP=0
pred=pred3S
for i in range(len(Ltest)):
    if Ltest[i]=="+":
        if Ltest[i]==pred[i]:
            TP+=1
        elif Ltest[i]!=pred[i]:
            FN+1
    if Ltest[i]=="-":
        if Ltest[i]==pred[i]:
            TN+=1
        elif Ltest[i]!=pred[i]:
            FP+=1
SW3=[3,"S&P-500",TP,FP,TN,FN,(TP+TN)/len(pred),TP/(TP+FN),TN/(TN+FP)]
#TP is 199
SW3[4]
SW3[2]
pred3S.count("-")
x=0
for i in range(len(Ltest)):
    if (Ltest[i]=='-') & (pred3S=='-'):
        x+=1
print(x)
#w=4
TP=0
FN=0
TN=0
FP=0
pred=pred4S
for i in range(len(Ltest)):
    if Ltest[i]=="+":
        if Ltest[i]==pred[i]:
            TP+=1
        elif Ltest[i]!=pred[i]:
            FN+1
    if Ltest[i]=="-":
        if Ltest[i]==pred[i]:
            TN+=1
        elif Ltest[i]!=pred[i]:
            FP+=1
SW4=[4,"S&P-500",TP,FP,TN,FN,(TP+TN)/len(pred),TP/(TP+FN),TN/(TN+FP)]

#ensemble
TP=0
FN=0
TN=0
FP=0
pred=predES
for i in range(len(Ltest)):
    if Ltest[i]=="+":
        if Ltest[i]==pred[i]:
            TP+=1
        elif Ltest[i]!=pred[i]:
            FN+1
    if Ltest[i]=="-":
        if Ltest[i]==pred[i]:
            TN+=1
        elif Ltest[i]!=pred[i]:
            FP+=1
SE=["ensemble","S&P-500",TP,FP,TN,FN,(TP+TN)/len(pred),TP/(TP+FN),TN/(TN+FP)]

values=[GW2,GW3,GW4,GE,SW2,SW3,SW4,SE]

#part 7
rates=pd.DataFrame(values,columns=["W","ticker","TP","FP","TN","FN","accuracy","TPR","TNR"])
#for GAB, there is a higher average accuracy but abysmal TN rates making most hyperparameters with current training data useless.











    
    
    
