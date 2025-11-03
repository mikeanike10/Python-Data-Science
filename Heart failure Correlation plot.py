# -*- coding: utf-8 -*-
"""
Spyder Editor

Michael Glass
CS 677
Question 1
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#1
df=pd.read_csv('heart_failure_clinical_records_dataset.csv',
               usecols=['creatinine_phosphokinase',
                        'serum_creatinine',
                        'serum_sodium',
                        'platelets',
                        'DEATH_EVENT'])
df_0=df[df["DEATH_EVENT"]==0].drop(columns=['DEATH_EVENT'])
df_1=df[df["DEATH_EVENT"]==1].drop(columns=['DEATH_EVENT'])

#2
M0=df_0.corr()


figure = plt.figure()
axes = figure.add_subplot(111)
ax = axes.matshow(M0, interpolation ='nearest',cmap='seismic') 
figure.colorbar(ax)
for (x, y), value in np.ndenumerate(M0):
    plt.text(x, y, f"{value:.2f}", va="center", ha="center")


M1=df_1.corr()
figure = plt.figure()
axes = figure.add_subplot(111)
ax = axes.matshow(M1, interpolation ='nearest') 
figure.colorbar(ax)
for (x, y), value in np.ndenumerate(M1):
    plt.text(x, y, f"{value:.2f}", va="center", ha="center")

#3
#a
#platelets and serum sodium have the highest correlation for surviving patietns
#b
#serum sodium and serum creatinine have the lowest correlation 
#c
#serum_sodium and creatinine_phosphokinase has the highest correlation
#d
#serum sodium and serum creatine have the lowest correlation
#e
#both matrices have the same lowest correlation between serum sodium and serum creatine, but different highest correlation








