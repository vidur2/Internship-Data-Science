# Consumer Credit Project
## Overview
The purpose of the code as a whole is to take consumer credit data and generate a prediction on their probability of default. The code here uses 4 data points per consumer(Trades, Revolving Balance, Balance Percent Satisfied, and Age) to predict an outcome(represented by a 0/1 variable, 0 being no default, 1 being default). Because the prediction is being generated based on credit data where the 0/1 outcome(goodbad) has already happened, the profitability of the prediction can be tested by comparing the probability the model gives of default to the actual default value.
## How to run and view the code
The file that you need to run is called 'Final Consolidation 1.py', located in the directory 'Pandas Python.' Running the code can be done using Python 3.8 or higher. All one needs to do is to press the run button in order for the program to run. Most of the output will be shown as text based output, however, the graphs should appear as popout windows.
## Understanding/Navigating the Output
### File information Generation
The first things done by the program are:
1. Generate a File Layout
2. Generate Descriptive Statistics

#### File Layout
All a file layout does is give the column names and their sizes, and the type of data contained in those files(ex. CRELIM has 100,000 rows, and has decimal numbers, the file layout will say that)

#### Descriptive Statistics
A descriptive statistic is basically a marker of the dataset, such as the mean(average) or median. Running the descriptive statistics will return all of these markers.

### Histogram/Bar Chart Generation
#### Purpose
The Histograms and Bar Charts are generated to show the amount of times a certain value for a certain variable appears. This will allow for better fitting of the data. In addition, by seeing the type of distribution(normal, monotonic, etc), one is also able to see how good of an indicator it might be for probability of default. For example a monotonic(only increasing/decreasing) variable may be a better indicator of default than a variable with a normal distribution.
#### Navigation
Once done seeing a histogram/bar chart, you can move on to the next one by closing out of the first one. The next one will immediatly pop out in addition to any text output that may also have been programmed to print in between the graphs.

### Binning of the Data
#### Bin Generation
After the plotting of the data, the four variables are put into 'bins', or categories based on user-generated ranges(called ordinal, or ORD[Variable Name]) and frequency(called ranked, or RANK[Variable Name]). The text output are the descriptive statistics of these binned variables.

### Model Generation
#### Random Splitting of the data
To generate and test predictions, we need two different datasets: one to train the data, and one to test it. In order to get these two datasets, we need to split the data into train and test categories.

In order to avoid any biases that may have been present during the collection, or our analysis of the data, the file needs to be randomly split into these two sets. The file is split this way 80/20, the 80% being the training data.

#### Logistic Regression Using sklearn
The current model is built using a package called sklearn. The Logistic Regression function was used to fit the data, due to the output needing to be 0/1. This is because of the shape of a logistic curve: There are two limits. In our case, the upper limit is the 1, or defualt case, and the lower limit is 0. The first output is the probability of default.

<img src="https://user-images.githubusercontent.com/55110959/123127808-9cce4700-d418-11eb-9aeb-ce4e5662151c.png" width=300></img>

#### Cutoff Points
The final part of the code deals with finding the cutoff points and generating the Profit Per customer. The cutoff points basically decide which is a 0(gets credit) and which is a 1(does not get credit) based on the Probability of default calculated in the last section. The profit from a given customer is calculated using the formula: (Number of Predicted Non Defaulters who did not Default) * 500 - (Number of Predicted Non Defaulters who did Default) *  0.5 * Credit Line Amount. The optimal cutoff point found is at a 30% probabilty of default.

