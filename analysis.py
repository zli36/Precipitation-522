# -*- coding: utf-8 -*-

#analysis
import netCDF4
import csv
import sys
import numpy as np
import math
from sklearn import linear_model
from sklearn.neural_network import MLPRegressor
from sklearn import cross_validation as cv
from sklearn.decomposition import PCA
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.preprocessing import Imputer
 
def calculateErrorRates(clf, testset, testresult):
  errorRates = 0;
  totalPoints = 0;
  for data, realresult in zip(testset,testresult):
    prediction = clf.predict([data])
    errorRates += math.sqrt((realresult-prediction)*(realresult-prediction))
    totalPoints += 1;
  errorRates = errorRates / totalPoints;
  print(errorRates)
  return(errorRates) 

print('start')

data = np.genfromtxt('modifiedData.csv', delimiter= ",")


imp = Imputer(missing_values='NaN', strategy='mean', axis=0)

imp.fit(data)

for i in data:
    if math.isnan(i[3]):
        i[3] = 0.0


#data = preprocessing.scale(data)

pca = PCA(n_components=3)
data = pca.fit_transform(data)

xValue = data[0:, 0 : len(data[0])-1]
yValue = data[0:, len(data[0])-1]

trainingX, testX, trainingY, testY= train_test_split(xValue, yValue, test_size=.20, random_state=42)

#clf = svm.SVR(kernel='linear')
#clf.fit(trainingX, trainingY)


print('success split')

#dataset
#dataresult
reg = linear_model.LinearRegression()
reg.fit(trainingX,trainingY)
print('LR Error rates:')
regError = calculateErrorRates(reg, testX, testY)

# ANN
ann = MLPRegressor(hidden_layer_sizes = (3),alpha = 1e-10)
ann.fit(trainingX,trainingY)
print('ANN Error rates for layer 3:')
annError3 = calculateErrorRates(ann, testX, testY)

ann.set_params(hidden_layer_sizes=(2))
ann.fit(trainingX,trainingY)
print('ANN Error rates for layer 2:')
annError2 = calculateErrorRates(ann, testX, testY)

ann.set_params(hidden_layer_sizes=(1))
ann.fit(trainingX,trainingY)
print('ANN Error rates for layer 1:')
annError1 = calculateErrorRates(ann, testX, testY)

#Ridge    
ridge = linear_model.Ridge (alpha = .5)
ridge.fit(trainingX,trainingY)
print('Ridge Error rates:')
ridgeError = calculateErrorRates(ridge, testX, testY)

#Lasso
lasso = linear_model.Lasso(alpha = 0.1)
lasso.fit(trainingX,trainingY)
print('Lasso Error rates:')
lassoError = calculateErrorRates(lasso, testX, testY)


#gause = GaussianProcessRegressor(alpha=1e-10)
#gause.fit(trainingX, trainingY)
#print('Gause Error rates:')
#gauseError = calculateErrorRates(gause, testX, testY)
