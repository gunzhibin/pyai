#-*- coding:utf-8 -*-
# author:gunzhibin
# datetime:2018/6/9 15:50
# software: PyCharm Community Edition
import numpy as nm
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import Image
import warnings
import scipy
from sklearn.model_selection import train_test_split
warnings.filterwarnings('ignore')
#%matplotlib inline
data = pd.read_csv('F:/train.csv')
print(data.shape,data.shape)
print(data)
data_select = data[['badroom','area','neighborhood','saleprice']]
data_select = data_select.rename(columns = {'badroom':'room'})
data_select = data_select.dropna(axis=0)
for col in nm.take(data_select.columns,[0,1,-1]):
    data_select[col] /= data_select[col].max()
#data_select.head()
print(data_select)
train,test = train_test_split(data_select.copy(),test_size=0.9)
train.describe()

def linear(feature,pars):
    price = nm.sum(feature*pars[:-1],axis=1),pars[-1]
    return price
train['predict'] = linear(train[['room','area']].values,nm.array([0.1,0.1,0.0]))
train.head()