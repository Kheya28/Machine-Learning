import numpy as np
import matplotlib as pylab
import matplotlib.pyplot as plt

#drawing a subgraph

x=np.linspace(0,10,12)   # 0 theke 10 ke 12 vag kora
y=x*x+2

plt.subplot(1,2,1)  #the contents are rows,columns & indexes
plt.plot(x,y,'r--')  # third parameter defines color & line style,,,,r-- means red color & dashed line

plt.subplot(1,2,2)
plt.plot(y,x,'g*-')
plt.show()
plt.close('all')

#draw a picture or graph,inside another graph

fig=plt.figure()
#fig=plt.figure(figsize=(16,9))  #figure size o bola jay
#fig=plt.figure(figsize=(16,9),dpi=300)

axes1=fig.add_axes([0.1,0.1,0.8,0.8]) #big axes  #control the left,right,width,height of the canvas from 0 to 1
axes2=fig.add_axes([0.2,0.5,0.3,0.4]) #small axes

axes1.plot(x,y,'g',marker='o',markersize=10)
axes2.plot(y,x,'r')

axes1.set_xlabel("x")
axes1.set_ylabel("y")
axes1.set_title("titleeeeeeee")

axes2.set_xlabel("xxxx")
axes2.set_ylabel("yyy")
axes2.set_title("title")

#plt.plot(x,x**2,'r',alpha=0.8,linewidth=2,linestyle=':',marker='o',markersize=10) #linewidth mane holo line kototuku cikon ba mota hoy
#plt.plot(x,x**3,marker='+')
#plt.plot(x,x**4)
#plt.legend(["y=x**2","y=x**3"],loc=6)  #plot er pore dite hoy  #loc mane kon position e legend show korbe


plt.show()




#https://www.youtube.com/watch?v=OKJyGzgWP6c