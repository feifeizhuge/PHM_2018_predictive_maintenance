# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:29:49 2019

@author: VWA08VG
"""

'''
This is a class. It can extra different kinds of feature and visualize them             
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt, seaborn

class df_feature():
    
    def __init__(self, df, df_fault, RUL, kind_fault):
        
        self.parameters_to_plot = ['stage','IONGAUGEPRESSURE', 'ETCHBEAMVOLTAGE', 'ETCHBEAMCURRENT',
    'ETCHSUPPRESSORVOLTAGE', 'ETCHSUPPRESSORCURRENT', 'FLOWCOOLFLOWRATE',
    'FLOWCOOLPRESSURE', 'ETCHGASCHANNEL1READBACK', 'ETCHPBNGASREADBACK','FIXTURESHUTTERPOSITION']
        
        self.parameters = ['IONGAUGEPRESSURE', 'ETCHBEAMVOLTAGE', 'ETCHBEAMCURRENT',
    'ETCHSUPPRESSORVOLTAGE', 'ETCHSUPPRESSORCURRENT', 'FLOWCOOLFLOWRATE',
    'FLOWCOOLPRESSURE', 'ETCHGASCHANNEL1READBACK', 'ETCHPBNGASREADBACK',
    'FIXTURETILTANGLE','ROTATIONSPEED','ACTUALROTATIONANGLE']
        
        self.color = ["#1f77b4", "#ff7f0e", "#2ca02c",
     "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf","#e377c2"]
        
        self.df = df
        self.kind_fault = kind_fault
        self.df_fault = df_fault
        self.RUL = RUL
        self.ind_start = 0
        self.ind_end = 0
        self.df_feature = pd.DataFrame()
        
        
    def find_ind(self, time_start, time_end):
        
        self.ind_start = np.argmin(abs(time_start - self.df.loc[:,'time']))
        self.ind_end = np.argmin(abs(time_end - self.df.loc[:,'time']))
        
        print(self.ind_start)
        print(self.ind_end)
        
    def plot_parameter(self):
        
        slice_data = self.df.iloc[self.ind_start:self.ind_end,]
        slice_data = slice_data.iloc[:,2:20]
        slice_RUL = self.RUL.iloc[self.ind_start:self.ind_end, self.kind_fault]
        labels = {'1':'RUL--the pressure low fault',
                 '2':'RUL--the pressure high fault',
                 '3':'RUL--the pressure leak fault'}
        
        # according to the kind of fault to choose the name of new colunms
        if self.kind_fault == 1:
            
            print('the original data size is:' + str(slice_data.shape))
            self.df_feature = slice_data.assign(RUL_f1=slice_RUL)
            print('successful! RUL has been added into data, the new size of data is: '
                  + str(self.df_feature.shape))
            
        elif self.kind_fault == 2:
            
            print('the original data size is:' + str(slice_data.shape))
            self.df_feature = slice_data.assign(RUL_f2=slice_RUL)
            print('successful! RUL has been added into data, the new size of data is: '
                  + str(self.df_feature.shape))
            
        elif self.kind_fault == 3:
            
            print('the original data size is:' + str(slice_data.shape))
            self.df_feature = slice_data.assign(RUL_f3=slice_RUL)
            print('successful! RUL has been added into data, the new size of data is: '
                  + str(self.df_feature.shape))
        
        else:
            print('die eingegebene Fehlerklasse ist falsch, bitte nur 1 bis 3 eingeben')
            
    
        f, ax = plt.subplots(12,1,sharex=True)
        for ind in range(len(ax)):
            
            # the first is special
            if ind == 0:
                ax[ind].plot(slice_RUL.index, slice_RUL, label=labels[str(self.kind_fault)])
                ax[ind].legend(loc='center left')
            else:
                ax[ind].plot(slice_data.index, slice_data[self.parameters_to_plot[ind-1]], 
                        label=self.parameters_to_plot[ind-1], color=self.color[ind-1])
                ax[ind].legend(loc='center left')
                
        
    def feature_generater(self, rolling_size):
        
        variables = ['IONGAUGEPRESSURE', 'ETCHBEAMVOLTAGE', 'ETCHBEAMCURRENT',
    'ETCHSUPPRESSORVOLTAGE', 'ETCHSUPPRESSORCURRENT', 'FLOWCOOLFLOWRATE',
    'FLOWCOOLPRESSURE', 'ETCHGASCHANNEL1READBACK', 'ETCHPBNGASREADBACK',
    'FIXTURETILTANGLE','ROTATIONSPEED','ACTUALROTATIONANGLE']
        # it saves the new generated features
        df_roll_agg = pd.DataFrame()
        for variable in variables:
            df_roll_agg[variable + '_max'] = self.df_feature[variable].rolling(rolling_size).max()
            df_roll_agg[variable + '_mean'] = self.df_feature[variable].rolling(rolling_size).mean()
            df_roll_agg[variable + '_min'] = self.df_feature[variable].rolling(rolling_size).min()
            df_roll_agg[variable + '_std'] = self.df_feature[variable].rolling(rolling_size).std()
            df_roll_agg[variable + '_var'] = self.df_feature[variable].rolling(rolling_size).var()
            df_roll_agg[variable + '_kurt'] = self.df_feature[variable].rolling(rolling_size).kurt()
            df_roll_agg[variable + '_skew'] = self.df_feature[variable].rolling(rolling_size).skew()
            df_roll_agg[variable + '_p2p'] = self.df_feature[variable].rolling(rolling_size).max() - \
                                             self.df_feature[variable].rolling(rolling_size).min()
                                             
        print('the old size of data is ' + str(df_roll_agg.shape))
        self.df_feature = pd.concat([self.df_feature, df_roll_agg], axis=1)
        print('successful! generated features have been added into data, the new size of data is: '
              + str(self.df_feature.shape))
        
    def plot_corr(self, plot_Heatmap):
        
        labels = {'1':'RUL_f1',
                 '2':'RUL_f2',
                 '3':'RUL_f3'}
        matrix_corr = self.df_feature.corr()
        plt.figure()
        matrix_corr.loc[:,labels[str(self.kind_fault)]].plot.bar()
        plt.title('correlation coefficience of parameters in ' + labels[str(self.kind_fault)]
        + ' between the index ' + str(self.ind_start) + ' to ' + str(self.ind_end))
        
        if plot_Heatmap == 1:
            seaborn.heatmap(matrix_corr, center=0, annot=True)
            
if __name__ == "__main__":
    
    #test 1: for fault one, time [12320000,12430304]
    df_01_fault_1 = df_feature(train_1, fault_1, RUL, 1)
    df_01_fault_1.find_ind(12320000,12430304)
    df_01_fault_1.plot_parameter()  
    df_01_fault_1.feature_generater(100)
    # do not plot heamtmap
    df_01_fault_1.plot_corr(0)
    
    # test 2: [1320000,1430304]
    df_01_fault_2 = df_feature(train_1, fault_1, RUL, 2)
    df_01_fault_2.find_ind(12320000,12430304)
    df_01_fault_2.plot_parameter()  
    df_01_fault_2.feature_generater(100)
    # do not plot heamtmap
    df_01_fault_2.plot_corr(0)
