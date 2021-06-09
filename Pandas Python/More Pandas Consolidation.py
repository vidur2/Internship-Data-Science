'''
This will be the start of the final Python File 
Vidur Modgil
Internship
'''

# Imports
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import random
from sklearn.linear_model import LogisticRegression

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
    #plt.show()

    data['AGE'].hist(bins=10)
    plt.title('Age')
    #plt.show()

    data['DELQID'].hist(bins=8)
    plt.title('Delqid')
    #plt.show()

    data['goodbad'].hist(bins=2)
    plt.title('goodbad')
    #plt.show()

    data['BRPCTSAT'].hist(bins=10)
    plt.title('Bank Revolving Payment Percent Satisfied')
    #plt.show()

    data['RBAL'].hist(bins=6)
    plt.title('Revolving Balance')
    #plt.show()

    data['CRELIM'].hist(bins=6)
    plt.title('Credit Limit')
    #plt.show()

    
    
    
    # Generation of and sorting of ordinal and ranked Variables
    
    
    # Ordinal Variables
    
    # Initializes Label values
    ordTradesLabels = [1, 2, 3, 4, 5]
    ordAgeLabels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    ordBrpctsatLabels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ordRbalLabels = [1, 2, 3, 4, 5, 6]
    
    # Initialize empty Lists
    ordTradesBin = [-0.1, 10, 20, 30, 40, 100]
    ordAgeBin = [0, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, int(data['AGE'].max())]
    ordBrpctsatBin = [-0.1, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, int(data['BRPCTSAT'].max())]
    ordRbalBin = [-0.1, 5000, 10_000, 15_000, 20_000, 40_000, int(data['RBAL'].max())]
    data['ORDTRADES'] = pd.cut(data['TRADES'], ordTradesBin, labels=ordTradesLabels, retbins=False, precision=0)
    data['ORDAGE'] = pd.cut(data['AGE'], ordAgeBin, labels=ordAgeLabels, retbins=False, precision=0)
    data['ORDBRPCTSAT'] = pd.cut(data['BRPCTSAT'], ordBrpctsatBin, labels=ordBrpctsatLabels, retbins=False, precision=0)
    data['ORDRBAL'] = pd.cut(data['RBAL'], ordRbalBin, labels= ordRbalLabels, retbins= False, precision=0)

    # Computer Generated Variable adding with pandas(Ranked Variables)
    labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    reLabel = [1, 2, 3, 4, 5, 6, 7, 8]
    _, brpctsatBins, _ = plt.hist(list(data['BRPCTSAT']), equalObs(list(data['BRPCTSAT']), 10), color='black')
    brpctsatBins = list(brpctsatBins)
    for i in range(2):
        brpctsatBins.remove(1)
    brpctsatBins[0] = -0.1
    
    _, rankedBrpctsatBins, _ = plt.hist(list(data['BRPCTSAT']), equalObs(list(data['BRPCTSAT']), 8), color='black')
    data['RANKEDTRADES'] = pd.qcut(data['TRADES'], q=10, retbins=False, labels=labels, precision=0)
    data['RANKEDAGE'] = pd.qcut(data['AGE'], q=10, retbins=False, labels=labels, precision=0)
    data['RANKEDBRPCTSAT'] = pd.cut(data['BRPCTSAT'], brpctsatBins, labels=reLabel, retbins=False, precision=0)
    data['RANKEDRBAL'] = pd.qcut(data['RBAL'], q=10, retbins=False, labels=labels, precision=0, duplicates='drop')
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

    # Splitting the file randomly
    random.seed(123456)
    randomNumbers = []
    for _ in range(100_000):
        randomNumber = random.random()
        randomNumbers.append(randomNumber)
    data['Shuffle Assignment'] = randomNumbers
    data.sort_values('Shuffle Assignment', ascending=True, inplace=True, ignore_index = True)
    modelData = data[0:80_000].copy()
    testData = data[80_001:99_999].copy()
    print(modelData['TRADES'].describe())
    print(testData['TRADES'].describe())
    print(modelData['AGE'].describe())
    print(testData['AGE'].describe())

if __name__ == '__main__':
    main()