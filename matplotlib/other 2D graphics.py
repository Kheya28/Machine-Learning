import numpy as np
import matplotlib as pylab
import matplotlib.pyplot as plt

#scatter
x=np.linspace(0,10,12)   # 0 theke 10 ke 12 vag kora
n=np.array([0,1,2,3,4,5])
fig,axes=plt.subplots(1,4,figsize=(16,5))  # 4 subplot in a row with size (16,5)
axes[0].set_title('scatter plot')
axes[0].scatter(x,x+0.25*np.random.randn(len(x)))

#step
axes[1].set_title('step')
axes[1].step(n,n**2,lw=2)

#bar
axes[2].set_title('bar')
axes[2].bar(n,n**2,align="center",width=0.5,alpha=0.5)

#bar
axes[3].set_title('fill between')
axes[3].fill_between(x,x**2,x**3,color="green",alpha=0.5)

plt.show()


#radar chart
fig=plt.figure(figsize=(6,6))
ax=fig.add_axes([0.0,0.0,0.6,0.6],polar=True)
t=np.linspace(0,2*np.pi,100)  #a spiral drawing in polar
ax.plot(t,t,color='blue',lw=3)

plt.show()

#Draw Histogram
n=np.random.randn(100000)
fig,axes=plt.subplots(1,2,figsize=(12,4))
axes[0].set_title("Difault Histogram")
axes[0].hist(n)

axes[1].set_title("Cumulative Detailed Histogram")
axes[1].hist(n,cumulative=True,bins=50)

plt.show()




