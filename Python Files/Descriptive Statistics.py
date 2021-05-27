'''
Internship Day 1
Age Variable
'''

#Imports
import pandas
from Commands import * 
from DescriptiveAnalysisCommands import *

def main():
    data, isSuccess = readCSV('**ENTER FILEPATH TO CSV HERE**')
    pandas.DataFrame.from_dict(data)
    variables = list(data.keys())
    variables.remove('MATCHKEY')
    for row in variables:
        median = str(getMedian(data, row))
        meanValue = str(mean(data, row))
        minimum, maximum = minAndMax(data, row)
        standardDev = str(standardDeviation(data, row))
        minimum = str(minimum)
        maximum = str(maximum)
        print(
            f"\nDescriptive Statistics of {row}:\n" + 
            f"The median of {row} is {median}\n" + 
            f"The mean of {row} is {meanValue}\n" + 
            f"The min of {row} is {minimum} and the max is {maximum}\n" + 
            f"The standard deviation of {row} is {standardDev}\n" 
        )
if __name__ == '__main__':
    main()
