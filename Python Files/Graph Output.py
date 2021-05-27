'''
Python File to graph Histograms/Bar Charts
Vidur Modgil
Internship
'''

# Imports
from matplotlib import pyplot as plt
from Commands import *

def plotHistogram(table, row):
    dataSet = table[row]
    plt.hist(dataSet, bins=30)
def plotBarChart(table, row):
    dataSet = table[row]
    key = gatherSet(table, row)
    numberOfBins = len(key)
    plt.hist(dataSet, bins=numberOfBins)

def main():
    data, isSuccess = readCSV('/Users/vidurmodgil/Desktop/DATA/Internship/Internship-Data/VIDURSAMPLE.csv')
    plotBarChart(data,'AGE')
    plt.show()
if __name__ == '__main__':
    main()