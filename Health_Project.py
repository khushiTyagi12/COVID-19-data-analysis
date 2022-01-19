# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 20:33:15 2022

@author: khushi
"""

import pandas as pd
import  numpy as np
covid_word=pd.read_csv('C:/Users/user/Desktop/7th semester/ML Lab/owid-covid-data.csv')
print(covid_word)
covid_word.info()
fields=['iso_code','continent','location','tests_units']
print(covid_word[fields])
covid_word['date']
fields=['iso_code','continent','location','tests_units']
covid_word[fields]=covid_word[fields].astype('category')
covid_word.loc[:,'date']=pd.to_datetime(covid_word['date'])
covid_word[fields].describe()
covid_word['tests_units'].cat.categories
covid_word['tests_units'].value_counts().to_frame()

covid_word.groupby('tests_units')['total_cases'].sum().sort_values(ascending=False).to_frame()
pd.options.display.float_format='{:,.0f}'.format
covid_word.groupby('tests_units')['total_cases'].sum().sort_values(ascending=False).to_frame()
