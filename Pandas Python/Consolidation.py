'''
This will be the start of the final Python File 
Vidur Modgil
Internship
'''

# Imports
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def equalObs(x, nbin):
    nlen = len(x)
    return np.interp(np.linspace(0, nlen, nbin + 1),
                     np.arange(nlen),
                     np.sort(x))

def main():
    # Reads in the csv
    data = pd.read_csv('/Users/vidurmodgil/Desktop/DATA/Internship/Internship-Data/VIDURSAMPLE.csv') # Enter your filepath for the data here
    
    # Generate and output file layout using pandas
    fileLayout = data.info()
    print(fileLayout)

    # Run Descriptive Statistics on the entire data set and output
    descriptiveStatistics = data.describe()
    print(descriptiveStatistics)

    
    # Histograms of all variables
    data['TRADES'].hist(bins=12)
    plt.title('Trades')
    plt.show()

    data['AGE'].hist(bins=10)
    plt.title('Age')
    plt.show()

    data['DELQID'].hist(bins=8)
    plt.title('Delqid')
    plt.show()

    data['goodbad'].hist(bins=2)
    plt.title('goodbad')
    plt.show()

    data['BRPCTSAT'].hist(bins=10)
    plt.title('Bank Revolving Payment Percent Satisfied')
    plt.show()

    data['RBAL'].hist(bins=6)
    plt.title('Revolving Balance')
    plt.show()

    data['CRELIM'].hist(bins=6)
    plt.title('Credit Limit')
    plt.show()

    
    
    
    # Generation of and sorting of ordinal and ranked Variables

    # Separation of dataframe columns into lists
    tradesList = list(data['TRADES'].copy())
    ageList = list(data['AGE'].copy())
    brpctsatList = list(data['BRPCTSAT'].copy())
    rbalList = list(data['RBAL'].copy())

    
    # Ordinal Variable Generation

    # Initialize empty Lists
    ordTrades = []
    ordAge = []
    ordBrpctsat = []
    ordRbal = []

    # Iterate through each of the trades and sort them based on preset bins 
    for i in tradesList:
        if i < 10:
            ordTrades.append(1)
        elif i < 20:
            ordTrades.append(2)
        elif i < 30:
            ordTrades.append(3)
        elif i < 40:
            ordTrades.append(4)
        else:
            ordTrades.append(5)

    for i in ageList:
        if i < 25:
            ordAge.append(1)
        elif i < 30:
            ordAge.append(2)
        elif i < 35:
            ordAge.append(3)
        elif i < 40:
            ordAge.append(4)
        elif i < 45:
            ordAge.append(5)
        elif i < 50:
            ordAge.append(6)
        elif i < 55:
            ordAge.append(7)
        elif i < 60:
            ordAge.append(8)
        elif i < 65:
            ordAge.append(9)
        elif i < 70:
            ordAge.append(10)
        else:
            ordAge.append(11)
    
    for i in brpctsatList:
        if i < 0.1:
            ordBrpctsat.append(1)
        elif i < 0.2:
            ordBrpctsat.append(2)
        elif i < 0.3:
            ordBrpctsat.append(3)
        elif i < 0.4:
            ordBrpctsat.append(4)
        elif i < 0.5:
            ordBrpctsat.append(5)
        elif i < 0.6:
            ordBrpctsat.append(6)
        elif i < 0.7:
            ordBrpctsat.append(7)
        elif i < 0.8:
            ordBrpctsat.append(8)
        elif i < 0.9:
            ordBrpctsat.append(9)
        else:
            ordBrpctsat.append(10)

    for i in rbalList:
        if i < 5000:
            ordRbal.append(1)
        elif i < 10000:
            ordRbal.append(2)
        elif i < 15000:
            ordRbal.append(3)
        elif i < 20000:
            ordRbal.append(4)
        elif i < 40000:
            ordRbal.append(5)
        else:
            ordRbal.append(6)
    
    # Appends the lists as columns to the Pandas Dataframe
    data['ORDTRADES'] = ordTrades
    data['ORDAGE'] = ordAge
    data['ORDBRPCTSAT'] = ordBrpctsat
    data['ORDRBAL'] = ordRbal


    # Ranked variable generation

    # Initialize empty lists for data collection
    rankedTrades = []
    rankedAge = []
    rankedBrpctsat = []
    rankedRbal = []

    # Generate bins for each category
    _, tradeBins, _ = plt.hist(tradesList, equalObs(tradesList, 10), edgecolor='black')
    _, ageBins, _ = plt.hist(ageList, equalObs(ageList, 10), color='black')
    _, rbalBins,  _ = plt.hist(rbalList, equalObs(rbalList, 10), color='black')
    _, brpctsatBins, _ = plt.hist(brpctsatList, equalObs(brpctsatList, 10), color='black')

    # Sort each element in trades list by bin ranges
    for i in tradesList:
        hasAppended = False
        for j in range(10):
            if i < tradeBins[j + 1]:
                rankedTrades.append(j + 1)
                hasAppended = True
                break
        if hasAppended == False:
            rankedTrades.append(10)
    
    for i in ageList:
        hasAppended = False
        for j in range(10):
            if i < ageBins[j + 1]:
                rankedAge.append(j + 1)
                hasAppended = True
                break
        if hasAppended == False:
            rankedAge.append(10)
    
    for i in brpctsatList:
        hasAppended = False
        for j in range(10):
            if i < brpctsatBins[j + 1]:
                rankedBrpctsat.append(j + 1)
                hasAppended = True
                break
        if hasAppended == False:
            rankedBrpctsat.append(10)
    
    for i in rbalList:
        hasAppended = False
        for j in range(10):
            if i < rbalBins[j + 1]:
                rankedRbal.append(j + 1)
                hasAppended = True
                break
        if hasAppended == False:
            rankedRbal.append(10)
    
    # Appends sorted variables to pandas dataframe
    data['RANKEDTRADES'] = rankedTrades
    data['RANKEDAGE'] = rankedAge
    data['RANKEDBRPCTSAT'] = rankedBrpctsat
    data['RANKEDRBAL'] = rankedRbal
    print(data)

    
    # Runs descriptive statistics with the new variables vs their original counterparts

    # Ordinal Variables
    ordTradesDescriptiveStatistics = data[["ORDTRADES", "TRADES"]].groupby("ORDTRADES").describe()
    ordAgeDescriptiveStatistics = data[["ORDAGE", "AGE"]].groupby("ORDAGE").describe()
    ordBrpctsatDescriptiveStatistics = data[["ORDBRPCTSAT", "BRPCTSAT"]].groupby("ORDBRPCTSAT").describe()
    ordRbalDescriptiveStatistics = data[["ORDRBAL", "RBAL"]].groupby("ORDRBAL").describe()

    print('\n\nOrdinal Variables vs Original Counterparts: \n')
    print(ordTradesDescriptiveStatistics)
    print(ordAgeDescriptiveStatistics)
    print(ordBrpctsatDescriptiveStatistics)
    print(ordRbalDescriptiveStatistics)

    # Computer-Ranked Variables
    rankedTradesDescriptiveStatistics = data[["RANKEDTRADES", "TRADES"]].groupby("RANKEDTRADES").describe()
    rankedAgeDescriptiveStatistics = data[["RANKEDAGE", "AGE"]].groupby("RANKEDAGE").describe()
    rankedBrpctsatDescriptiveStatistics = data[["RANKEDBRPCTSAT", "BRPCTSAT"]].groupby("RANKEDBRPCTSAT").describe()
    rankedRbalDescriptiveStatistics = data[["RANKEDRBAL", "RBAL"]].groupby("RANKEDRBAL").describe()
    
    print('\n\nRanked Variables vs Original Counterparts: \n')
    print(rankedTradesDescriptiveStatistics)
    print(rankedAgeDescriptiveStatistics)
    print(rankedBrpctsatDescriptiveStatistics)
    print(rankedRbalDescriptiveStatistics)

    
    # Runs Descriptive Statistics on the new variables vs goodbad to see p(default)

    # Ordinal variables
    ordTradesDescriptiveStatistics = data[["ORDTRADES", "goodbad"]].groupby("ORDTRADES").describe()
    ordAgeDescriptiveStatistics = data[["ORDAGE", "goodbad"]].groupby("ORDAGE").describe()
    ordBrpctsatDescriptiveStatistics = data[["ORDBRPCTSAT", "goodbad"]].groupby("ORDBRPCTSAT").describe()
    ordRbalDescriptiveStatistics = data[["ORDRBAL", "goodbad"]].groupby("ORDRBAL").describe()

    print('\n\nOrdinal Variables vs goodbad: \n')
    print(ordTradesDescriptiveStatistics)
    print(ordAgeDescriptiveStatistics)
    print(ordBrpctsatDescriptiveStatistics)
    print(ordRbalDescriptiveStatistics)

    # Computer-Ranked Variables
    rankedTradesDescriptiveStatistics = data[["RANKEDTRADES", "goodbad"]].groupby("RANKEDTRADES").describe()
    rankedAgeDescriptiveStatistics = data[["RANKEDAGE", "goodbad"]].groupby("RANKEDAGE").describe()
    rankedBrpctsatDescriptiveStatistics = data[["RANKEDBRPCTSAT", "goodbad"]].groupby("RANKEDBRPCTSAT").describe()
    rankedRbalDescriptiveStatistics = data[["RANKEDRBAL", "goodbad"]].groupby("RANKEDRBAL").describe()
    
    print('\n\nRanked Variables vs goodbad: \n')
    print(rankedTradesDescriptiveStatistics)
    print(rankedAgeDescriptiveStatistics)
    print(rankedBrpctsatDescriptiveStatistics)
    print(rankedRbalDescriptiveStatistics)


    
if __name__ == '__main__':
    main()