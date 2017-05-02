#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 10:48:11 2017

@author: abk
"""

import pandas as pd
import numpy as np
import time
import datetime
import matplotlib.pyplot as plt

#%% library
def principle_component(li):
    for item in li:
        if item == '':
            item = 'NaN'
    
    dic = {}
    for item in li:
        if item in dic:
            dic[item] = dic[item] + 1
        else:
            dic[item] = 1
               
    keys = []
    values = []
    
    for key, value in dic.items():
        keys.append(key)
        values.append(value)
    
    
    keys = np.array(keys)
    values = np.array(values)
    
    index = np.argsort(-values)
    keys = keys[index]
    values = values[index]
    
    total = sum(values)
    count = 0
    for i in range(np.size(keys)):
        count = count + values[i]
        print(keys[i],'portion:',values[i]/total,'cumulate:',count/total)
               
    return keys, values
            
        

#%% read dataset
df = pd.read_csv('../data_for_student_case.csv')
#df = df.replace(np.nan, '', regex=True)
features = list(df)
#%%
for item in df['bookingdate']:
    item = string_to_timestamp(item)
    
#%% 