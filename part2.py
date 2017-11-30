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
from sklearn.cluster import KMeans


print('start')

data = np.genfromtxt('modifiedData.csv', delimiter= ",")


imp = Imputer(missing_values='NaN', strategy='mean', axis=0)

imp.fit(data)

for i in data:
    if math.isnan(i[3]):
        i[3] = 0.0


positions = []
for i in range(0, 60000):    
    num = data[i][3]  
    if num != 0:
        for j in range(0, int(num)):    
            tempPos = [data[i][1], data[i][2]] 
            positions.append(tempPos)      
finalPos = np.array(positions)          
kmeans = KMeans(n_clusters = 21, random_state = 0).fit(finalPos)  
print('centers: ') 
print(kmeans.cluster_centers_)         
print("predict")
print("1st:")
print(kmeans.predict([[47.38, -120.625]]))
print("2nd: ")
print(kmeans.predict([[48.8086, -122.5]]))
print("3rd: ")
print(kmeans.predict([[43.5706, -121.875]]))
print("4th: ")
print(kmeans.predict([[42.6182, -123.125]]))
print("5th: ")
print(kmeans.predict([[45.4753, -118.125]]))



