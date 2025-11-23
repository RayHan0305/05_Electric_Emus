#!/usr/bin/env Rscript
# TAutoCorr.R
# Autocorrelation in Florida annual mean temperature (lag-1)

rm(list = ls())

# Load data
load("../data/KeyWestAnnualMeanTemperature.RData")  # should load 'ats'
head(ats)

# Extract vectors
years <- ats$Year
temps <- ats$Temp

# Observed lag-1 correlation 
# x: all years except last; y: all years except first
x <- temps[-length(temps)]
y <- temps[-1]

r_obs <- cor(x, y)
cat("Observed lag-1 correlation (r_obs):", r_obs, "\n")

# Permutation test 
set.seed(1234)
nperm <- 10000
r_perm <- numeric(nperm)

for (i in 1:nperm) {
  temps_perm <- sample(temps)         # shuffle the temperatures
  x_perm <- temps_perm[-length(temps_perm)]
  y_perm <- temps_perm[-1]
  r_perm[i] <- cor(x_perm, y_perm)
}

# Empirical p-value
p_val <- mean(r_perm >= r_obs)
cat("Empirical p-value:", p_val, "\n")

if (!dir.exists("../results")) dir.create("../results", recursive = TRUE)

pdf("../results/TAutoCorr_histogram.pdf", width = 7, height = 5)
hist(r_perm,
     breaks = 30,
     main = "Lag-1 Autocorrelation\nPermutation Test",
     xlab = "Correlation Coefficient (r_perm)",
     col = "skyblue",
     border = "white")
abline(v = r_obs, col = "red", lwd = 3)
text(r_obs, par("usr")[4] * 0.9,
     labels = sprintf("Observed r = %.3f\np = %.4f", r_obs, p_val),
     pos = 4, col = "red")
dev.off()
cat("Saved: ../results/TAutoCorr_histogram.pdf\n")

