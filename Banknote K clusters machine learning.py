#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 15:27:20 2023

@author: Michael Glass
Question 3
#create knn algorithm for different Ks and assess 
"""
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt


#1
scaler = StandardScaler()
x_train_sc = scaler.fit_transform(x_train)
x_test_sc = scaler.transform(x_test)

#k=3
classifier = KNeighborsClassifier(n_neighbors=3) 
classifier.fit(x_train_sc,y_train)
y_pred =  classifier.predict(x_test_sc)
cm = confusion_matrix(y_test,y_pred)
print(accuracy_score(y_test,y_pred)) #0.998
kthree=accuracy_score(y_test,y_pred)
#k=5
classifier = KNeighborsClassifier(n_neighbors=5) 
classifier.fit(x_train_sc,y_train)
y_pred =  classifier.predict(x_test_sc)
cm = confusion_matrix(y_test,y_pred)
print(accuracy_score(y_test,y_pred)) #1.0
kfive=accuracy_score(y_test,y_pred)
#k=7
classifier = KNeighborsClassifier(n_neighbors=7) 
classifier.fit(x_train_sc,y_train)
y_pred =  classifier.predict(x_test_sc)
cm = confusion_matrix(y_test,y_pred)
print(accuracy_score(y_test,y_pred)) #1.0
kseven=accuracy_score(y_test,y_pred)
#k=9
classifier = KNeighborsClassifier(n_neighbors=9) 
classifier.fit(x_train_sc,y_train)
y_pred =  classifier.predict(x_test_sc)
cm = confusion_matrix(y_test,y_pred)
print(accuracy_score(y_test,y_pred)) #1.0
knine=accuracy_score(y_test,y_pred)
#k=11
classifier = KNeighborsClassifier(n_neighbors=11) 
classifier.fit(x_train_sc,y_train)
y_pred =  classifier.predict(x_test_sc)
cm = confusion_matrix(y_test,y_pred)
print(accuracy_score(y_test,y_pred)) #1.0
keleven=accuracy_score(y_test,y_pred)

#2
k=[3,5,7,9,11]
predacc=[kthree,kfive,kseven,knine,keleven]
plt.scatter(k,predacc)

#3
#k=11 is best
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
kacc=pd.DataFrame({"TP":[TP],
                  "FP":[FP],
                  "TN":[TN],
                  "FN":[FN],
                  "accuracy":[(TP+TN)/len(test)],
                  "TPR":[TP/(FP+TP)],
                  "TNR":[TN/(FN+TN)]})


#4
#knn is better then in every measure to my simple rules

#5 
#using simple
#predicts class 1


#using KNN
classifier = KNeighborsClassifier(n_neighbors=11) 
trainBUID=x_train
trainBUID.loc[len(x_train.index)]=[8,9,6,0]
x_train_sc = scaler.fit_transform(trainBUID)
classifier.fit(x_train_sc,y_train)
x_train_sc[685]
y_pred =  classifier.predict(x_train_sc)
print("using my BUID digits as feature values logistic prediction is class",y_pred[685])
#knn predicts 1













