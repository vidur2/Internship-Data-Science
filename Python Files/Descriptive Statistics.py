'''
Descriptive Statistics
Vidur Modgil
Internship
'''

#Imports
from Commands import * 
from DescriptiveAnalysisCommands import *
from matplotlib import pyplot as plt

def main():
    # Opens and reads file into a dictionary
    data, isSuccess = readCSV('/Users/vidurmodgil/Desktop/DATA/Internship/Internship-Data/VIDURSAMPLE.csv')
    # Gets row headers and removes the matchkey
    variables = list(data.keys())
    variables.remove('MATCHKEY')
    # Empty list of statistics
    listOfStatistics = []
    # Iterates through list
    for row in variables:
        # Finds the descriptive statistics, and gets them into string form
        # Finds median and mean
        median = str(getMedian(data, row))
        
        meanValue = mean(data, row)
        # Rounds mean to make sure fits in table form
        meanValue = round(meanValue, 4)
        meanValue = str(meanValue)
        
        # Finds minimum and maximum of each row
        minimum, maximum = minAndMax(data, row)

        # Finds Standard Deviation and round
        standardDev = standardDeviation(data, row)
        standardDev = round(standardDev, 4)

        # Casts standard deviation, minimum, and maximum to string
        standardDev = str(standardDev)
        minimum = str(minimum)
        maximum = str(maximum)
        # Saves to list and appends list to another list
        singleRow = [median, meanValue, minimum, maximum, standardDev]
        listOfStatistics.append(singleRow)
        
        # Prints Descriptive Statistics in formatted statement
        print(
            f"\nDescriptive Statistics of {row}:\n" + 
            f"The median of {row} is {median}\n" + 
            f"The mean of {row} is {meanValue}\n" + 
            f"The min of {row} is {minimum} and the max is {maximum}\n" + 
            f"The standard deviation of {row} is {standardDev}\n" 
        )
    
    # Plots table in matplotlib
    statTable = plt.table(listOfStatistics, loc=9, colLabels=['Median', 'Mean', 'Min', 'Max', 'Standard Dev'], rowLabels=variables)
    statTable.auto_set_font_size(False)
    statTable.set_fontsize(8)
    statTable.scale(1, 1)
    plt.axis('off')
    plt.show()

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
if __name__ == '__main__':
    main()
