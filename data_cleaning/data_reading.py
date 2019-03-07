# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 12:39:39 2019

@author: he 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


"""
####################################
 find path of datasets and load it 
 
 RUL --> remaining useful life
 train_01 --> training data
 fault_01 --> fault data
####################################
"""

# get current path of running file
current_path = os.path.dirname(__file__)
ober_path = os.path.dirname(current_path)
train_path = current_path + '/01_M02_DC_train.csv'
fault_path = current_path + '/train_faults/01_M02_train_fault_data.csv'
remaining_life_path = current_path + '/train_ttf/01_M02_DC_train.csv' 

# load data with read_csv
#train_01 = pd.read_csv(train_path, sep=',')
#fault_01 = pd.read_csv(fault_path, sep=',')
#RUL = pd.read_csv(remaining_life_path, sep=',')

"""
####################################################
  Fault data processing 
  
  transform the fault dataframe into three different 
  data series
####################################################
"""

train_1 = train_01.copy()
fault_1 = fault_01.copy()

# use dict to map all kinds of faults to simpler strings
fault_dict = {'1':'FlowCool Pressure Dropped Below Limit',
              '2':'Flowcool Pressure Too High Check Flowcool Pump',
              '3':'Flowcool leak'}

# get F1,F2,F3 Series
falg_value = 1 
F1_series = fault_1[fault_1['fault_name'] == fault_dict['1']].iloc[:,0:2]
F1_series['fault_name'] = falg_value
F1_series.index = np.arange(0, len(F1_series))

F2_series = fault_1[fault_1['fault_name'] == fault_dict['2']].iloc[:,0:2]
F2_series['fault_name'] = falg_value
F2_series.index = np.arange(0, len(F2_series))

F3_series = fault_1[fault_1['fault_name'] == fault_dict['3']].iloc[:,0:2]
F3_series['fault_name'] = falg_value
F3_series.index = np.arange(0, len(F3_series))
  
fault_count = pd.DataFrame({fault_dict['1']:len(F1_series),
                           fault_dict['2']:len(F2_series),
                           fault_dict['3']:len(F3_series)
                            }, index=[0])


"""
##################################################################
  Data visulisation 
  
  1. Overview of the whole training dataset(on selected parameter)
  
  2. plot RUL and corresponding fault point, so that 
  determine the fault punkt
  
  3. plot all three kinds of fault together
###################################################################
"""

'''
### 1. Overview of the whole dataset
    
    processing trainingdata:
    
    ## data columns:
    'time', 'Tool', 'stage', 'Lot', 'runnum', 'recipe', 'recipe_step',
    'IONGAUGEPRESSURE', 'ETCHBEAMVOLTAGE', 'ETCHBEAMCURRENT',
    'ETCHSUPPRESSORVOLTAGE', 'ETCHSUPPRESSORCURRENT', 'FLOWCOOLFLOWRATE',
    'FLOWCOOLPRESSURE', 'ETCHGASCHANNEL1READBACK', 'ETCHPBNGASREADBACK',
    'FIXTURETILTANGLE', 'ROTATIONSPEED', 'ACTUALROTATIONANGLE',
    'FIXTURESHUTTERPOSITION', 'ETCHSOURCEUSAGE', 'ETCHAUXSOURCETIMER',
    'ETCHAUX2SOURCETIMER', 'ACTUALSTEPDURATION']
    
    select specific columns : 'FLOWCOOLPRESSURE'
'''

selected_parameter = 'FLOWCOOLPRESSURE'
train_pressure = train_1.loc[:,['time', selected_parameter]]
train_pressure.plot.scatter(x='time', y=selected_parameter)
plt.title('overview ' + selected_parameter + ' on the whole data')

'''
### 2. plot RUL and corresponding fault point
'''

fault_name = ['TTF_FlowCool Pressure Dropped Below Limit',
              'TTF_Flowcool Pressure Too High Check Flowcool Pump',
              'TTF_Flowcool leak']

RUL.plot(x='time', y=fault_name[0], label='RUL')
plt.stem(F1_series['time'], F1_series['fault_name'],'r-.',label=
         'Pressure Dropped Below Limit')
plt.legend()
plt.title(fault_name[0])

RUL.plot(x='time', y=fault_name[1], label='RUL')
plt.stem(F2_series['time'], F2_series['fault_name'],'g-.',label=
         'Pressure Too High Check Flowcool Pump')
plt.legend()
plt.title(fault_name[1])

RUL.plot(x='time', y=fault_name[2], label='RUL')
plt.stem(F3_series['time'], F3_series['fault_name'],'g-.',label=
         'TTF_Flowcool leak')
plt.legend()
plt.title(fault_name[2])

'''
### 3. plot all three kinds of fault together
'''
plt.figure()
plt.stem(F1_series['time'], F1_series['fault_name'],'r-.',label=
         'Pressure Dropped Below Limit --- red')
plt.stem(F2_series['time'], F2_series['fault_name'],'g-.',label=
         'Pressure Too High Check Flowcool Pump --- green')
plt.stem(F3_series['time'], F3_series['fault_name'],'y-.',label=
         'Flowcool leak --- yellow')
plt.legend()

"""
###########################################
 padding the empty time index 
 
 because fault time index is not same as
 traning data's time index
###########################################
"""

'''

align the index in original data and fault data:
    
    1. initialise a seriese and fill with zero
    2. make a for loop and check wheather the index of fault is in the original
    data, if True set it as 1 
          else such the nearst index forward.
'''

#a = train_1['time'].isin(F1_series.iloc[:,0])
# initailise 
F1_new_col = pd.Series(np.zeros(len(train_1)))
count_f1 = 0 

for i in F1_series.index:
    # True: fault index is in the data's time index
    check_flag = F1_series.iloc[i,0] == train_1['time']
    if any(check_flag):
        # find the index and a
        index = np.argmax(check_flag)
        F1_new_col[index] = 1
        count_f1 = count_f1 + 1
        
    # False: fault index is not in the data's time index, then find the nearst
    # index to replace it 
    else:
        # use "diff" to record the distance between fault'time with data'time
        diff = abs(F1_series.iloc[i,0]-train_1.loc[:,'time'])
        index = np.argmin(diff)
        F1_new_col[index] = 1
        count_f1 = count_f1 + 1 


### do the same for F2
        
F2_new_col = pd.Series(np.zeros(len(train_1)))
count_f2 = 0 

for i in F2_series.index:
    # True: fault index is in the data's time index
    check_flag = F2_series.iloc[i,0] == train_1['time']
    if any(check_flag):
        # find the index and a
        index = np.argmax(check_flag)
        F2_new_col[index] = 1
        count_f2 = count_f2 + 1
        
    # False: fault index is not in the data's time index, then find the nearst
    # index to replace it 
    else:
        # use "diff" to record the distance between fault'time with data'time
        diff = abs(F2_series.iloc[i,0]-train_1.loc[:,'time'])
        index = np.argmin(diff)
        F2_new_col[index] = 1
        count_f2 = count_f2 + 1 
        
  ### do the same for F3      
F3_new_col = pd.Series(np.zeros(len(train_1)))
count_f3 = 0 

for i in F3_series.index:
    # True: fault index is in the data's time index
    check_flag = F3_series.iloc[i,0] == train_1['time']
    if any(check_flag):
        # find the index and a
        index = np.argmax(check_flag)
        F3_new_col[index] = 1
        count_f3 = count_f3 + 1
        
    # False: fault index is not in the data's time index, then find the nearst
    # index to replace it 
    else:
        # use "diff" to record the distance between fault'time with data'time
        diff = abs(F3_series.iloc[i,0]-train_1.loc[:,'time'])
        index = np.argmin(diff)
        F3_new_col[index] = 1
        count_f3 = count_f3 + 1 





