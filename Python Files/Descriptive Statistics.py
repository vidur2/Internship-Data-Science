'''
Descriptive Statistics
Vidur Modgil
Internship
'''

#Imports
from Commands import * 
from DescriptiveAnalysisCommands import *
from matplotlib import pyplot as plt

def main():
    # Headers of columns
    data, isSuccessful = readCSV('/Users/vidurmodgil/Desktop/DATA/Internship/Internship-Data/VIDURSAMPLE.csv')
    keys = list(data.keys())
    descriptiveDataGraphing(keys)
if __name__ == '__main__':
    main()
