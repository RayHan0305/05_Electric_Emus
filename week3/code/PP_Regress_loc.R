#!/usr/bin/env Rscript

## PP_Regress_loc.R
## Regression analysis by Feeding type x Predator life stage x Location

if (!require("dplyr")) install.packages("dplyr", repos = "https://cloud.r-project.org")
library(dplyr)

pp_data_path   <- "../data/EcolArchives-E089-51-D1.csv"
pp_results_loc <- "../results/PP_Regress_loc_Results.csv"

PP <- read.csv(pp_data_path, stringsAsFactors = FALSE)

PP <- PP %>%
  filter(!is.na(Prey.mass),
         !is.na(Predator.mass),
         Prey.mass > 0,
         Predator.mass > 0)

PP$Predator.lifestage <- factor(PP$Predator.lifestage)
PP$Type.of.feeding.interaction <- factor(PP$Type.of.feeding.interaction)
PP$Location <- factor(PP$Location)

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


reg_results_loc <- PP %>%
  group_by(Type.of.feeding.interaction,
           Predator.lifestage,
           Location) %>%
  filter(n() >= 2) %>%        # skip tiny groups where lm() would fail
  do(fit_single_lm(.)) %>%
  ungroup()

write.csv(reg_results_loc, pp_results_loc, row.names = FALSE)
