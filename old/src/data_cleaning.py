# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:59:38 2019

@author: johnc
"""



import pandas as pd



census = pd.read_csv('C:/Users/johnc/Desktop/ISQS-6350-Group3-Project/data/Census Guyana 2012 v2.csv')

#Dropping Race Data
census = census.drop(columns=['Black','Amerindian','East Indian', 'Chinese', 'Mixed', 'Portugese', 'White', 'Other Ethnicity'])

# Dropping Religion Data
census = census.drop(columns=['Anglican','Methodist', 'Pentecostal', 'Catholic', 'Witness', 'Adventist', 'Bahai', 'Muslim',
                             
                             'Hindu', 'Rastafarian', 'Christians','No Religion', 'Other Religion'])

# Dropping Village Data
census = census.drop(columns=['Village No', 'Village Name'])

census['Population'] = census['Male'] + census['Female']


# Making Larger Age Brackets
census['0-19'] = census['0 to 4'] + census['5 to 9'] + census['10 to 14'] + census['15 to 19']
census['20-39']= census['20 to 24'] + census['25 to 29'] + census['30 to 34'] + census['35 to 39']
census['40-59']= census['40 to 44'] + census['45 to 49'] + census['50 to 54'] + census['55 to 59']
census['60+']= census['60 to 64'] + census['65 to 69'] + census['70 to 74'] + census['75 to 79']+ census['80 to 84'] + census['85 +']

# Dropping Smaller Age Brackets
census = census.drop(columns=['0 to 4','5 to 9','10 to 14','15 to 19','20 to 24','25 to 29','30 to 34','35 to 39',
                     '40 to 44','45 to 49','50 to 54','55 to 59','60 to 64','65 to 69','70 to 74','75 to 79',
                     '80 to 84','85 +'])



corr = census.corr()
corr.mask((abs(corr) < 0.15) | (abs(corr) > 0.9))
census['Population'] = census['Male'] + census['Female']

# Dropping columns with large amounds correlation above or below 0.15, 0.9
census = census.drop(columns=['Female','Male'])
census = census.drop(columns=['0-19','20-39','40-59','60+'])
corr = census.corr()
corr.mask((abs(corr) < 0.15) | (abs(corr) > 0.9))

census.to_csv('../data/cleaned_census_data.csv',index=False)

census_region = census.groupby(['Region']).sum()
census_region.to_csv('../data/census_grouped_region.csv', index = True)




