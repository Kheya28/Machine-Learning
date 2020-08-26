import numpy as np
import matplotlib as pylab
import matplotlib.pyplot as plt


x=np.linspace(0,10,12)   # 0 theke 10 ke 12 vag kora
y=x*x+2

fig,axes=plt.subplots(1,2,figsize=(10,5))

axes[0].plot(x,x**2,x**3,lw=2)
axes[0].grid(True)

axes[1].plot(x,x**2,x**3,lw=2)
axes[1].set_xlim(2,5)  # xlimit of data
axes[1].set_ylim(0,60)
#axes[1].grid(True)

plt.show()

