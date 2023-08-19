setwd("~/Documents/School/952986478/MATH839 Applied Regression Analysis/hw1")

#Imports
library(readr)
library(ggplot2)
mpg <- read_csv("MilesPerGallonMPV.csv")

#Simple Linear Regression
slr_mpg <- lm(formula = Displacement ~ MPG, data = mpg)
summary(slr_mpg)
ggplot(data=mpg, aes(x=Displacement,y=MPG)) + 
  geom_point(color="green") +
  geom_smooth(method='lm',formula = y~x)

#ANOVA
anova <- aov(formula = Displacement ~ MPG, data = mpg)
summary(anova)

#Confidence Intervals
groupwise
