import random 
from matplotlib import cm
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure(2,figsize=(13,9),dpi=150)
axi= fig.gca(projection='3d')

[x,y]=np.meshgrid(np.array(range(25))/24.0,
                np.arange(0,505.5,0.5)/575*17*np.pi-2*np.pi)

a=(np.pi/2)*np.exp(-y/(8*np.pi))

b=1-(1-np.mod(3.6*y,2*np.pi)/np.pi)**4/2

c=2*(x**2-x)**2*np.sin(a)

d=b*(x*np.sin(a)+c*np.cos(a))

surface=axi.plot_surface(d*np.cos(y),d*np.sin(y),b*(x*np.cos(a)-c*np.sin(a)),rstride=1,cstride=1,cmap=plt.cm.ocean)

plt.axis('off')
plt.savefig('file.png')
plt.show()