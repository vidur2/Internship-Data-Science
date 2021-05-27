'''
Internship Day 1
Age Variable
'''

#Imports
import pandas
from Commands import * 

def main():
    data, isSuccess = readCSV('/Users/vidurmodgil/Desktop/DATA/Internship/Internship-Data/VIDURSAMPLE.csv')
    pandas.DataFrame.from_dict(data)
    delqid = data['goodbad']
    freq = []
    possibleData = gatherSet(data, 'DELQID')
    print(possibleData)
    getFreq = frequencyDist(data, 'DELQID', possibleData)
    print(getFreq)

if __name__ == '__main__':
    main()