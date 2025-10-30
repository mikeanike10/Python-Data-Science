#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 13:26:13 2023

@author: Michael Glass
Question 5
test logistic regression with different missing parameters
"""
#1
log_reg = LogisticRegression()
#missing f1
x_traindrop=x_train.drop(columns=["f1"])
x_testdrop=x_test.drop(columns=["f1"])
log_reg.fit(x_traindrop,y_train)
y_pred =  log_reg.predict(x_testdrop)
cm = confusion_matrix(y_test,y_pred)
print(accuracy_score(y_test,y_pred)) #0.82

#missing f2
x_traindrop=x_train.drop(columns=["f2"])
x_testdrop=x_test.drop(columns=["f2"])
log_reg.fit(x_traindrop,y_train)
y_pred =  log_reg.predict(x_testdrop)
cm = confusion_matrix(y_test,y_pred)
print(accuracy_score(y_test,y_pred)) #0.90

#missing f3
x_traindrop=x_train.drop(columns=["f3"])
x_testdrop=x_test.drop(columns=["f3"])
log_reg.fit(x_traindrop,y_train)
y_pred =  log_reg.predict(x_testdrop)
cm = confusion_matrix(y_test,y_pred)
print(accuracy_score(y_test,y_pred))#0.88

#missing f4
x_traindrop=x_train.drop(columns=["f4"])
x_testdrop=x_test.drop(columns=["f4"])
log_reg.fit(x_traindrop,y_train)
y_pred =  log_reg.predict(x_testdrop)
cm = confusion_matrix(y_test,y_pred)
print(accuracy_score(y_test,y_pred)) #0.99

#2
#accuracy did not increase in any case

#3
#dropping f1 lost the most accuracy

#4
#dropping f4 lost the least accuracy

#5
#knn had less loss in general, but for both classifying methods losing f1 had the largest loss in accuracy
#and losing f4 had the least loss in accuracy


