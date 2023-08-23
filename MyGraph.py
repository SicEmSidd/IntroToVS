import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()

#py -3 -m venv introvenv -- this is a way to create a new virtual environment