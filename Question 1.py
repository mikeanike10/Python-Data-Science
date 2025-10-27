#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 11:01:33 2023

@author: Michael Glass
CS 677
Question 1
create data frames for Spy and personal(gab), add a true label column and calculate different probabilites 
"""

from pandas_datareader import data as web
import os
import pandas as pd
import numpy as np
import yfinance as yf

def get_stock(ticker, start_date, end_date, s_window, l_window):
    try:
        df = web.get_data_yahoo(ticker, start=start_date, end=end_date)
        df['Return'] = df['Adj Close'].pct_change()
        df['Return'].fillna(0, inplace=True)
        df['Date'] = df.index
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.month
        df['Year'] = df['Date'].dt.year
        df['Day'] = df['Date'].dt.day
        for col in ['Open', 'High', 'Low', 'Close', 'Adj Close']:
            df[col] = df[col].round(2)
        # df['Weekday'] = df['Date'].dt.weekday_name
        df['Weekday'] = df['Date'].dt.day_name()
        df['Week_Number'] = df['Date'].dt.strftime('%U')
        df['Year_Week'] = df['Date'].dt.strftime('%Y-%U')
        df['Short_MA'] = df['Adj Close'].rolling(
            window=s_window, min_periods=1).mean()
        df['Long_MA'] = df['Adj Close'].rolling(
            window=l_window, min_periods=1).mean()
        col_list = ['Date', 'Year', 'Month', 'Day', 'Weekday',
                    'Week_Number', 'Year_Week', 'Open',
                    'High', 'Low', 'Close', 'Volume', 'Adj Close',
                    'Return', 'Short_MA', 'Long_MA']
        num_lines = len(df)
        df = df[col_list]
        print('read ', num_lines, ' lines of data for ticker: ', ticker)
        return df
    except Exception as error:
        print(error)
        return None




here = os.path.abspath(r'C:\iCloud Drive\Documents\CS 677\Datasets')
input_dir = os.path.abspath(os.path.join(here, os.pardir))
tickers = ['GAB']
for ticker in tickers:
    try:
        output_file = os.path.join(input_dir, ticker + '.csv')
        df = get_stock(ticker, start_date='2016-01-01', end_date='2020-12-31',
                       s_window=14, l_window=50)
        df.to_csv(output_file, index=False)
        print('wrote ' + str(len(df)) + ' lines to file: ' + output_file)
    except Exception as e:
        print(e)
        print('failed to get Yahoo stock data for ticker: ', ticker)
        
df_GAB=df[['Year','Return']].copy()
TL=['+' if float(i)>=0 else '-' for i in df_GAB['Return']]
df_GAB["True Label"]=TL

    

here = os.path.abspath(r'C:\iCloud Drive\Documents\CS 677\Datasets')
input_dir = os.path.abspath(os.path.join(here, os.pardir))
tickers = ['SPY']
for ticker in tickers:
    try:
        output_file = os.path.join(input_dir, ticker + '.csv')
        df = get_stock(ticker, start_date='2016-01-01', end_date='2020-12-31',
                       s_window=14, l_window=50)
        df.to_csv(output_file, index=False)
        print('wrote ' + str(len(df)) + ' lines to file: ' + output_file)
    except Exception as e:
        print(e)
        print('failed to get Yahoo stock data for ticker: ', ticker)
        
df_SPY=df[['Year','Return']].copy()
TL=['+' if float(i)>=0 else '-' for i in df_SPY['Return']]
df_SPY["True Label"]=TL      
        
#part 2
#using GAB
L=df_GAB["True Label"].where((df_GAB["Year"]==2016) | (df_GAB["Year"]==2017) | (df_GAB["Year"]==2018) ).dropna().values.tolist()
LP=[i for i in L if i=='+']
LN=[i for i in L if i=="-"]
print("Chance of being an up day is",len(LP)/len(L)) #61% chance of positive day for GAB

#using spy
L=df_SPY["True Label"].where((df_SPY["Year"]==2016) | (df_SPY["Year"]==2017) | (df_SPY["Year"]==2018) ).dropna().values.tolist()
LP=[i for i in L if i=='+']
LN=[i for i in L if i=="-"]
print("Chance of next day being an up day is",len(LP)/len(L)) #55% chance of positive day for SPY

#part 3
#for GAB
L=df_GAB["True Label"].where((df_GAB["Year"]==2016) | (df_GAB["Year"]==2017) | (df_GAB["Year"]==2018) ).dropna().values.tolist()
#k=1
m=0#list for occurences of -,+
n=0#list of occurences of -,-
for i in range(len(L)-1):
    if L[i] == "-":
        if L[i+1] == "+":
            m+=1
        elif L[i+1] == "-":
            n+=1
print("probability of up day after one down day",m/(m+n)) #62% of the time an up happens after 1 down

#k=2
m=0#list for occurences of -,-,+
n=0#list of occurences of -,-,-
for i in range(len(L)-2):
    if (L[i]=="-") & (L[i+1]=='-'):
        if L[i+2]=="+":
            m+=1
        elif L[+2]=='-':
            n+=1
print("chance of up day after two down days is", m/(m+n)) #61% of the time an up happens after 2 down


#k=3
m=0#list for occurences of -,-,-,+
n=0#list of occurences of -,-,-,-
for i in range(len(L)-3):
    if (L[i] == "-") & (L[i+1] == "-") & ( L[i+2] == "-"):
        if L[i+3] =='+':
            m+=1
        elif L[i+3]:
            n+=1
print("chance of being up after 3 down is", m/(m+n)) #73% chance of being up after 3 down

#for SPY
#k=1       
L=df_SPY["True Label"].where((df_SPY["Year"]==2016) | (df_SPY["Year"]==2017) | (df_SPY["Year"]==2018) ).dropna().values.tolist()
m=0#list for occurences of -,+
n=0#list of occurences of -,-
for i in range(len(L)-1):
    if L[i] == "-":
        if L[i+1] == "+":
            m+=1
        elif L[i+1] == "-":
            n+=1
print("chance of being up after one down is",m/(m+n)) #59% of the time an up happens after 1 down  
                  
#k=2
m=0#list for occurences of -,-,+
n=0#list of occurences of -,-,-
for i in range(len(L)-2):
    if (L[i] == "-") &  (L[i+1] == "-"):
        if L[i+2] == "+":
            m+=1
        elif L[i+2] == "-":
            n+=1
print("Chance of being an up after two down is ",m/(m+n)) #59% chance of being up if 2 downs

#k=3
m=0#list for occurences of -,-,-,+
n=0#list of occurences of -,-,-,-
for i in range(len(L)-3):
    if (L[i] == "-") & (L[i+1]=="-") & (L[i+2]=='-'):
            if L[i+3] =='+':
                m+=1
            elif L[i+3] == "-":
                n+=1
print("Chance of being up after 3 down is",m/(m+n)) #64% chance of being up if 3 downs

#part 4
#for gab
#k=1
L=df_GAB["True Label"].where((df_GAB["Year"]==2016) | (df_GAB["Year"]==2017) | (df_GAB["Year"]==2018) ).dropna().values.tolist()
#k=1
m=0#list for occurences of +,+
n=0#list of occurences of +,-
for i in range(len(L)-1):
    if L[i] == "+":
        if L[i+1] == "+":
            m+=1
        elif L[i+1] == "-":
            n+=1
print("Chance of being up after one up is",m/(m+n)) #61% chance of being up after being up

#k=2
m=0#list for occurences of +,+,+
n=0#list of occurences of +,+,-
for i in range(len(L)-2):
    if (L[i] == "+") & (L[i+1] == "+"):
        if L[i+2] == "+":
            m+=1
        elif L[i+2] == "-":
            n+=1
print("Chance of being up after two ups is",m/(m+n))#61% chance of being up after 2 ups

#k=3
m=0#list for occurences of +,+,+,+
n=0#list of occurences of +,+,+,-
for i in range(len(L)-3):
    if (L[i] == "+") & (L[i+1] == "+") & (L[i+2] == "+"):
        if L[i+3] =='+':
            m+=1
        elif L[i+3] =="-":
            n+=1
print("Chance of being up after 3 ups is",m/(m+n)) #58% chance of being up after 3 ups

#for spy
L=df_SPY["True Label"].where((df_SPY["Year"]==2016) | (df_SPY["Year"]==2017) | (df_SPY["Year"]==2018) ).dropna().values.tolist()
#k=1
m=0#list for occurences of +,+
n=0#list of occurences of +,-
for i in range(len(L)-1):
    if L[i] == "+":
        if L[i+1] == "+":
            m+=1
        elif L[i+1] == "-":
            n+=1
print("Chance of being up after one up is",m/(m+n))#52% chance of being up after 1 up

#k=2
m=0#list for occurences of +,+,+
n=0#list of occurences of +,+,-
for i in range(len(L)-2):
    if (L[i] == "+") & (L[i+1] == "+"):
        if L[i+2] == "+":
            m+=1
        elif L[i+2] == "-":
            n+=1
print("Chance of being up after two ups is",m/(m+n)) #50% chance of being up after 2 ups

#k=3      
m=0#list for occurences of +,+,+,+
n=0#list of occurences of +,+,+,-
for i in range(len(L)-3):
    if (L[i] == "+") & (L[i+1] == "+") & (L[i+2] == "+"):
        if L[i+3] =='+':
            m+=1
        elif L[i+3] =="-":
            n+=1
print("Chance of being up after 3 ups is",m/(m+n))#47% chance of being up after 4 ups

 
        
        
        
        
        
        
        
        