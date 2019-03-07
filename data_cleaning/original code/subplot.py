# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 13:08:23 2019

@author: he
"""

'''
### subplot for different parameters
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt, seaborn

'''
### useful parameters:
    'IONGAUGEPRESSURE', 'ETCHBEAMVOLTAGE', 'ETCHBEAMCURRENT',
    'ETCHSUPPRESSORVOLTAGE', 'ETCHSUPPRESSORCURRENT', 'FLOWCOOLFLOWRATE',
    'FLOWCOOLPRESSURE', 'ETCHGASCHANNEL1READBACK', 'ETCHPBNGASREADBACK',
'''

parameters = ['IONGAUGEPRESSURE', 'ETCHBEAMVOLTAGE', 'ETCHBEAMCURRENT',
    'ETCHSUPPRESSORVOLTAGE', 'ETCHSUPPRESSORCURRENT', 'FLOWCOOLFLOWRATE',
    'FLOWCOOLPRESSURE', 'ETCHGASCHANNEL1READBACK', 'ETCHPBNGASREADBACK']

def spines_invisible(ax_obj):
    
    ax_obj.spines['right'].set_visible(False)
    ax_obj.spines['top'].set_visible(False)
    #ax_obj.spines['bottom'].set_visible(False)
    plt.xticks([])
    
## Creates two subplots and unpacks the output array immediately
#f, ax_list = plt.subplots(10, 1, sharey=True, sharex=True)
## Remove the spine and trick from the axis
#[spines_invisible(ax_obj) for ax_obj in ax_list]

## plot first fault indicator
#ax_list[0].plot(F1_series['time'],F1_series['fault_name'],'.')
#
## plot the rest parameters
#for index, para in enumerate(parameters):
#    
#    ax_list[index+1].plot(train_1['time'], train_1[para],'-')
#    #ax_list[index+1].ylim(np.min(train_1[para]), np.max(train_1[para]))
    
    
#ax = plt.subplot(3,1,1)
#ax.plot(F2_series['time'],F2_series['fault_name'],'r.', label='fault indicator')
#spines_invisible(ax)
#plt.legend()
#
#ax1 = plt.subplot(3,1,2)
#ax1.plot(train_1['time'], train_1['FLOWCOOLFLOWRATE'],'g-', label='FLOWCOOLFLOWRATE')
#spines_invisible(ax1)
#plt.legend()
#
#ax2 = plt.subplot(3,1,3)
#ax2.plot(train_1['time'], train_1['FLOWCOOLPRESSURE'],'b-', label='FLOWCOOLPRESSURE')
#spines_invisible(ax2)
#plt.legend()

f, ax = plt.subplots(3,1)
ax[0].plot(F2_series['time'],F2_series['fault_name'],'r.', label='fault indicator')
spines_invisible(ax[0])
ax[0].set_xlim([train_1['time'][0], np.max(train_1['time'])])


ax[1].plot(train_1['time'], train_1['FLOWCOOLFLOWRATE'],'g-', label='FLOWCOOLFLOWRATE')
spines_invisible(ax[1])


ax[2].plot(train_1['time'], train_1['FLOWCOOLPRESSURE'],'b-', label='FLOWCOOLPRESSURE')
spines_invisible(ax[2])
f.align_xlabels()



