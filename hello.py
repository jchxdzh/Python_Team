import matplotlib.pyplot as plt
import numpy as np
x=list(np.arange(-20,20,0.05))
y=[]
for i in range(len(x)):
    y.append(int(1/x[i])*x[i])
plt.plot(x,y)
plt.show()