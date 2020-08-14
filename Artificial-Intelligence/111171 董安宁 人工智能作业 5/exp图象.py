import numpy as np
import math
import matplotlib.pyplot as plt
x=np.arange(0,10,0.1)
def fun(x):
    return -math.exp(-(x-5))
y1=[fun(a) for a in x]
#y2=[math.log(a,0.5)+2 for a in x]
y3=[a for a in x]
plot1=plt.plot(x,y1,'-g',label="-e(x)")
plt.legend(loc='lower right')
plt.vlines(1, 0, fun(1), colors = "r", linestyles = "dashed")
plt.grid() 
plt.show()

