#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 13:23:07 2023

@author: Michael Glass
Question 2
create train and test data and create a simple classifier
"""
import seaborn
from sklearn.model_selection import train_test_split
#1
x_train,x_test,y_train, y_test = train_test_split(df[["f1","f2","f3","f4"]], df["class"], test_size=0.5,random_state=1, stratify=df["class"])

seaborn.pairplot(x_train.loc[y_train[y_train==0].index.tolist()])
seaborn.pairplot(x_train.loc[y_train[y_train==1].index.tolist()])



#2
#f1>0 and f2>0 and f3>1



#3
pred=[]
for i in x_test.index:
    if (x_test.loc[i]["f1"]>-1) & (x_test.loc[i]["f2"]>3) & (x_test.loc[i]["f3"]<2):
        pred.append(0)
    else:
        pred.append(1)
        
#4
test=y_test
test=test.reset_index(drop=True)
TP=0
FP=0
TN=0
FN=0
for i in range(len(test)):
    if (test[i]==pred[i]) & (test[i]==0):
        TP+=1
    elif (test[i]!=pred[i]) & (test[i]==1):
        FP+=1
    elif (test[i]==pred[i]) & (test[i]==1):
        TN+=1
    elif (test[i]!=pred[i]) & (test[i]==0):
        FN+=1
        
values=[TP,FP,TN,FN,TP/(FP+TP),TN/(FN+TN)]
acc=pd.DataFrame({"TP":[TP],
                  "FP":[FP],
                  "TN":[TN],
                  "FN":[FN],
                  "accuracy":[(TP+TN)/len(test)],
                  "TPR":[TP/(FP+TP)],
                  "TNR":[TN/(FN+TN)]})

#5
#better at identifying good bills and accuracy is better then a coinflip(66%)











