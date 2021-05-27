'''
Internship Day 1
Age Variable
'''

#Imports
import csv
import pandas
import os
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
def main():
    data, isSuccess = readCSV('/Users/vidurmodgil/Desktop/DATA/Internship/Internship-Data/VIDURSAMPLE.csv')
    pandas.DataFrame.from_dict(data)
    delqid = data['DELQID']
    freq = []
    for i in range(8):
        counter = 0
        for element in delqid:
            if i == int(element):
                counter = counter + 1
        freq.append(counter)
    print(freq)
if __name__ == '__main__':
    main()