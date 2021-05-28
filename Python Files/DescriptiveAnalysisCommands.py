'''
File for commands for finding parts of data set such as mean median mode
Vidur Modgil
'''

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