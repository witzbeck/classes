#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 14:45:40 2021

@author: Fr333y3d3a
"""

import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.tools.eval_measures import rmse
import pandas as pd

oxy = pd.read_csv("~/Documents/School/952986478/MATH839 Applied Regression Analysis/hw1/OxyDistillationMPV.csv")
oxy.columns = ["Purity","Hydrocarbon"]


model = ols("Purity ~ Hydrocarbon",data=oxy)
results = model.fit()

print(results.summary())

anova = anova_lm(results)
print(anova,"\n")

#sns.regplot(x="Hydrocarbon",y="Purity",data=oxy)

x = oxy.iloc[:,1]
y = oxy.iloc[:,0]
ypred = results.predict(x)

def sum_squares(y,ypred):
    squares=[]
    for i in range(len(y)):
        squares.append((y[i]-ypred[i])**2)
    return sum(squares)

def arrr_squared(y, ypred):
        
    y_bar =  pd.Series(y).mean()
    y_bar_list = [y_bar for _y in y]
    
    explained_variance = sum_squares(y,ypred)
    total_variance = sum_squares(y,y_bar_list)
    
    rsq = 1-(explained_variance/total_variance)
    return rsq
    
#print("R^2 value as calculated w/ my functions:",arrr_squared(y, ypred),"\n",
 #     "R^2 value as calculated by the statsmodels package:",results.rsquared)



root_mean = rmse(y,ypred)
print("\nRMSE:",root_mean,"\n")

def hijack_pred(x,results,add_x_value):
    x_list = list(x)
    x_list.append(add_x_value)
    
    x = pd.Series(x_list,name="Hydrocarbon")
    ypredictions = results.predict(x)
    return_value = ypredictions[len(ypredictions)-1]
    return return_value

pur = 1.0
pred_value = hijack_pred(x,results,pur)

print(f"Predicted value @ Hydrocarbon% = {pur}:",pred_value)

def make_95ci(value,stddev):
    low = value - 2*stddev
    high = value + 2*stddev
    return [low,high]

print("\nIf the standard error represents the std dev,\na 95% confidence interval could be shown by \ngoing up and down two std devs from the predicted value.\n")
print(make_95ci(pred_value,root_mean),"\nError used: RMSE")

  
    