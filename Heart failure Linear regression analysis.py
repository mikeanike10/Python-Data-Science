#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 14:41:44 2023

@author: Michael Glass
Question 2

"""
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import sklearn.linear_model
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
#using group 1, x creatinine phosphokinase and y platelets 
#question 1
#survivining
x_train,x_test,y_train, y_test = train_test_split(df_0.loc[:,["creatinine_phosphokinase"]],df_0.loc[:, ["platelets"]],test_size=0.5,random_state=1)
test = pd.concat([x_test, y_test], axis=1)
test=test.sort_values(by=['creatinine_phosphokinase'])
x_test=test.loc[:,["creatinine_phosphokinase"]]
y_test=test.loc[:,["platelets"]]

#survivining
#simple linear
lin_reg = LinearRegression()
lin_reg.fit(x_train,y_train)
print([lin_reg.intercept_,lin_reg.coef_[0]]) #a=260156.63 b=6.728
y_pred = lin_reg.predict(x_test)
plt.plot(x_test, y_test, "b.")
plt.plot(x_test,y_pred,"k--")
plt.xlabel("Predictor variable")
plt.ylabel("Response Variable")
residual=(y_test-y_pred)**2
sum(residual["platelets"]) #1114142677733.0276

#quadratic
poly = PolynomialFeatures(2, include_bias=False) # argument here is the highest degree you want for your model; here we have 2 for a quadratic model
x_new = poly.fit_transform(x_train)
lin_reg = LinearRegression()
lin_reg.fit(x_new,y_train)
print([lin_reg.intercept_,lin_reg.coef_[0]])#a=249629.09273105 b=4.24997883e+01 c=-9.06885516e-03
x_test_new = poly.fit_transform(x_test)
y_pred = lin_reg.predict(x_test_new)
plt.plot(x_test, y_test, "b.")
plt.plot(x_test,y_pred,"k--")
plt.xlabel("Predictor variable")
plt.ylabel("Response Variable")
residual=(y_test-y_pred)**2
sum(residual["platelets"]) #1156251304018.028

#cubic
poly = PolynomialFeatures(3, include_bias=False) # argument here is the highest degree you want for your model; here we have 2 for a quadratic model
x_new = poly.fit_transform(x_train)
lin_reg = LinearRegression()
lin_reg.fit(x_new,y_train)
print([lin_reg.intercept_,lin_reg.coef_[0]])#a=249477.46132367 b=4.33266316e+01 c=-9.65154105e-03 d=8.75619952e-08
x_test_new = poly.fit_transform(x_test)
y_pred = lin_reg.predict(x_test_new)
plt.plot(x_test, y_test, "b.")
plt.plot(x_test,y_pred,"k--")
plt.xlabel("Predictor variable")
plt.ylabel("Response Variable")
residual=(y_test-y_pred)**2
sum(residual["platelets"]) #1156401636003.3994

#glm
lin_reg = LinearRegression()
lin_reg.fit(np.log(x_train),y_train)
print([lin_reg.intercept_,lin_reg.coef_]) #a=208922.97023079 b=9808.95423947
y_pred = lin_reg.predict(np.log(x_test))
plt.plot(x_test, y_test, "b.")
plt.plot(x_test,y_pred,"k--")
plt.xlabel("Predictor variable")
plt.ylabel("Response Variable")
residual=(y_test-y_pred)**2
sum(residual["platelets"]) #1133210760949.6887

#glm log(y)
lin_reg = LinearRegression()
lin_reg.fit(np.log(x_train),np.log(y_train))
print([lin_reg.intercept_,lin_reg.coef_]) #a=12.34157938 b=0.01599545
y_pred = lin_reg.predict(np.log(x_test))
y_pred=np.exp(y_pred)
plt.plot(x_test, y_test, "b.")
plt.plot(x_test,y_pred,"k--")
plt.xlabel("Predictor variable")
plt.ylabel("Response Variable")
residual=(y_test-y_pred)**2
sum(residual["platelets"]) #1144612941344.4023

#dead
x_train,x_test,y_train, y_test = train_test_split(df_1.loc[:,["creatinine_phosphokinase"]],df_1.loc[:, ["platelets"]],test_size=0.5,random_state=1)
test = pd.concat([x_test, y_test], axis=1)
test=test.sort_values(by=['creatinine_phosphokinase'])
x_test=test.loc[:,["creatinine_phosphokinase"]]
y_test=test.loc[:,["platelets"]]

#simple linear
lin_reg = LinearRegression()
lin_reg.fit(x_train,y_train)
print([lin_reg.intercept_,lin_reg.coef_[0]]) #a=239295.84159125 b=7.81546747
y_pred = lin_reg.predict(x_test)
plt.plot(x_test, y_test, "b.")
plt.plot(x_test,y_pred,"k--")
plt.xlabel("Predictor variable")
plt.ylabel("Response Variable")
residual=(y_test-y_pred)**2
sum(residual["platelets"]) #489272557690.0972

#quadratic
poly = PolynomialFeatures(2, include_bias=False) # argument here is the highest degree you want for your model; here we have 2 for a quadratic model
x_new = poly.fit_transform(x_train)
lin_reg = LinearRegression()
lin_reg.fit(x_new,y_train)
print([lin_reg.intercept_,lin_reg.coef_[0]])#a=246391.04984573 b=-1.20111246e+01 c=2.71094612e-03
x_test_new = poly.fit_transform(x_test)
y_pred = lin_reg.predict(x_test_new)
plt.plot(x_test, y_test, "b.")
plt.plot(x_test,y_pred,"k--")
plt.xlabel("Predictor variable")
plt.ylabel("Response Variable")
residual=(y_test-y_pred)**2
sum(residual["platelets"]) #490804335614.8889

#cubic
poly = PolynomialFeatures(3, include_bias=False) # argument here is the highest degree you want for your model; here we have 2 for a quadratic model
x_new = poly.fit_transform(x_train)
lin_reg = LinearRegression()
lin_reg.fit(x_new,y_train)
print([lin_reg.intercept_,lin_reg.coef_[0]])#a=242663.59918467 b=3.53007357e+00 c=-4.83308113e-03 d=7.34101062e-07
x_test_new = poly.fit_transform(x_test)
y_pred = lin_reg.predict(x_test_new)
plt.plot(x_test, y_test, "b.")
plt.plot(x_test,y_pred,"k--")
plt.xlabel("Predictor variable")
plt.ylabel("Response Variable")
residual=(y_test-y_pred)**2
sum(residual["platelets"]) #491966262897.5837

#glm
lin_reg = LinearRegression()
lin_reg.fit(np.log(x_train),y_train)
print([lin_reg.intercept_,lin_reg.coef_]) #a=211947.0530173 b=5892.13964827
y_pred = lin_reg.predict(np.log(x_test))
plt.plot(x_test, y_test, "b.")
plt.plot(x_test,y_pred,"k--")
plt.xlabel("Predictor variable")
plt.ylabel("Response Variable")
residual=(y_test-y_pred)**2
sum(residual["platelets"]) #485925037113.6133

#glm log(y)
lin_reg = LinearRegression()
lin_reg.fit(np.log(x_train),np.log(y_train))
print([lin_reg.intercept_,lin_reg.coef_]) #a=12.17857821 b=0.02235302
y_pred = lin_reg.predict(np.log(x_test))
y_pred=np.exp(y_pred)
plt.plot(x_test, y_test, "b.")
plt.plot(x_test,y_pred,"k--")
plt.xlabel("Predictor variable")
plt.ylabel("Response Variable")
residual=(y_test-y_pred)**2
sum(residual["platelets"]) #564539865998.4521




























