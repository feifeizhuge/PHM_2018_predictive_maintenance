# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 14:49:19 2019

@author: VWA08VG
"""

'''
### process fault data:

    tranform it into different dataframe
    old ---['time', 'fault_name', 'Tool']
    new ---['time', 'fault_1', 'fault_2','fault_3']
    
### fault_name:
    
    {'FlowCool Pressure Dropped Below Limit',
     'Flowcool Pressure Too High Check Flowcool Pump',
     'Flowcool leak'}
    
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt, seaborn

train_1 = train_01.copy()
fault_1 = fault_01.copy()

#Todo:
    ###check out wether all fault id is same as 01M02
    #np.sum(fault_01.loc[:,'Tool'] == '01M02')
    
    
#Todo:
    ### check out missing data

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


'''
### processing trainingdata:
    
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

train_pressure = train_1.loc[:,['time','FLOWCOOLPRESSURE']]
train_flowcoolrate = train_1.loc[:,['time','FLOWCOOLFLOWRATE']]


# temp_1(23) doesn't equal to 53, it means the fault time and the time in the
# train are not One-to-one correspondence. 
temp_1 = np.sum(train_pressure.loc[:,'time'].isin(F1_series['time'].tolist()))


'''

### plot pressure with fault occur together

'''
train_pressure.plot.scatter(x='time', y='FLOWCOOLPRESSURE')
plt.scatter(train_pressure['time'], train_pressure['FLOWCOOLPRESSURE'])
'''
Index(['time', 'TTF_FlowCool Pressure Dropped Below Limit',
       'TTF_Flowcool Pressure Too High Check Flowcool Pump',
       'TTF_Flowcool leak'])
'''

RUL.plot(x='time', y='TTF_Flowcool Pressure Too High Check Flowcool Pump')
#plt.stem(F1_series['time'], F1_series['fault_name'],'r-.',label=
#         'Pressure Dropped Below Limit --- red')
plt.stem(F2_series['time'], F2_series['fault_name'],'g-.',label=
         'Pressure Too High Check Flowcool Pump --- green')
#plt.stem(F3_series['time'], F3_series['fault_name'],'y-.',label=
#         'Flowcool leak --- yellow')

plt.legend()
plt.show()


'''

### plot flowcool rate with fault occur together

'''


train_flowcoolrate.plot(x='time', y=['FLOWCOOLFLOWRATE'])
plt.stem(F1_series['time'], F1_series['fault_name'],'r-.',label=
         'Pressure Dropped Below Limit --- red')
plt.stem(F2_series['time'], F2_series['fault_name'],'g-.',label=
         'Pressure Too High Check Flowcool Pump --- green')
plt.stem(F3_series['time'], F3_series['fault_name'],'y-.',label=
         'Flowcool leak --- yellow')
plt.legend()
plt.show()


'''

### calclulate the correlationsmatrix 

'''
#train_1_corr = train_1.corr()
#seaborn.heatmap(train_1_corr, center=0, annot=True)
#plt.show()













