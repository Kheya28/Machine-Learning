
import numpy as np
import matplotlib as pylab
import matplotlib.pyplot as plt
#print(pylab.__version__)

plt.close('all')
x=np.linspace(0,10,12)   # 0 theke 10 ke 12 vag kora
y=x*x+2
print(x)
print(y)
print(np.array([x,y]).reshape(12,2))  #array reshape kora

plt.plot(x,y,'r')  # third parameter defines color & line style,,r means red
plt.show()





















