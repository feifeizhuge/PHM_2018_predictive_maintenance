# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:25:43 2019

@author: VWA08VG
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
        
        
        