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

#%% library
def string_to_timestamp(date_string):#convert time string to float value
    time_stamp = time.strptime(date_string, '%Y-%m-%d %H:%M:%S')
    return time.mktime(time_stamp)

#%% read dataset
df = pd.read_csv('../data_for_student_case.csv')

#%% 