import matplotlib.pyplot as plt
import numpy as np

z = np.linspace(0,10,100)

plt.plot(z,z,label='linear')

plt.legend()

plt.show()
