'''
Commands to make frequency distribution finding easie
'''
#Imports
import csv
#import pandas
import os
from matplotlib import pyplot as plt
# Command for reading a CSV into a dict
# Uses first row as headers
def readCSV(filepath):
    # Uses filepath exists to make sure code does not have an error
    if (os.path.exists(filepath) == True):
        storedInformation = dict()
        # Reads CSV into a list
        with open(filepath) as openFile:
            csvReader = csv.reader(openFile)
            csvList = list(csvReader)
        # Parses through csv and separates the headers out
        for rows in csvList[0]:
            storedInformation[rows] = []
        headers = csvList[0]
        del csvList[0]

        # Separates the columns into different keys in the dictionary and returns it
        for rows in csvList:
            iterator = 0
            for elements in rows:
                storedInformation[headers[iterator]].append(float(elements))
                iterator = iterator + 1
        return storedInformation, True
    else:
        # If the wrong filepath is entered, returns Nonetype and False to user
        return None, False

def frequencyDist(table, rowName, possibleValues):
    # Initializes Frequency Dictionary
    freq = dict()
    enterableFrequency = []
    # Iterates through the possibleValues set() which was entered
    for i in possibleValues:
        # counter and newInformation are reset every iteration
        counter = 0
        newInformation = []

        # Iterates through the table
        for element in table[rowName]:
            # If the element matches i, then counter is increased
            if float(i) == float(element):
                counter = counter + 1
        # counter is appended to new Information which is added to frequency dictionary
        newInformation.append(counter)
        freq[i] = newInformation
        enterableFrequency.append(newInformation)
    # Plots table using matplotlib
    freqTable = plt.table(enterableFrequency, loc=9, colLabels=['Frequency'], rowLabels=list(possibleValues), cellLoc='center')
    freqTable.auto_set_font_size(False)
    freqTable.set_fontsize(8)
    freqTable.scale(0.5, 1)
    plt.axis('off')
    plt.show()
    # Returns Frequency Dictionary
    return freq


def gatherSet(table, rowName):
    returnSet = set()
    for i in table[rowName]:
        returnSet.add(i)
    return returnSet