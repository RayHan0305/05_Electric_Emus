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
nrows(ats)
class(ats)
head(ats)
summary(ats)
tail(ats)
plot(ats)
ls()
library(ggplot2)


