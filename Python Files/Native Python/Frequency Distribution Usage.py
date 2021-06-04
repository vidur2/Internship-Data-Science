'''
File that generates Frequency Distribution Table
'''

# Imports
import freqCommands

def main():
    # Reads in data from csv
    data, isSuccess = freqCommands.readCSV('/Users/vidurmodgil/Desktop/DATA/Internship/Internship-Data/VIDURSAMPLE.csv')
    print(list(data.keys()))
    # Generates set of unique data
    uniqueId = freqCommands.gatherSet(data, 'AGE')
    # Gets frequency and plots table
    frequencyDict = freqCommands.frequencyDist(data, 'AGE', uniqueId)

if __name__ == '__main__':
    main()
