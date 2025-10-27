#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 15:54:57 2023

@author: michae Glass
cs 677
question 5
create graph with buy and hold strategy and best W* and ensemble graphed along it
"""
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

#part 1
df_returns=df_GAB.where((df_GAB["Year"]==2019) | (df_GAB["Year"]==2020) ).dropna().values
df_returns=pd.DataFrame(df_returns,
                        columns=["Year","Return","True Label"])
df_returns["predW4"]=pred4G
df_returns["predEG"]=predEG
x=[]
r=100
for i in range(len(df_returns["Return"])):
    x.append(r)
    r+=r*float(df_returns["Return"][i])
print("Buy and Hold made",r) #151.93

#best W*
x1=[]
r=100
for i in range(len(df_returns["Return"])):
    if df_returns["predW4"][i]=="+":
        x1.append(r)
        r+=r*float(df_returns["Return"][i])
print("Best W* made",r) #245.13

#ensemble
x2=[]
r=100
for i in range(len(df_returns["Return"])):
    if df_returns["predEG"][i]=="+":
        x2.append(r)
        r+=r*float(df_returns["Return"][i])
print("ensemble made",r) #151.93

plt.plot(x, 'red',label="Buy and hold", x1, 'blue', x2, 'green')
plt.plot(x,"red",label="Buy and hold")
plt.plot(x1,"blue",label="Best W*")
plt.plot(x2,"green",label="ensemble")
plt.legend(loc="upper left")

#part 2
#steady growth for 2014 with a massive drop for both around the same time. Both final points massively higher then their lowest. Appears to coincide with covid
#buy and hold matches ensemble because the ensemble method predicted every label to be "+"


