# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 10:53:47 2019

@author: VWA08VG
"""

'''
After the processing data, we add three new columns(F1,F2,F3) to the original 
data and choose the reasonable slice and save it as csv data. 
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt, seaborn

#train_added = train_01.assign(F1=F1_new_col, F2=F2_new_col, F3=F3_new_col)
## make a slice
#train_added = train_added[147680:1351556]
#
## save it as 'csv' file
#train_added.to_csv("01_M02_train_selected.csv")

'''
After the processing data, we add the following new columns:
    1. RUL of fault one
    2. RUL of fault two
    3. RUL of fault three
    4. maximal value
    5. mean value
    6. minimal value
    7. std value
    8. varianz value
    9. kurtosis
    10. skewness
    11. peak
'''

variables = ['IONGAUGEPRESSURE', 'ETCHBEAMVOLTAGE', 'ETCHBEAMCURRENT',
    'ETCHSUPPRESSORVOLTAGE', 'ETCHSUPPRESSORCURRENT', 'FLOWCOOLFLOWRATE',
    'FLOWCOOLPRESSURE', 'ETCHGASCHANNEL1READBACK', 'ETCHPBNGASREADBACK',
    'FIXTURETILTANGLE','ROTATIONSPEED','ACTUALROTATIONANGLE']

#start_1 = 725000
#end_1 = 813922
#
#start_2 = 1280000
#end_2 = 1351556

# a selected piece of data corresponding to fault 1 (pressure low) 
selected_f1 = slice_data_f1.iloc[:,2:20]
selected_f1 = selected_f1.assign(RUL_f1=slice_RUL_f1)
# a selected piece of data corresponding to fault 2 (pressure high) 
selected_f2 = slice_data_f2.iloc[:,2:20]
selected_f2 = selected_f2.assign(RUL_f2=slice_RUL_f2)

add_feature_f1 = feature_generation('fault_1')
fault1_features = add_feature_f1.statistical_features(selected_f1, variables, 100)
all_features_f1 = pd.concat([selected_f1, fault1_features], axis=1)

add_feature_f2 = feature_generation('fault_2')
fault2_features = add_feature_f2.statistical_features(selected_f2, variables, 100)
all_features_f2 = pd.concat([selected_f2, fault2_features], axis=1)

#plt.figure()
#fault_1_corr = all_features_f1.corr()
#fault_1_corr.loc[:,'RUL_f1'].plot.bar()
#seaborn.heatmap(fault_1_corr, center=0, annot=True)
#plt.show()
#
#plt.figure()
#fault_2_corr = all_features_f2.corr()
##fault_2_corr.loc[:,'RUL_f2'].plot.bar()
#seaborn.heatmap(fault_2_corr, center=0, annot=True)
#plt.show()

