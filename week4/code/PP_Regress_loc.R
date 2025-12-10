#!/usr/bin/env Rscript

# Language: R
# Script: PP_Regress_loc.R
# Des: Perform log10-scale linear regression of Predator.mass ~ Prey.mass
#      by Feeding type × Predator life stage × Location, and save results to CSV.
# Usage 1: Rscript PP_Regress_loc.R (in terminal)
# Usage 2: source("PP_Regress_loc.R") (in R console)
# Output: ../results/PP_Regress_loc_Results.csv
# Date: Dec, 2025
# Author: Zhiquan Kang, Ximan Ding, Paruit Lisa.

# Load required packages
if (!require("dplyr")) install.packages("dplyr", repos = "https://cloud.r-project.org")
library(dplyr)

# Define file paths
pp_data_path   <- "../data/EcolArchives-E089-51-D1.csv"
pp_results_loc <- "../results/PP_Regress_loc_Results.csv"

# Load and clean the data
PP <- read.csv(pp_data_path .., stringsAsFactors = FALSE)

# Remove missing or non-positive values (log10 requires positive data)
PP <- PP %>%
  filter(!is.na(Prey.mass),
         !is.na(Predator.mass),
         Prey.mass > 0,
         Predator.mass > 0)

# Convert grouping variables to factors
PP$Predator.lifestage <- factor(PP$Predator.lifestage)
PP$Type.of.feeding.interaction <- factor(PP$Type.of.feeding.interaction)
PP$Location <- factor(PP$Location)

# Function to fit a single linear model
fit_single_lm <- function(df) {
  m <- lm(log10(Predator.mass) ~ log10(Prey.mass), data = df)
  s <- summary(m)
  
  # F-statistic can be missing (NULL)
  if (is.null(s$fstatistic)) {
    f_val <- NA
    df1 <- NA
    df2 <- NA
    pval <- NA
  } else {
    fstat <- s$fstatistic
    f_val <- unname(fstat[1])
    df1 <- unname(fstat[2])
    df2 <- unname(fstat[3])
    pval <- pf(f_val, df1, df2, lower.tail = FALSE)
  }

  # Return regression statistics as a data frame 
  data.frame(
    n              = nrow(df),
    slope          = unname(coef(m)[2]),
    intercept      = unname(coef(m)[1]),
    r_squared      = s$r.squared,
    F_statistic    = f_val,
    df1            = df1,
    df2            = df2,
    p_value        = pval
  )
}

# Run regressions by group
reg_results_loc <- PP %>%
  group_by(Type.of.feeding.interaction,
           Predator.lifestage,
           Location) %>%
  filter(n() >= 2) %>%        # skip tiny groups where lm() would fail
  do(fit_single_lm(.)) %>%
  ungroup()

write.csv(reg_results_loc, pp_results_loc, row.names = FALSE)
