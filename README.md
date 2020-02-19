# Big_Data_Project

## Project Name: StockAnalysis
### Course: Big Data
### Semester : Spring-2020
### Section : 02
### Project Number: 04
### Team Members:
1. Rohith Bharadwaj - S534783@nwmissouri.edu
1. Samanth Gourineni- S534569@nwmissouri.edu
1. Deepak Sai Krishna Jayanthi - S534843@nwmissouri.edu 

## Links:
1. [Github hub repo link](https://github.com/rohithbharadwaj/Big_Data_Project)
1. [Github issue link](https://github.com/rohithbharadwaj/Big_Data_Project/issues/1)
1. [Dataset Link](https://www.kaggle.com/cuicuifeng/new-york-stock-exchange-daily-price)

## Introduction: 
We are working on the data of the New York stock exchange, Where we can calculate the Maximum/Minimum/Sum/Count of the opening_price, closing_price and volume of stocks depending on the company(stock_symbol) by filtering with date.

## Data Source:
* Format: .CSV format
* Key attributes: This dataset has  stock symbols(company code), date, stock volume and stock price.
* Volume: This dataset has very huge volume of data about 448MB, it has several CSV file each with a volume of about approx 50 MB, having records 825936 with 9 columns.
* Variety: Structured data in excel format.
* Velocity: Velocity of data inflow is constant as data is generated day by day for each stock symbol.
* Veracity: The dataset is not messy and we can easily filter the values through dates or volumes or stock symbols(company code).
* Value: This dataset gives us information about the stock price details and volume of each company every day with respect to the New York stock exchange.

## Big Data Problems
* For each company, find the maximum stock volume.
* For each company, find the minimum stock volume.
* For each company, find the sum stock volume.


## Rohith Bharadwaj
* For each company, find the Maximum stock volume.



## Samanth Gourineni
* For each company, find the Minimum stock volume.
* Input Data: (https://github.com/rohithbharadwaj/Big_Data_Project/blob/master/Data/NYSE_daily_prices_C.csv)
* For each company, the minimum of stock volume is 0.
* Intermediate pairs:

exchange : NYSE

stock_symbol : CAE

date : 2/12/2010

stock_price_open : 8.42

stock_price_high : 8.76

stock_price_low : 8.39

stock_price_close : 8.71

stock_volume : 40200

stock_price_adj_close : 8.71

*Final Pairs:

stock_symbol : CAE

stock_volume : 40200

* Type of chart : Bar Graph

## Deepak Sai Krishna Jayanthi 
* For each company, find the sum stock volume.
* Input Data: (https://github.com/rohithbharadwaj/Big_Data_Project/blob/master/Data/NYSE_daily_prices_C.csv)
* For each company, the sum of stock volume is 713647300.
* Intermediate pairs:

exchange : NYSE

stock_symbol : CAE

date : 2/12/2010

stock_price_open : 8.42

stock_price_high : 8.76

stock_price_low : 8.39

stock_price_close : 8.71

stock_volume : 40200

stock_price_adj_close : 8.71

*Final Pairs:

stock_symbol : CAE

stock_volume : 40200

* Type of chart : Bar Graph