'''
File for commands for finding parts of data set such as mean median mode
Vidur Modgil
'''

def getMedian(table, row):
    dataSet = table[row]
    dataSet.sort()
    median = None
    length = len(dataSet) - 1
    remainder = length % 2
    if remainder == 0:
        median = dataSet[(len(dataSet)-1)/2]
    else:
        point1 = dataSet[int((len(dataSet)-1)/2 + 0.5)] 
        point2 = dataSet[int((len(dataSet)-1)/2 - 0.5)] 
        median = (point1 + point2)/2
    return median

def mean(table, row):
    dataSet = table[row]
    return sum(dataSet)/len(dataSet)

def minAndMax(table, row):
    dataSet = table[row]
    dataSet.sort()
    return dataSet[0], dataSet[len(dataSet) - 1]

def standardDeviation(table, row):
    dataSet = table[row]
    meanValue = mean(table, row)
    deviations = []
    for element in dataSet:
        deviations.append((meanValue - element)**2)
    return (sum(deviations)/len(deviations))**0.5