'''
Descriptive Statistics
Vidur Modgil
Internship
'''

#Imports
import pandas
from Commands import * 
from DescriptiveAnalysisCommands import *
from matplotlib import pyplot as plt

def main():
    data, isSuccess = readCSV('/Users/vidurmodgil/Desktop/DATA/Internship/Internship-Data/VIDURSAMPLE.csv')
    pandas.DataFrame.from_dict(data)
    variables = list(data.keys())
    variables.remove('MATCHKEY')
    listOfStatistics = []
    for row in variables:
        median = str(getMedian(data, row))
        meanValue = mean(data, row)
        meanValue = round(meanValue, 4)
        meanValue = str(meanValue)
        minimum, maximum = minAndMax(data, row)
        standardDev = standardDeviation(data, row)
        standardDev = round(standardDev, 4)
        standardDev = str(standardDev)
        minimum = str(minimum)
        maximum = str(maximum)
        singleRow = [median, meanValue, minimum, maximum, standardDev]
        listOfStatistics.append(singleRow)
        print(
            f"\nDescriptive Statistics of {row}:\n" + 
            f"The median of {row} is {median}\n" + 
            f"The mean of {row} is {meanValue}\n" + 
            f"The min of {row} is {minimum} and the max is {maximum}\n" + 
            f"The standard deviation of {row} is {standardDev}\n" 
        )
    statTable = plt.table(listOfStatistics, loc=9, colLabels=['Median', 'Mean', 'Min', 'Max', 'Standard Dev'], rowLabels=variables)
    statTable.auto_set_font_size(False)
    statTable.set_fontsize(8)
    statTable.scale(1, 1)
    plt.axis('off')
    plt.show()
if __name__ == '__main__':
    main()
