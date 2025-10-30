#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 13:08:49 2023

@author: Michael Glass
Question 5
create logistic regression using test and train and assess
"""
#1
from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(x_train,y_train)
y_pred =  log_reg.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
print(accuracy_score(y_test,y_pred))#0.99

#2
test=y_test
test=test.reset_index(drop=True)
TP=0
FP=0
TN=0
FN=0
for i in range(len(y_test)):
    if (test[i]==y_pred[i]) & (test[i]==0):
        TP+=1
    elif (test[i]!=y_pred[i]) & (test[i]==1):
        FP+=1
    elif (test[i]==y_pred[i]) & (test[i]==1):
        TN+=1
    elif (test[i]!=y_pred[i]) & (test[i]==0):
        FN+=1
        
values=[TP,FP,TN,FN,TP/(FP+TP),TN/(FN+TN)]
lacc=pd.DataFrame({"TP":[TP],
                  "FP":[FP],
                  "TN":[TN],
                  "FN":[FN],
                  "accuracy":[(TP+TN)/len(test)],
                  "TPR":[TP/(FP+TP)],
                  "TNR":[TN/(FN+TN)]})


#3
#the logistic regression is better then my simple classifier in every measure

#4
#knn is better in every measure then the logistic regression, but only by a little

#5 
BUID=pd.DataFrame({"f1":[8],
                   "f2":[9],
                   "f3":[6],
                   "f4":[0]})
y_pred =  log_reg.predict(BUID)
print("using my BUID digits as feature values logistic prediction is class",y_pred) #0


