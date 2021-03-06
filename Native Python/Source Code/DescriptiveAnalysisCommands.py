'''
File for commands for finding parts of data set such as mean median mode
Vidur Modgil
'''
# Basic Imports
from freqCommands import *
from matplotlib import pyplot as plt
# Function to find median given table and row name
def getMedian(table, row):
    # Creates a pointer to a specific row
    dataSet = table[row]
    # Sorts the row from least value to greatest
    dataSet.sort()
    
    # Initializes median value
    median = None
    
    # Gets max key value of dataSet
    length = len(dataSet) - 1
    remainder = len(dataSet) - 1 % 2

    # If the remainder is 0, then finds median directly
    if remainder == 0:
        median = dataSet[(len(dataSet)-1)/2]
    
    # Otherwise, averages two values next to mean value, but averaged
    else:
        point1 = dataSet[int((len(dataSet)-1)/2 + 0.5)] 
        point2 = dataSet[int((len(dataSet)-1)/2 - 0.5)] 
        median = (point1 + point2)/2
    
    # Returns the median
    return median

# Finds median of data set
def mean(table, row):
    # Pointer to specific row
    dataSet = table[row]
    # Returns mean of data set
    return sum(dataSet)/len(dataSet)

def minAndMax(table, row):
    # Pointer to row
    dataSet = table[row]
    # Sort data set in ascending order
    dataSet.sort()
    # Returns least and greatest Values in dataset
    return dataSet[0], dataSet[len(dataSet) - 1]

def standardDeviation(table, row):
    # Pointer to row
    dataSet = table[row]

    # Finds meand of Dataset
    meanValue = mean(table, row)
    # Initializes empty list
    deviations = []
    for element in dataSet:
        # Appends deviation calculation
        deviations.append((meanValue - element)**2)
    
    # Calculates and returns standard deviation through a calc of mean and sqrt
    return (sum(deviations)/len(deviations))**0.5

# General function to plot descriptive statistics in a table
def descriptiveDataGraphing(columnNames):
    # Reads in file
    data, isSuccess = readCSV('/Users/vidurmodgil/Desktop/DATA/Internship/Internship-Data/VIDURSAMPLE.csv')
    
    # Initializes empty list
    listOfStatistics = []

    # Iterates through entered column names
    for row in columnNames:
        # Gets median and casts it to string
        median = str(getMedian(data, row))

        # Mean value is found, and rounded to 4 decimal places
        meanValue = mean(data, row)
        meanValue = round(meanValue, 4)
        # Casts mean value to string
        meanValue = str(meanValue)

        # Finds minimum and maximum of each row
        minimum, maximum = minAndMax(data, row)

        # Finds standard deviation, rounds it, and casts it to string
        standardDev = standardDeviation(data, row)
        standardDev = round(standardDev, 4)
        standardDev = str(standardDev)

        # Minimum and maximum are casted to strings
        minimum = str(minimum)
        maximum = str(maximum)

        # Generates a list based on median, mean, min, max, and standard deviation
        singleRow = [median, meanValue, minimum, maximum, standardDev]
        # Appended to a list of statistics
        listOfStatistics.append(singleRow)
    
    # Plots a table using matplotlib
    statTable = plt.table(listOfStatistics, loc=9, colLabels=['Median', 'Mean', 'Min', 'Max', 'Standard Dev'], rowLabels=columnNames)
    statTable.auto_set_font_size(False)
    statTable.set_fontsize(8)
    statTable.scale(1, 1)
    plt.axis('off')
    plt.show()