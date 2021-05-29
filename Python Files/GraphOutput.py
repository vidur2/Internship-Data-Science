'''
Python File to graph Histograms/Bar Charts
Vidur Modgil
Internship
'''

# Imports
from matplotlib import pyplot as plt
from Commands import *

def plotHistogram(table, row, binNumber):
    dataSet = table[row]
    plt.hist(dataSet, bins=binNumber)

def plotBarChart(table, row):
    dataSet = table[row]
    key = gatherSet(table, row)
    numberOfBins = len(key)
    plt.hist(dataSet, bins=numberOfBins)

def main():
    data, isSuccess = readCSV('/Users/vidurmodgil/Desktop/DATA/Internship/Internship-Data/VIDURSAMPLE.csv')
    allKeys = data.keys()
    discreetKeys = []
    continiousKeys = []
    for key in allKeys:
        dataSet = data[key]
        dataSet.sort()
        dataSet = set(dataSet)
        check = True
        for element in dataSet:
            if int(element) != element:
                check = False
                break
        if check == True:
            discreetKeys.append(key)
        else:
            continiousKeys.append(key)
    for key in continiousKeys:
        plotHistogram(data, key, 30)
        plt.show()
    for key in discreetKeys:
        plotBarChart(data, key)
        plt.show()

if __name__ == '__main__':
    main()