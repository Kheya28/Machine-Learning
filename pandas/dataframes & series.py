
#series is one dimensional & dataframe is two dimensional
import pandas as pd
import numpy as np

s=pd.Series([1,2,3,4,5,np.nan,6,7])  #creating series
print(s)

#ekhon amra jodi inex 1 theke shuru korte cai
order=[1,2,3,4,5,6,7,8]
s=pd.Series([1,2,3,4,5,np.nan,6,7],order)  #creating series
print(s)

d=pd.date_range('20200323',periods=10)
print(d)

df=pd.DataFrame(np.random.randn(10,4),index=d,columns=['A','B','C','D'])  #dataframe
print(df)

n=np.random.randn(5) #create random ndarray
index=['a','b','c','d','e']
s1=pd.Series(n,index)
print(s1)

#create series from dictionary
d={'a':1,'b':2,'c':3}
s2=pd.Series(d)
print(s2)

#modify the index of series
s2.index=[1,2,3]  #age jotota index chilo totota dewa lagbe
print(s2)

#slicing
a=s2[:2]  # prothom duita value show korbe
print(a)

a=s2[:-2]  #last duita bade bakigula show korbe
print(a)

a=s2[2:] # 1st duita bade bakigula show korbe
print(a)

a=s2[-2:]  #last duita  show korbe
print(a)

#append
#s1 er sathe s2 append
s3=s1.append(s2)
print(s3)
s3=s3.drop(3) #s3 er vitore rekhe change korte hobe,,ekhane 3 index delete hoye geche
print(s3)



#https://www.youtube.com/watch?v=PfVxFV1ZPnk
#https://www.youtube.com/watch?v=UB3DE5Bgfx4