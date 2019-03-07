# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:30:02 2019

@author: VWA08VG
"""

'''
in this code I will determine how to use pandan window functions
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class feature_generation:
    def __init__(self, name):
        self.name = name

    def statistical_features(self, df, variables, rolling_size):
        df_roll_agg = pd.DataFrame()
        #df_roll_agg['index'] = df.index
        #print(df_roll_agg['index'])
        for variable in variables:
            #df_roll_agg[variable] = df[variable]
            df_roll_agg[variable + '_max'] = df[variable].rolling(rolling_size).max()
            df_roll_agg[variable + '_mean'] = df[variable].rolling(rolling_size).mean()
            df_roll_agg[variable + '_min'] = df[variable].rolling(rolling_size).min()
            df_roll_agg[variable + '_std'] = df[variable].rolling(rolling_size).std()
            df_roll_agg[variable + '_var'] = df[variable].rolling(rolling_size).var()
            df_roll_agg[variable + '_kurt'] = df[variable].rolling(rolling_size).kurt()
            df_roll_agg[variable + '_skew'] = df[variable].rolling(rolling_size).skew()
            df_roll_agg[variable + '_p2p'] = df[variable].rolling(rolling_size).max() - \
                                             df[variable].rolling(rolling_size).min()
                                         
        return df_roll_agg
                                             
                         