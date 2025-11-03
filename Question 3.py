#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 14:31:37 2023

@author: Michael Glass
Question 3

"""
import pandas as pd
#1
d={"Model":["Linear","Quadratic","Cubic","GLM","GLM log(y)"],
   "SSE 0":[1114142677733.0276,1156251304018.028,1156401636003.3994,1133210760949.6887,1144612941344.4023],
   "SSE 1":[489272557690.0972,490804335614.8889,491966262897.5837,485925037113.6133,564539865998.4521]}

df=pd.DataFrame(data=d)

#2
#smallest SSE for suviving is linear model
#smallest SSE for death was the glm model


#3
#largest SSE for suviving is linear model
#largest SSE for death was the glm model


