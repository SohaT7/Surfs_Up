# An Analysis of Surfs Up
## Table of Contents
- [Overview of the Analysis](#overview-of-the-analysis)
    - [Purpose](#purpose)
    - [About the Dataset](#about-the-dataset)
    - [Tools Used](#tools-used)
    - [Description](#description)
- [Results](#results)
- [Summary](#summary)
- [Contact Information](#contact-information)

## Overview of the Analysis
### Purpose:
The purpose of this project is to analyse the climate data (temperatures in June and December) in Oahu, Hawaii, in order to gauge if opening up a surf shop there will make for a viable investment or not. 

# About the Dataset:
The dataset for this project comprises of climate data on Oahu, Hawaii, and is contained in the following SQLite database:
 - [hawaii.sqlite](https://github.com/SohaT7/Surfs_Up/blob/main/Resources/hawaii.sqlite)

### Tools Used:
 - Python (Pandas, Numpy, Matplotlib)
 - SQLite
 - SQLAlchemy
 - Flask

### Description:
Using Python and SQLAlchemy, the date column of the Measurements table is filtered for all the temperatures from the particular month.

![query_june](https://github.com/SohaT7/Surfs_Up/blob/main/Images/query_june.png)
![query_dec](https://github.com/SohaT7/Surfs_Up/blob/main/Images/query_dec.png)

The temperatures are then converted to a list, the list converted into a DataFrame, and the summary statistics (minimum temperatures, maximum temperatures, average temperatures, and range of temperatures) then generated from the DataFrame. Matplotlib is used to plot out the temperatures for that month. 

## Results
The summary statistics and plots for temperatures from June and December can be seen below:

<img width="122" alt="image" src="https://github.com/SohaT7/Surfs_Up/blob/main/Images/df_june.png"> <img width="368" alt="image" src="https://github.com/SohaT7/Surfs_Up/blob/main/Images/plot_june.png">


<img width="116" alt="image" src="https://github.com/SohaT7/Surfs_Up/blob/main/Images/df_dec.png"> <img width="339" alt="image" src="https://github.com/SohaT7/Surfs_Up/blob/main/Images/plot_dec.png">

The summary statistics and the plotted graphs for the two months show:
 - The average tempertaure in December is 71 degrees Farenheit, which is 4 degrees lower than June's average temperature (75 degrees F).
 - The plot for June temperatures shows that the frequency of temperatures in June have more of a bell-shaped, normally-distributed curve. This explains the smaller standard deviation of 3.26, as compared to December's 3.7.
 - The weather in June and December can be inferred to be about the same. Decmeber has a higher variance (XXXx) but the two months' temperatures have about the same range (June's 21 degrees and December's 27) and average temperature (June's 74.9 F and December's 71 F).

## Summary
Although the temperatures in Oahu, Hawaii in December vary more than they do in June, the temperatures in the two months do not seem to be drastically different from one another. December still might make into a good month to surf. However, to make a more accurate prediction, we can 
analyse the precipitation patterns for the two months. Moreover, we can compare and contrast the wind speeds between the two months. 

## Contact Information
Email: st.sohatariq@gmail.com
