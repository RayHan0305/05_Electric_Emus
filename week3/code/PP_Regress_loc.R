#!/usr/bin/env Rscript
# Author: zhiquan kang (zk425@ic.ac.uk)
# To run the script:
# Rscript PP_Regress_loc.R
#
# No arguments are required for running this script.

library(ggplot2) 
library(dplyr)
library(broom)
library(purrr)

rm(list=ls())

#setting seed for repeatability
set.seed(12345)

#read data in
data <- read.csv("../data/EcolArchives-E089-51-D1.csv")

# Combine all feeding types into one dataset and log transform predator and prey mass
data_combined <- data %>%
  mutate(
    LogPreyMass = log10(Prey.mass),
    LogPredatorMass = log10(Predator.mass)
  )

# find which groups have fewer than 3 points, these will show up as NA when calculating lm coefficients  
data_combined %>%
  group_by(Type.of.feeding.interaction, Predator.lifestage) %>%
  summarize(count = n())

LM <- data_combined %>%
  dplyr::select(Record.number, Predator.mass, Prey.mass, Predator.lifestage, Type.of.feeding.interaction, Location) %>%
  group_by(Type.of.feeding.interaction, Predator.lifestage, Location) %>%
  filter(n() > 1) %>%
  filter(sd(Prey.mass) > 0) %>%
  do(mod = lm(Predator.mass ~ Prey.mass, data = .)) %>%
  mutate(
    Regression.slope = summary(mod)$coefficients[2, 1],
    Regression.intercept = summary(mod)$coefficients[1, 1],
    R.squared = summary(mod)$adj.r.squared,
    Fstatistic = summary(mod)$fstatistic[1],
    P.value = summary(mod)$coefficients[2, 4]
  ) %>%
  dplyr::select(-mod)


#save linear model coefficients output by location
write.csv(LM, "../results/PP_Regress_bylocation_Results.csv", row.names = FALSE)