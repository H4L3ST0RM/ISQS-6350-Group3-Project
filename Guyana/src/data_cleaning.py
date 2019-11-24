# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:59:38 2019

@author: johnc
"""



import pandas as pd



census = pd.read_csv('../data/Census Guyana 2012 v2.csv')
census_perc = pd.read_csv('../data/Census Guyana 2012 v2.csv')

#Dropping Race Data
census = census.drop(columns=['Black','Amerindian','East Indian', 'Chinese', 'Mixed', 'Portugese', 'White', 'Other Ethnicity'])

# Dropping Religion Data
census = census.drop(columns=['Anglican','Methodist', 'Pentecostal', 'Catholic', 'Witness', 'Adventist', 'Bahai', 'Muslim',
                             
                             'Hindu', 'Rastafarian', 'Christians','No Religion', 'Other Religion'])
# Dropping Age Brackets
census = census.drop(columns=['0 to 4','5 to 9','10 to 14','15 to 19','20 to 24','25 to 29','30 to 34','35 to 39',
                     '40 to 44','45 to 49','50 to 54','55 to 59','60 to 64','65 to 69','70 to 74','75 to 79',
                     '80 to 84','85 +'])
# Dropping Village Data
census = census.drop(columns=['Village No', 'Village Name'])

census['Population'] = census['Male'] + census['Female']

# Dropping columns with large amounds correlation above or below 0.15, 0.9
census = census.drop(columns=['Female','Male'])

corr = census.corr()
corr.mask((abs(corr) < 0.15) | (abs(corr) > 0.9))


census.dropna(inplace=True)

census.to_csv('../data/cleaned_census_data2.csv',index=False)

census_region = census
#census_region.to_csv('../data/census_grouped_region.csv', index = True)

census_percent = census
for i in range(0,len(census)):
    census_percent.iloc[i,1:21] =  census.iloc[i,1:21] /  sum(census.iloc[i,1:21])
census_percent.dropna(inplace=True)
census_percent.to_csv('../data/cleaned_census_perc_data2.csv',index=False)

