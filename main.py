# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import netCDF4
import csv
import sys
from sklearn import linear_model

precip_nc_file = 'C:\Users\zhuo\PycharmProjects\untitled\pnwrain.50km.daily.4994.nc'
nc = netCDF4.Dataset(precip_nc_file, mode='r')

def ncdump(nc_fid, verb=True):
    def print_ncattr(key):
        try:
            print "\t\ttype:", repr(nc_fid.variables[key].dtype)
            for ncattr in nc_fid.variables[key].ncattrs():
                print '\t\t%s:' % ncattr,\
                      repr(nc_fid.variables[key].getncattr(ncattr))
        except KeyError:
            print "\t\tWARNING: %s does not contain variable attributes" % key

    # NetCDF global attributes
    nc_attrs = nc_fid.ncattrs()
    if verb:
        print "NetCDF Global Attributes:"
        for nc_attr in nc_attrs:
            print '\t%s:' % nc_attr, repr(nc_fid.getncattr(nc_attr))
    nc_dims = [dim for dim in nc_fid.dimensions]  # list of nc dimensions
    # Dimension shape information.
    if verb:
        print "NetCDF dimension information:"
        for dim in nc_dims:
            print "\tName:", dim 
            print "\t\tsize:", len(nc_fid.dimensions[dim])
            print_ncattr(dim)
    # Variable information.
    nc_vars = [var for var in nc_fid.variables]  # list of nc variables
    if verb:
        print "NetCDF variable information:"
        for var in nc_vars:
            if var not in nc_dims:
                print '\tName:', var
                print "\t\tdimensions:", nc_fid.variables[var].dimensions
                print "\t\tsize:", nc_fid.variables[var].size
                print_ncattr(var)
    return nc_attrs, nc_dims, nc_vars


nc_attrs, nc_dims, nc_vars = ncdump(nc)

lats = nc.variables['lat'][:]  # extract/copy the data
lons = nc.variables['lon'][:]
time = nc.variables['time'][:]
data = nc.variables['data'][:]  # shape is time, lat, lon as shown above
 
print('begin')
listX = list()

for i in range(0,16801):
    for j in range(0,17):
        for k in range(0,16):
            listTemp =list()    
            listTemp.append(time[i])
            listTemp.append(lats[j])
            listTemp.append(lons[k])
            listTemp.append(data[i][j][k])
            listX.append(listTemp)
            
#print(len(listX))
#print(listX[0][0])

#print('preend')

with open("modifiedData.csv",'wb') as resultFile:
    wr = csv.writer(resultFile,dialect='excel')
    wr.writerows(listX)
print('end')
#clf = linear_model.LogisticRegression()
#clf.fit(trainingSet, trainingClasses)
#
