
import pandas as pd
import numpy as np

arr1=[6,7,8,9,5]
arr2=[0,1,2,3,4,5,7]


s5=pd.Series(arr1)
s6=pd.Series(arr2)

print(s5.add(s6)) #duita series jog
print(s5.sub(s6)) #minus
print(s5.mul(s6)) #multiply
print(s5.div(s6)) #division
print(s6.median())
print(s6.max())
print(s6.min())













