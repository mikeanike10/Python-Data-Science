#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 18:07:38 2023

@author: Michael Glass
Question 1
#import data and make calculations
"""
import os
import pandas as pd

txt=open(r'data_banknote_authentication.txt','r')
lines=txt.readlines()
txt.close()

#1
fone=[]
ftwo=[]
fthree=[]
ffour=[]
c=[]
color=[]
for attribute in lines:
    x=attribute.split(",")
    fone.append(float(x[0]))
    ftwo.append(float(x[1]))
    fthree.append(float(x[2]))
    ffour.append(float(x[3]))
    c.append(int(x[4]))
    if int(x[4])==0:
        color.append("green")
    else:
        color.append("red")
     
    
        
df=pd.DataFrame({"f1":fone,
                 "f2":ftwo,
                 "f3":fthree,
                 "f4":ffour,
                 "class":c,
                 "color":color
                 })

#2

mean=df.loc[:,df.columns!="class"].mean().round(2)
sd=df.loc[:,df.columns!="class"].std().round(2)
Call=[]
for i in range(4):
    Call.append(mean[i])
    Call.append(sd[i])
    
mean=df.loc[:,df.columns!="class"].where(df["class"]==0).mean().round(2)
sd=df.loc[:,df.columns!="class"].where(df["class"]==0).std().round(2)
Czero=[]
for i in range(4):
    Czero.append(mean[i])
    Czero.append(sd[i])
    
mean=df.loc[:,df.columns!="class"].where(df["class"]==1).mean().round(2)
sd=df.loc[:,df.columns!="class"].where(df["class"]==1).std().round(2)
Cone=[]
for i in range(4):
    Cone.append(mean[i])
    Cone.append(sd[i])


values=[Czero,Cone,Call]
mandsd=pd.DataFrame(values,
                    columns=["mu(f1)","sd(f1)","mu(f2)","sd(f2)","mu(f3)","sd(f3)","mu(f4)","sd(f4)"]
                    ).rename(index={2:"all"})


#3
#f4 has negative mean and standard deviation no matter the subset
#f2 has similar standard deviations between subsets










