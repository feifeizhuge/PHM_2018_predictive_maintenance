# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:57:44 2019

@author: VWA08VG
"""

'''
find the nearst point in the index of data
'''

parameters = ['stage','IONGAUGEPRESSURE', 'ETCHBEAMVOLTAGE', 'ETCHBEAMCURRENT',
    'ETCHSUPPRESSORVOLTAGE', 'ETCHSUPPRESSORCURRENT', 'FLOWCOOLFLOWRATE',
    'FLOWCOOLPRESSURE', 'ETCHGASCHANNEL1READBACK', 'ETCHPBNGASREADBACK','FIXTURESHUTTERPOSITION']

c = ["#1f77b4", "#ff7f0e", "#2ca02c",
     "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf","#e377c2"]

#def ind_find(start,end,df):
    
    
start = 7930000
end = 8059956

lowwer_index_f1 = np.argmin(abs(start-train_1.loc[:,'time']))
#lowwer_index_f1 = 725000
upper_index_f1 = np.argmin(abs(end-train_1.loc[:,'time']))
    

'''
detect the first fault -- FlowCool Pressure Dropped Below Limit
'''
slice_data_f1 = train_1.iloc[lowwer_index_f1:upper_index_f1,]
slice_RUL_f1 = RUL.iloc[lowwer_index_f1:upper_index_f1,1]


f1, ax1 = plt.subplots(12,1,sharex=True)
for ind in range(len(ax1)):
    
    # the first is special
    if ind == 0:
        ax1[ind].plot(slice_RUL_f1.index, slice_RUL_f1, label='RUL--the pressure low fault')
        ax1[ind].legend(loc='center left')
    else:
        ax1[ind].plot(slice_data_f1.index, slice_data_f1[parameters[ind-1]], 
                label=parameters[ind-1], color=c[ind-1])
        ax1[ind].legend(loc='center left')
    
plt.show()
f1.title('fault 1')


'''
detect the second fault -- Flowcool Pressure Too High Check Flowcool Pump
'''
start = 12320000
end = 12430304

lowwer_index_f2 = np.argmin(abs(start-train_1.loc[:,'time']))
#lowwer_index_f2 = 1280000
upper_index_f2 = np.argmin(abs(end-train_1.loc[:,'time']))

slice_data_f2 = train_1.iloc[lowwer_index_f2:upper_index_f2,]
slice_RUL_f2 = RUL.iloc[lowwer_index_f2:upper_index_f2,2]

f2, ax2 = plt.subplots(12,1,sharex=True)
for ind in range(len(ax2)):
    
    # the first is special
    if ind == 0:
        ax2[ind].plot(slice_RUL_f2.index, slice_RUL_f2, label='RUL--the pressure too high fault')
        ax2[ind].legend(loc='center left')
    else:
        ax2[ind].plot(slice_data_f2.index, slice_data_f2[parameters[ind-1]], 
                label=parameters[ind-1], color=c[ind-1])
        ax2[ind].legend(loc='center left')
    
plt.show()
