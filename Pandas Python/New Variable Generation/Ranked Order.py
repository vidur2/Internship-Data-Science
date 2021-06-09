import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def equalObs(x, nbin):
    nlen = len(x)
    return np.interp(np.linspace(0, nlen, nbin + 1),
                     np.arange(nlen),
                     np.sort(x))

data = pd.read_csv('/Users/vidurmodgil/Desktop/DATA/Internship/Internship-Data/VIDURSAMPLE.csv')
tradesDF = list(data['TRADES'].copy())
tradesDataFrame = pd.DataFrame(data['TRADES'].copy())
tradeList = data['TRADES'].tolist()
ageList = data['AGE'].tolist()
rbalList = data['RBAL'].tolist()
brpctsatList = data['BRPCTSAT'].tolist()

n, tradeBins, patches = plt.hist(tradeList, equalObs(tradeList, 10), edgecolor='black')
_, ageBins, _ = plt.hist(ageList, equalObs(ageList, 10), color='black')
_, rbalBins,  _ = plt.hist(rbalList, equalObs(rbalList, 10), color='black')
_, brpctsatBins, _ = plt.hist(brpctsatList, equalObs(brpctsatList, 10), color='black')

ordTrades = []
rankedAge = []
rankedRbal = []
rankedBrpctsat = []

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

for i in ageList:
    if i < ageBins[1]:
        rankedAge.append(1)
    elif i < ageBins[2]:
        rankedAge.append(2)
    elif i < ageBins[3]:
        rankedAge.append(3)
    elif i < ageBins[4]:
        rankedAge.append(4)
    elif i < ageBins[5]:
        rankedAge.append(5)
    elif i < ageBins[6]:
        rankedAge.append(6)
    elif i < ageBins[7]:
        rankedAge.append(7)
    elif i < ageBins[8]:
        rankedAge.append(8)
    elif i < ageBins[9]:
        rankedAge.append(9)
    else:
        rankedAge.append(10)
    
for i in tradesDF:
    if i < tradeBins[1]:
        x = 1
        ordTrades.append(x)
    elif i < tradeBins[2]:
        x = 2
        ordTrades.append(x)
    elif i < tradeBins[3]:
        x = 3
        ordTrades.append(x)
    elif i < tradeBins[4]:
        x = 4
        ordTrades.append(x)
    elif i < tradeBins[5]:
        x = 5
        ordTrades.append(x)
    elif i < tradeBins[6]:
        x = 6
        ordTrades.append(x)
    elif i < tradeBins[7]:
        x = 7
        ordTrades.append(x)
    elif i < tradeBins[8]:
        x = 8
        ordTrades.append(x)
    elif i < tradeBins[9]:
        x = 9
        ordTrades.append(x)
    else:
        x = 10
        ordTrades.append(x)

print(len(rankedBrpctsat))
print(len(brpctsatList))
data['RANKTRADE'] = ordTrades
data['RANKEDAGE'] = rankedAge
data['RANKEDRBAL'] = rankedRbal
data['RANKEDBRPCTSAT'] = rankedBrpctsat

rankTradeDescriptiveStats = data[["RANKTRADE", "goodbad"]].groupby("RANKTRADE").describe()
RankRbalStats = data[["RANKEDRBAL", "goodbad"]].groupby("RANKEDRBAL").describe()
rankedBrpctsatStats = data[["RANKEDBRPCTSAT", "goodbad"]].groupby("RANKEDBRPCTSAT").describe()

rankedBrpctsatStats = pd.DataFrame(data[["RANKEDBRPCTSAT", "goodbad"]].groupby("RANKEDBRPCTSAT").mean())
rankedBrpctsatStats['RANKEDBRPCTSAT_1'] = rankedBrpctsatStats.index
print(rankedBrpctsatStats)
rankedBrpctsatStats.plot.scatter(x='Prediction_1', y="goodbad")
plt.show()
print(rankedBrpctsatStats)