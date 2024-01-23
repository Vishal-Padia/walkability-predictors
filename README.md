# Walkability Predictors

This repository builds regression models to predict the EPA's National Walkability Index based on related built environment and area features.

## Dataset
The dataset used is the EPA's 2019 Walkability Index which characterizes Census block groups nationwide based on walkability. The data dictionary is as follows:

## Walkability Features

- D1: Intersection density
- D2: Employment/population balance
- D3: Activity density
- D4: Transit availability
- D5: Job accessibility

## Area Attributes

- TotPop: Total population
- Workers: Employed residents
- CountHU: Housing units
- AutoOwn: Households with 0, 1, or 2+ vehicles

## Target Variable

- NatWalkIndex: EPA National Walkability Index score

## Models
Linear regression and random forest regression models are developed to predict NatWalkIndex using the above features. The goal is to uncover the strongest predictors of block group walkability.
