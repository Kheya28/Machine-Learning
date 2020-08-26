import numpy as np
import pandas as pd

df=pd.DataFrame({'A':[1,2,2,2,3,3,4,5,6,7]})
print(df)
df=df.loc[df['A'].shift()!=df['A']]   # it removes the repeated data
print(df)

