#numpy takes less memory than list & it is fast & conveinient
import numpy as np

a=np.array([1,2,3])  #one dimensional array
print(a)

a=np.array([(1,2,3),(4,5,6)]) #two dimensional
print(a)
print(a.ndim)  #koto dimensional ta print kore
print(a.dtype)  #data type
print(a.size) #kotota element ache
print(a.shape)  #kotota row r column

#slicing
print(a[0,2])  # 0th row er 2th column er value
print(a[0:,2]) # 0 soho protita row er 2th column er value print kora
print(a[0:1,2])  # 0 soho protita row er 2th column er value print kora(majhkhane 1 deway 1ta porjonto kaj korbe)

#reshape
a=a.reshape(3,2)  #eta array er shape change kore
print(a)


a=np.arange(10)
print(a)

a=np.zeros((3,3))
print(a)

a=np.ones((3,3))
print(a)

a=np.full((3,3),7)
print(a)

a=np.eye(2)  #2X2 identity matrix
print(a)

a=np.random.random((2,2)) #array filled with random values
print(a)

a=np.linspace(1,3,5)  #1 theke 3 ke 5ta value te vag kora
print(a)

a=np.array([1,2,3])
print(a.max())
print(a.min())
print(a.sum())

#the rows r called axis 1 & colums are called axis 0
a=np.array([(1,2,3),(4,5,6)])
print(a.sum(axis=0))  #(1+4),(2+5),(3+6),,,,coloumn onujayi jog
print(a.sum(axis=1))  # (1+2+3),(4+5+6),,,row onujayi jog

print(np.sqrt(a))  #protita value er square root
print(np.std(a))  #standard deviation of a
#jodi ei 2-dimensional array ke one dimensional e ante cai tahole..
print(a.ravel())

#matrix r matrix e jog,biyog,gun,vag
a=np.array([(1,2,3),(4,5,6)])
b=np.array([(1,2,3),(4,5,6)])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#ekta array er sathe arektake attach kora
print(np.vstack((a,b))) #vertically add
print(np.hstack((a,b)))  #horizontally add


#https://www.youtube.com/watch?v=8JfDAm9y_7s