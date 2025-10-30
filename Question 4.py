#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 12:59:16 2023

@author: Michael Glass
Question 4
test best k with different missing parameters and assess
"""


#1
classifier = KNeighborsClassifier(n_neighbors=11) 


#missing f1
x_traindrop=x_train.drop(columns=["f1"])
x_testdrop=x_test.drop(columns=["f1"])
x_train_sc = scaler.fit_transform(x_traindrop)
x_test_sc = scaler.transform(x_testdrop)
classifier.fit(x_train_sc,y_train)
y_pred =  classifier.predict(x_test_sc)
cm = confusion_matrix(y_test,y_pred)
print(accuracy_score(y_test,y_pred)) #0.94

#missing f2
x_traindrop=x_train.drop(columns=["f2"])
x_testdrop=x_test.drop(columns=["f2"])
x_train_sc = scaler.fit_transform(x_traindrop)
x_test_sc = scaler.transform(x_testdrop)
classifier.fit(x_train_sc,y_train)
y_pred =  classifier.predict(x_test_sc)
cm = confusion_matrix(y_test,y_pred)
print(accuracy_score(y_test,y_pred)) #0.97

#missing f3
x_traindrop=x_train.drop(columns=["f3"])
x_testdrop=x_test.drop(columns=["f3"])
x_train_sc = scaler.fit_transform(x_traindrop)
x_test_sc = scaler.transform(x_testdrop)
classifier.fit(x_train_sc,y_train)
y_pred =  classifier.predict(x_test_sc)
cm = confusion_matrix(y_test,y_pred)
print(accuracy_score(y_test,y_pred))#0.97

#missing f4
x_traindrop=x_train.drop(columns=["f4"])
x_testdrop=x_test.drop(columns=["f4"])
x_train_sc = scaler.fit_transform(x_traindrop)
x_test_sc = scaler.transform(x_testdrop)
classifier.fit(x_train_sc,y_train)
y_pred =  classifier.predict(x_test_sc)
cm = confusion_matrix(y_test,y_pred)
print(accuracy_score(y_test,y_pred)) #0.99

#2
#accuracy decreased in every scenario

#3
#dropping f1 contributed the biggest lo

#4
#dropping f4 lost the least accuracy 

















