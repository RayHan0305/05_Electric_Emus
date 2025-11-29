############################################################
# Question: Are temperatures of one year significantly correlated
# with the next year (successive years), across years in a given location?
#
# DESCRIPTION: This script calculates a premutation test to obtain the actual
# Correlation Coefficient of the temperature data.
#
# The script: TAutoCorr.R
#
#
# INPUT: KeyWestAnnualMeanTemperature.RData
#
#
# OUTPUT: permuted correlation results
#
#
# AUTHOR: Natasha Lawson-Hale
# DATE: 29rd November 2025
############################################################
# Clear environment and load data frame
rm(list = ls())
Florida_data <- load("../data/KeyWestAnnualMeanTemperature.RData")
#explore data frame
ls()
nrow(ats)
class(ats)
head(ats)
summary(ats)
tail(ats)
plot(ats)

ls()
library(ggplot2)
#check for normal distribution
hist(x)
qqnorm(x)
qqline(x, col = "red") # line for easy comparison

# Define variables and the number of permutations
y <- ats$Year
x <- ats$Temp
n_permutations <- 10000
ls()
class(x)
#Create lagged variables for correlation
X <- x - [length(x)]
X_x <- x[-1]

#observed_coefficient
obs_coef <- cor(X, X_x, use = "everything", method = c("pearson"))
cat(obs_coef)
