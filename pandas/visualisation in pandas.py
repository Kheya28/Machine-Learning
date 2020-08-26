
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import U matplotlib
#%matplotlib inline

plt.close('all')
#series & dataframe line chart
ts=pd.Series(np.random.randn(50),index=pd.date_range('today',periods=50))
ts=ts.cumsum()  #cumulative sum
ts.plot()
plt.show()


df=pd.DataFrame(np.random.randn(50,4),index=ts.index,columns=['A','B','C','D'])
df=df.cumsum()
df.plot()
plt.show()


'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])

fig, ax = plt.subplots()
df.plot.area(ax=ax);
plt.show()
'''

