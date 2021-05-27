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
    for i in range(len(dataSet)-1):
        dataSet[i] = float(dataSet[i])
    if remainder == 0:
        median = dataSet[(len(dataSet)-1)/2]
    else:
        point1 = dataSet[int((len(dataSet)-1)/2 + 0.5)] 
        point2 = dataSet[int((len(dataSet)-1)/2 - 0.5)] 
        median = (point1 + point2)/2
    return median