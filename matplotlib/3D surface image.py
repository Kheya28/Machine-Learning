import numpy as np
import matplotlib as pylab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D


delta=0.025
x=np.arange(-3.0,3.0,delta)
y=np.arange(-2.0,2.0,delta)
X,Y=np.meshgrid(x,y)
Z1=np.exp(-X**2-Y**2)
Z2=np.exp(-(X-1)**2-(Y-1)**2)
Z=(Z1-Z2)*2

#draw 3D surface image
fig=plt.figure(figsize=(14,6))

#specify 3D graphics to draw with projection='3d'
ax=fig.add_subplot(1,2,1,projection='3d')  # add_subplot vitorer number change er sathe sathe shape o change hoy
ax.plot_surface(X,Y,Z,rstride=4,cstride=4,linewidth=0)
plt.show()

#heatmap.......color map
languages='python','java','c','c++','c#'
popularity=[22.2,17.6,8.8,8,7.7]
color=["blue","green","black","yellow","red"]
#explode 1st slice
explode=(0.1,0,0,0,0)
plt.pie(popularity,explode=explode,labels=languages,colors=color,autopct='%1.1f%%',shadow=True,startangle=140)

plt.show()


#https://www.youtube.com/watch?v=OKJyGzgWP6c




