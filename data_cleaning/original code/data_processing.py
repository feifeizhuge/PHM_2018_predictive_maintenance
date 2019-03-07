# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 13:09:59 2019

@author: he
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


"""
 find path of datasets and load it 
"""



# creat a copy of variable "df"
train_1 = train_01.copy()
train_pressure = train_1.loc[:,'FLOWCOOLPRESSURE']
plt.plot(np.arange(0,len(train_pressure)), train_pressure)
#fault_1 = fault_01_M02.copy()

# df1 selection by label
#flowcoolPressure = df1.loc[:,'TTF_Flowcool leak']
#flowcoolPressure.plot()

# select the fault of Flowcool leak
'''
faults name:
    F1 --  FlowCool Pressure Dropped Below Limit
    F2 --  Flowcool Pressure Too High Check Flowcool Pump
    F3 --  Flowcool leak
'''
#F1_index = fault_1.loc[:,'fault_name'] == 'FlowCool Pressure Dropped Below Limit'
#F1_time = fault_1[F1_index].loc[:,'time']
#plt.scatter(np.arange(0,len(F1_time)), F1_time)

"""
ttf columns:
    ['time', 
    'TTF_FlowCool Pressure Dropped Below Limit',
    'TTF_Flowcool Pressure Too High Check Flowcool Pump',
    'TTF_Flowcool leak']
"""

#ttf_1.plot(x='time',y=['TTF_Flowcool Pressure Too High Check Flowcool Pump'])
#ttf_1.plot(x='time',y=['TTF_FlowCool Pressure Dropped Below Limit'])
#ttf_1.plot(x='time',y=['TTF_Flowcool leak'])
