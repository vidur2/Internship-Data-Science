'''
Commands to make programming easier
'''
#Imports
import csv
import pandas
import os
import Commands

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
                storedInformation[headers[iterator]].append(elements)
                iterator = iterator + 1
        return storedInformation, True
    else:
        # If the wrong filepath is entered, returns Nonetype and False to user
        return None, False

def frequencyDist(table, rowName, possibleValues):
    freq = dict()
    for i in possibleValues:
        counter = 0
        newInformation = []
        for element in table[rowName]:
            if float(i) == float(element):
                counter = counter + 1
        newInformation.append(counter)
        freq[i] = newInformation
    return freq


def gatherSet(table, rowName):
    returnSet = set()
    for i in table[rowName]:
        returnSet.add(i)
    return returnSet