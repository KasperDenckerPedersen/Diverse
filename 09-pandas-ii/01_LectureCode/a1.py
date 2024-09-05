import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--')
plt.show() #Since we are coding online, this does not work. Only works locally. 
#plt.savefig('01_LectureCode/a1.png')
