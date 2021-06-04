'''
Create user-defined bins and sort through the data that way
Vidur Modgil
Internship
'''

# Imports
import pandas as pd
from matplotlib import pyplot as plt
def main():
    data = pd.read_csv('/Users/vidurmodgil/Desktop/DATA/Internship/Internship-Data/VIDURSAMPLE.csv')
    
    Brpctsat = list(data['BRPCTSAT'].copy())
    rbal = list(data['RBAL'].copy())
    trades = list(data['TRADES'].copy())
    age = list(data['AGE'].copy()) 
    
    ordBrpctsat = []
    ordRbal = []
    ordTrades = []
    ordAge = []

    for i in Brpctsat:
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
    
    for i in rbal:
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
    
    for i in trades:
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

    for i in age:
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

    data['ORDBRPCTSAT'] = ordBrpctsat
    data['ORDRBAL'] = ordRbal
    data['ORDTRADES'] = ordTrades
    data['ORDAGE'] = ordAge
    ageDescriptiveStats = data[["ORDBRPCTSAT", "goodbad"]].groupby("ORDBRPCTSAT").describe()
    print(ageDescriptiveStats)
if __name__ == '__main__':
    main()