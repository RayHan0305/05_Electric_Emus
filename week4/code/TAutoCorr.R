#!/usr/bin/env Rscript

# Language: R
# Script: TAutoCorr.R
# Des: Test lag-1 autocorrelation in annual mean temperature (Key West, Florida) using a permutation test
# Usage: Rscript TAutoCorr (in terminal) or source("TAutoCorr.R") (in R console)
# Date: Oct, 2025
# Author: Ruixuan Han, Lawson-Hale Tasha L

# Permutation test for lag-1 autocorrelation in annual mean temperature
# Question: Are temperatures in one year correlated with the next year?

rm(list = ls())

## 1. Load data -----------------------------------------------------------
## This .RData should contain an object called 'ats' with columns Year, Temp
load("../data/KeyWestAnnualMeanTemperature.RData")

if (!exists("ats")) {
  stop("Object 'ats' not found in KeyWestAnnualMeanTemperature.RData")
}

# Inspect briefly (optional)
# print(head(ats))

years <- ats$Year
temps <- ats$Temp

# Remove missing temperatures if any
ok <- !is.na(temps)
years <- years[ok]
temps <- temps[ok]

n <- length(temps)
if (n < 3) stop("Not enough years to compute lag-1 autocorrelation")

## 2. Compute observed lag-1 correlation ---------------------------------
# x: all temps except last; y: all temps except first -> (n - 1) pairs
x <- temps[-n]
y <- temps[-1]

r_obs <- cor(x, y, method = "pearson")
cat("Observed lag-1 correlation (r_obs):", r_obs, "\n")

## 3. Permutation test ----------------------------------------------------
set.seed(1234)           # for reproducible results
nperm <- 10000
r_perm <- numeric(nperm)

for (i in seq_len(nperm)) {
  # Randomly permute the temperature series (breaks temporal order)
  temps_perm <- sample(temps, replace = FALSE)
  xp <- temps_perm[-n]
  yp <- temps_perm[-1]
  r_perm[i] <- cor(xp, yp, method = "pearson")
}

## 4. Empirical p-values --------------------------------------------------
# One-sided (H1: positive autocorrelation)
p_one <- mean(r_perm >= r_obs)

# Two-sided (H1: non-zero autocorrelation)
p_two <- mean(abs(r_perm) >= abs(r_obs))

cat("Empirical p-value (one-sided):", p_one, "\n")
cat("Empirical p-value (two-sided):", p_two, "\n")

## 5. Save results --------------------------------------------------------
if (!dir.exists("../results")) dir.create("../results", recursive = TRUE)

# Save numeric results to a small text file
res_text <- sprintf(
  "Lag-1 autocorrelation in annual mean temperature\n\nObserved r = %.4f\nOne-sided p = %.5f\nTwo-sided p = %.5f\nN permutations = %d\n",
  r_obs, p_one, p_two, nperm
)
writeLines(res_text, "../results/TAutoCorr_results.txt")

## 6. Plot null distribution and observed r -------------------------------
pdf("../results/TAutoCorr_histogram.pdf", width = 7, height = 5)

hist(r_perm,
     breaks = 40,
     main = "Lag-1 Autocorrelation\nPermutation Test",
     xlab = "Correlation coefficient under null (permuted)",
     col = "grey80",
     border = "white")

abline(v = r_obs, col = "red", lwd = 3)

text(x = r_obs,
     y = par("usr")[4] * 0.9,
     labels = sprintf("Observed r = %.3f\np(one-sided) = %.4f", r_obs, p_one),
     pos = 4,
     col = "red")

dev.off()

cat("Saved:\n  ../results/TAutoCorr_histogram.pdf\n  ../results/TAutoCorr_results.txt\n")
