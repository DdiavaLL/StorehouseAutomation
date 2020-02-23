import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig = plt.figure()
ax = plt.subplot()

# Variant 1
x_length = np.linspace(0, 10)
# y1_width = 0
# y2_width = 10
# ax.fill_between(x_length, y1_width, y2_width, color='black')

# Variant 2
ax.set_facecolor("black")
y1_width = 0
y2_width = 10
ax.fill_between(x_length, y1_width, y2_width, color='#F0E6E6')

# Defining the coordinate system
x = np.linspace(0, 10)
y = np.linspace(0, 10)

# Setting the grid parameters
plt.title('Storehouse', color='white')
plt.xlabel('Length', color='white')
plt.ylabel('Width', color='white')

plt.plot(x, y)
plt.grid(color='black', linewidth=2, axis='both')
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
plt.show()
