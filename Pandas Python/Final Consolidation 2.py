'''
Client Productionalized Code
Vidur Modgil
Internship
'''
import pandas as pd
import math

def main():
    # This is the model function which takes input and predicts(think f(x) = mx + b, where x is the input variable)
    logisticModel = lambda trades, age, brpctsat, rbal: (math.exp(0.7736147308484715 - (0.177008 * trades) - (0.061682 * age) + (0.175941 * brpctsat) - (0.292972 * rbal)))/(1 + math.exp(0.7736147308484715 - (0.177008 * trades) - (0.061682 * age) + (0.175941 * brpctsat) - (0.292972 * rbal)))

    # Gets the filepath as input
    csvPath = input('Enter the location of your input file here(supported file is .csv): ')
    data = pd.read_csv(csvPath)

    # This part of the code sorts the data by their numeric input(sorts by range value)
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

    # Goes through your inputted file and inputs data into model
    predictions = []
    ordTrades = list(data['ORDTRADES'].copy())
    ordAge = list(data['ORDAGE'].copy())
    ordBrpctsat = list(data['ORDBRPCTSAT'].copy())
    ordRbal = list(data['ORDRBAL'].copy())
    
    counter = 0

    for ordTrade in ordTrades:
        ordage = ordAge[counter]
        ordbrpctsat = ordBrpctsat[counter]
        ordrbal = ordRbal[counter]
        prediction = logisticModel(ordTrade, ordage, ordbrpctsat, ordrbal)
        if prediction <= 0.3:
            predictions.append(0)
        else:
            predictions.append(1)
        counter = counter + 1
    
    # This part of the code stores the prediction in a csv
    data['Prediction Outcome'] = predictions
    groupedData = data.groupby('Prediction Outcome')
    outputStore = input('Where would you like to store your output(Enter filepath)? ')
    data.set_index('MATCHKEY')
    data.to_csv(outputStore)
    

if __name__ == '__main__':
    main()