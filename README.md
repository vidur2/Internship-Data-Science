# Consumer Credit Project
## Overview
The purpose of the code as a whole is to take consumer credit data and generate a prediction on their probability of default. The code here uses 4 data points per consumer(Trades, Revolving Balance, Balance Percent Satisfied, and Age) to predict an outcome(represented by a 0/1 variable, 0 being no default, 1 being default). Because the prediction is being generated based on credit data where the 0/1 outcome(goodbad) has already happened, the profitability of the prediction can be tested by comparing the probability the model gives of default to the actual default value.

# User Guides
There are two different versions of the productionalized code, the client code and the data scientist code.
There READMEs can be found here:
1. [Data Science README.md](OverviewForDataScientists.md)
2. [Client README.md](ClientOverview.md)
