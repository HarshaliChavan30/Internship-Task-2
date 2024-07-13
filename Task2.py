import pandas as pd
import numpy as np
from scipy import stats

data = pd.read_csv('D:\\assignment\\assignment\\TASK2\\01.Data Cleaning and Preprocessing.csv')

type(data)
pd.core.frame.DataFrame
a=data.info
print(data.info) #concise summary 
print('**********************************************************************')
a=data.describe() #descriiptive statistics
print(data.describe())
print('**********************************************************************')

a=data.drop_duplicates() #delete duplicates from dataset
print(data.drop_duplicates)
print('**********************************************************************')

a=data.isnull() #emptyspace in column
print(data.isnull)
print('**********************************************************************')

a=data.notnull 
print(data.notnull)
print('**********************************************************************')

a=data.isnull().sum()
print(a)
print('**********************************************************************')

a=data.isnull().sum().sum()
print(a)
print('**********************************************************************')

data2=data.fillna(value=0)
print(data2)
print('**********************************************************************')

data3 = data.fillna(method='pad')
print(data3)
print('**********************************************************************')

data4=data.fillna(method='bfill')
print(data4)
print('**********************************************************************')

data2.columns
print(data2)
print('**********************************************************************')

data2.drop(['Observation'], axis=1, inplace= True)
data2.columns
print(data2)
print('**********************************************************************')

Q1=data2.quantile(0.25)
Q3=data2.quantile(0.75)
IQR=Q3-Q1
print(IQR)
print('**********************************************************************')

data2=data2[~((data2<(Q1-1.5*IQR)) | (data2>(Q3+1.5*IQR))).any(axis=1)]
print(data2)
print('**********************************************************************')
