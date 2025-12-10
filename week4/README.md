# Week 4 - Group project


## Table of Contents
- [**Week 4 - Group project**](#week-4---group-project)
  - [**Table of Contents**](#table-of-contents)
  - [**Project Structure**](#project-structure)
  - [**Languages Used**](#languages-used)
  - [**Installation**](#installation)
  - [**Dependencies**](#dependencies)
  - [**Brief Description**](#brief-description)
  - [**Scripts List**](#scripts-list)
  - [**Basic Script Usage**](#basic-script-usage)
  - [**Author and Contact**](#author-and-contact)


## Project Structure
The structure of week4 is shown below:

```
./week4/
│
├── code/
│   ├── PP_Regress_loc.R
│   └── TAutoCorr.R
│
├── data/
│   ├── EcolArchives-E089-51-D1.csv
│   └── KeyWestAnnualMeanTemperature.RData
│
├── results/
│   └── (currently empty — ignored by .gitignore)
│
├── .gitignore
└── group_assessment2.pdf
```

## Languages Used
```
R
```

## **Installation**
```
Ensure that you are using a UNIX-based environment.

git clone git@github.com:RayHan0305/05_Electric_Emus.git
```

## **Dependencies** 
Most of the scripts only require base R and can be run directly in the terminal using Rscript.

Installation: `sudo apt install r-base` (Run in the terminal)

## Brief Description
In this week, we focus on applying statistical and ecological modelling techniques using R. The main learning objectives include:

1. Reading and processing real ecological datasets
2. Time series data handling and visualization
3. Autocorrelation analysis in biological time series
4. Spatial and local regression modelling
5. Interpreting ecological and environmental data using regression
6. Improving computational reproducibility using structured project folders
7. Understanding relationships between climate variables and ecological responses
8. These works are based on CMEE practical materials and provided datasets


## Scripts List
| Script Name        | Description                                                          | Arguments |
| ------------------ | -------------------------------------------------------------------- | --------- |
| PP_Regress_loc.R   | Performs local regression analysis on ecological and climate-related data | None      |
| TAutoCorr.R        | Performs time-series autocorrelation analysis on temperature data    | None      |


## Basic Script Usage
```
# in terminal
Rscript TAutoCorr.R
Rscript PP_Regress_loc.R
```

## Dependencies
Most scripts require base R, with some additional commonly used statistical packages.
Install R: `sudo apt install r-base`


# Author and Contact
Name: Paruit Lisa, Zhiquan Kang, Ximan Ding, Lawson-Hale Tasha L, Ruixuan Han

Institution: CMEE Programme, Imperial College London