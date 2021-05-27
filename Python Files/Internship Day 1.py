'''
Internship Day 1
Age Variable
'''

#Imports
import pandas
from Commands import * 
from DescriptiveAnalysisCommands import *

def main():
    data, isSuccess = readCSV('/Users/vidurmodgil/Desktop/DATA/Internship/Internship-Data/VIDURSAMPLE.csv')
    pandas.DataFrame.from_dict(data)
    delqid = data['goodbad']
    freq = []
    possibleData = gatherSet(data, 'DELQID')
    getFreq = frequencyDist(data, 'DELQID', possibleData)
    df = pandas.DataFrame.from_dict(getFreq)
    median = getMedian(data, 'AGE')
    print(median)
if __name__ == '__main__':
    main()