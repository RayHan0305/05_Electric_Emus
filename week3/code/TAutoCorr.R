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
#Import
library(ggplot2)
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
X <- x[-length(x)]
X_x <- x[-1]

#observed_coefficient
obs_coef <- cor(X, X_x, use = "everything", method = c("pearson"))
cat(obs_coef)
# resulting observed correlation coefficient= 0.3261697

#permutation function
calc_permuted <- function(X, X_x, n_permutations) {
  permuted <- sapply(1:n_permutations, function(i) {
    
    # shuffle using sample
    # The lagged year temperatures are shuffled to break year on year dependency
    X_x_shuffled <- sample(X_x)
    
    # Calculate the Pearson correlation for the new random pairing
    return(cor(X, X_x_shuffled, use = "everything", method = ("pearson")))
  })
return(permuted)
  }

#calling calc_permuted func and checking results
permuted_coef <- calc_permuted(X, X_x, n_permutations = 10000)
print(head(permuted_coef))
print(tail(permuted_coef))
summary(permuted_coef)
sd(permuted_coef)

#calculating the pvalue
p_val <- sum(abs(permuted_coef) >= abs(obs_coef)) / (1 + n_permutations)

#calculating the z-score
z_score <- (obs_coef-mean(permuted_coef))/sd(permuted_coef)

#save the results to a data frame and .csv
results_perm <- data.frame(parameter = c("obs_coef", "n_permutations", "P_val", "Z-score"),
value = c(obs_coef, n_permutations, p_val, z_score)
)
print(results_perm)

write.csv(results_perm, file = "../results/perm_coef_data.csv", row.names = FALSE)