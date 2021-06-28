'''
This is the Run File for the 'Data Scientist' Version of the code
Vidur Modgil
Internship
'''

# Here we are importing all of the required packages
import numpy as np
import pandas as pd
import os
from matplotlib import pyplot as plt
import random
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

def main():
    # The first thing the code does is get the path of the CSV and read it into a pandas dataframe.
    workingDir = os.getcwd()
    data = pd.read_csv(workingDir + '/VIDURSAMPLE.csv') # Enter your filepath for the data here

    # This part of the code plots all of the variables as histograms to show the distribution.
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
    

    # Here the four prediction variables(Trades, Age, BRPCTSAT, and RBAL) are binned according to user-defined bins    
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

    # This splits the dataframe 80/20(train/test) randomly to ensure that there is no bias on what data is used to generate the model.
    random.seed(123456)
    randomNumbers = []
    for _ in range(100_000):
        randomNumber = random.random()
        randomNumbers.append(randomNumber)
    data['Shuffle Assignment'] = randomNumbers
    data.sort_values('Shuffle Assignment', ascending=True, inplace=True, ignore_index = True)
    modelData = data[0:80_000].copy()
    testData = data[80_001:99_999].copy()

    # The binned(ordinal) variables are then used to generate a logistic regression model
    # Note that good bad is the dependent variable
    usableModelDataX = modelData[['ORDTRADES', 'ORDAGE', 'ORDRBAL', 'ORDBRPCTSAT']]
    usableModelDataY = modelData['goodbad'].copy()
    
    # Fitting of the data
    logisticRegOrd = LogisticRegression()
    logisticRegOrd.fit(usableModelDataX, usableModelDataY)
    
    # Prediction of p(default)
    ordPrecitionProbability = list(logisticRegOrd.predict_proba(usableModelDataX))
    ordModelCoeff = list(logisticRegOrd.coef_)
    ordModelInt = list(logisticRegOrd.intercept_)
    ordModel = list(ordModelCoeff[0])
    
    ordModel.append(ordModelInt)
    
    # Output of Model Scoring using AUC(Expected value is 0.71)
    modelData['Prediction Prob_ORD'] = ordPrecitionProbability
    metrics.plot_roc_curve(logisticRegOrd, usableModelDataX, usableModelDataY)
    plt.show()
    
    # Output of the coefficients and intercept of Logistic Regression Model(~0.77361(Intercept), ~ -0.177008(ORDTRADES), ~ -0.061682(ORDAGE), ~ 0.175941(ORBRPCTSAT), ~ -0.292972(ORDRBAL))
    predictionModels = pd.DataFrame(data=[ordModel], index=['Ordinal'], columns=['ORDTrades', 'ORDAge', 'ORDBRPCTSAT', 'ORDRBAL', 'Intercept'])
    print('\n')
    print(predictionModels)
    print('\n')

    # Testing the model on the 20,000 datapoints not used to generate the model
    testDataInd = testData[['ORDAGE', 'ORDTRADES', 'ORDRBAL', 'ORDBRPCTSAT']]
    predictionVariable = list(logisticRegOrd.predict_proba(testDataInd))
    predictionVariableSingular = []
    for element in predictionVariable:
        predictionVariableSingular.append(element[1])
    testData['Prediction Variable'] = predictionVariableSingular
    print(testData)

    
    '''
    5 Cutoff points are tested(see cutoffPoints tuple) to see which maximizes profit according to the profit function:
    Profit = 500(# of Predicted non defaulters who did not default) - (0.5 * Credit Limit)(# of Predicted non defaulters who did default)
    Profit Per Customer = Profit/Total number of Data Points
    The Predicted Cuttoff point is 0.3, and the Expected Profit Per customer should be ~$276.54
    '''
    cutoffPoints = (0.2, 0.25, 0.3, 0.35, 0.4)
    predictionVariable = list(testData['Prediction Variable'])
    possibleProfits = []
    for point in cutoffPoints:
        profits = 0
        testDataPredictedGoodBad = []
        for element in predictionVariable:
            if element < point:
                testDataPredictedGoodBad.append(0)
            else:
                testDataPredictedGoodBad.append(1)
        title = 'Prediction Variable cutoff point ' + str(point)
        testData[title] = testDataPredictedGoodBad
        groupedTest = testData.groupby(title)
        intendedGroup = groupedTest.get_group(0)
        for index, row in intendedGroup.iterrows():
            if row['goodbad'] == 0:
                profits = profits + 500
            else:
                profits = profits - (0.5 * row['CRELIM'])
        possibleProfits.append(profits/len(predictionVariable))
        
    maxProfits = max(possibleProfits)
    maxProfitsIndex = possibleProfits.index(maxProfits)
    print(f'The optimal cutoff point is {cutoffPoints[maxProfitsIndex]}, with a profit per account value of {maxProfits}')
    plt.plot(cutoffPoints, possibleProfits)
    plt.title('Cuttoff Point Optimization')
    plt.show()

if __name__ == '__main__':
    main()