import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.title('Storehouse', color='white')
plt.xlabel('Length', color='white')
plt.ylabel('Width', color='white')

plt.plot(x, y)
plt.grid(color='black', axis='both')
plt.show()