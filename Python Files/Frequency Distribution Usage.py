'''
File that generates Frequency Distribution Table
'''

# Imports
import Commands

def main():
    # Reads in data from csv
    data, isSuccess = Commands.readCSV('/Users/vidurmodgil/Desktop/DATA/Internship/Internship-Data/VIDURSAMPLE.csv')

    # Generates set of unique data
    uniqueDelqid = Commands.gatherSet(data, 'DELQID')
    # Gets frequency and plots table
    frequencyDict = Commands.frequencyDist(data, 'DELQID', uniqueDelqid)

if __name__ == '__main__':
    main()
