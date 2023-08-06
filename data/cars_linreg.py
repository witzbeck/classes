"""
Created on Mon Mar  1 21:28:02 2021

@author: Fr333y3d3a
"""

##Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
"""
cars = pd.read_csv("./cars.csv")

##Making cylinder number categorical
cars["cylinders"] = cars["cylinders"].astype("category")

##Horsepower not taking reciprocal function - casting as float
cars["horsepower"] = cars["horsepower"].astype(float)

##Axes
a = cars["mpg"]
b = cars["horsepower"]
c = cars["origin"]
"""
import seaborn as sb
sb.pairplot(cars)
"""
##Split frames

am = cars.loc[cars["origin"] == "American"]
ja = cars.loc[cars["origin"] == "Japanese"]
eu = cars.loc[cars["origin"] == "European"]

mean_am, mean_ja, mean_eu = np.mean(am), np.mean(ja), np.mean(eu)

col = cars.columns.tolist()

##Confidence intervals are significant enough to reject the null hypothesis, 
from statsmodels.stats.multicomp import pairwise_tukeyhsd
print(pairwise_tukeyhsd(cars["mpg"], cars["origin"]))
print(pairwise_tukeyhsd(cars["mpg"], cars["cylinders"]))

##Model
model = smf.ols('mpg ~ origin + np.reciprocal(engine_displacement) + np.reciprocal(horsepower) + np.log(acceleration) + cylinders + model_year', data = cars)
res = model.fit()

##Residuals
sid = cars["mpg"] - res.fittedvalues
print(res.summary())

plt.scatter(cars.index,sid)
plt.xlabel("Index")
plt.ylabel("Residual")

plt.scatter(890.9183*np.reciprocal(cars["horsepower"]), sid)
plt.xlabel("Weighted Contribution of Horsepower to Model")
plt.ylabel("Residuals")

import statsmodels

statsmodels.stats.stattools.durbin_watson(sid)

#Comparing variables
def plot(x,y):
    xi = x
    yi = y
    plt.scatter(xi, yi, marker=("1"))
    plt.xlim((min(x)-5,max(x)+5))
    plt.ylim((min(y)-5,max(y)+5))
   
    xlab = input("Please enter desired x axis label:")
    plt.xlabel(xlab)
    ylab = input("Please enter desired y axis label:")
    plt.ylabel(ylab)


##Experimenting with 3D plotting
a = cars["acceleration"]
b = cars["horsepower"]
c = cars["mpg"]

x = pd.DataFrame([a],[b])
y = pd.DataFrame([b],[c])
z = pd.DataFrame([c],[a])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
cmcw = plt.get_cmap("coolwarm")

ax.scatter(x,y,z, zdir = "z", s=5, c = -z, cmap = cmcw)

ax.set_xlabel('Acceleration from 0-60mph (s)')
ax.set_ylabel('Horsepower')
ax.set_zlabel('Miles per Gallon')


plt.show()
