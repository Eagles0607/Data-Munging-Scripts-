# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 13:07:30 2016

@author: charleswiles
"""

import pandas as pd

#Loads the data#

rawData = pd.read_csv('properties.csv',low_memory=False)
offProp = pd.read_excel('new_offprop.xlsx',sheetname="prop2015")

#Fills blanks#

blanksFilled = rawData.fillna('blank')
offPropblanks = offProp.fillna('blank')

#Filter conditions#

extconds = [0,5,6,7]
intconds = [0,5,6,7]
catcds = [1,2,3,6]
zone = ['RSA1', 'RSA2', 'RSA3','RSA4', 'RSA5', 'RTA1', 'RM1', 'RM2', 'RMX1', 'CMX1', 'CMX2', 'CMX2.5', 'IRMX']

#Filtered dataframes#

prepdataonprop = blanksFilled[
    blanksFilled['Exterior Condition'].isin(extconds) & 
    blanksFilled['Interior Condition'].isin(intconds) & 
    blanksFilled['Zoning'].isin(zone) &
    blanksFilled['Category Code'].isin(catcds)
    ] 
    
    

prepdataoffprop = offPropblanks[
    offPropblanks['EXT COND'].isin(extconds) & 
    offPropblanks['INT COND'].isin(intconds) & 
    offPropblanks['ZONE'].isin(zone) &
    offPropblanks['CAT CD'].isin(catcds)
    ] 


prepdataonprop.to_csv('preppedonprop.csv') 

prepdataoffprop.to_csv('preppedoffprop.csv')
