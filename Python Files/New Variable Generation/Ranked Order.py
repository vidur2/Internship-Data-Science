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
n, tradeBins, patches = plt.hist(tradeList, equalObs(tradeList, 10), edgecolor='black')
ordTrades = []
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
        print(x)
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
data['RANKTRADE'] = ordTrades
tradeSort = pd.DataFrame(data[['RANKTRADE', 'TRADES']].copy())
tradeSort.sort_values(['RANKTRADE'], ascending=True, inplace=True)
print(tradeSort)