#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 11:41:03 2023

@author: Michael Glass
CS 677
Problem 1
create 5 dataframes based on years and analyze
"""

 #question 1
 #initalizes values and clears last run
 x=linesGAB[0].split(",") #creates list to determine location of each value
 w=x.index("Weekday") #index value for weekdays
 r=x.index("Return") #index value for returns
 y=x.index("Year") #index value for year
 m=[] #Monday Return list
 tu=[] #Tuesday Return list
 we=[] #Wednesday Return list
 th=[] #thursday return list
 f=[] #friday return list
  

 for i in range(1,len(linesGAB)):
     t=linesGAB[i].split(",") #turns string into list
     if t[y]=="2016": #determines year, manually change between 2016 to 2020 to create tables
         if t[w]=="Monday": #appends monday values of year
             m.append(eval(t[r]))
         elif t[w]=="Tuesday": #appends tuesday values of year
             tu.append(eval(t[r]))
         elif t[w]=="Wednesday": #appends wednesday values of year
             we.append(eval(t[r]))
         elif t[w]=="Thursday": #appends thursday values of year
             th.append(eval(t[r]))
         else:                  #appends friday values of year
             f.append(eval(t[r]))
     
 #initializes values and clears last run
 muR=[] #mew of R
 sdR=[] #standard deviation of R
 lRP=[] #amount of returns with positive 
 muRP=[] #positive returns mew
 sdRP=[] #positive standard deviation
 lRN=[] #amount of returns with negative
 muRN=[] #mew of negative returns
 sdRN=[] #standard deviation of negative returns

 j=0
 for i in [m,tu,we,th,f]:
     mu=sum(i)/len(i) #mu of each day
     sd=sum([(x-mu)**2 for x in i])/len(i) #sd of each day
     lp=len([x for x in i if x>0]) #days with positive returns
     mup=sum([x for x in i if x>0])/len([x for x in i if x>0]) #positive returns mu
     sdp=sum([(x-mup)**2 for x in i if x>0])/len([x for x in i if x>0]) #positive returns sd
     ln=len([x for x in i if x<0]) #days with negative returns
     mun=sum([x for x in i if x<0])/len([x for x in i if x<0]) #negative returns mu
     sdn=sum([(x-mup)**2 for x in i if x<0])/len([x for x in i if x<0]) #negative returns sd
     muR.append(mu)
     sdR.append(sd)
     lRP.append(lp)
     muRP.append(mup)
     sdRP.append(sdp)
     lRN.append(ln)
     muRN.append(mun)
     sdRN.append(sdn)
     
 #creates dataframe from values
 df=pd.DataFrame({"Days":("Monday","Tuesday","Wednesday","Thursday","Friday"),
              "muR":muR,
              "sdR":sdR,
              "lRP":lRP,
              "muRP":muRP,
              "sdRP":sdRP,
              "lRN":lRN,
              "muRN":muRN,
              "sdRN":sdRN})
