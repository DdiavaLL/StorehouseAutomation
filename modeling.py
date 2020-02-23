import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig = plt.figure()
ax = plt.subplot()

# Defining the coordinate system
x = [i for i in range(0, 5)]
y = [i for i in range(0, 5)]

# Variant 1
x_length = np.linspace(0, len(x))
# y1_width = 0
# y2_width = 10
# ax.fill_between(x_length, y1_width, y2_width, color='black')

# Variant 2
ax.set_facecolor("black")
y1_width = 0
y2_width = len(y)
ax.fill_between(x_length, y1_width, y2_width, color='#F0E6E6')

# Setting the grid parameters
plt.title('Storehouse', color='white')
plt.xlabel('Length', color='white')
plt.ylabel('Width', color='white')

# Drawing the walls of the storehouse
w1X = [x[0]-1, x[0]]
w1Y = [y[len(y)-1]+2, y[len(y)-1]+1]

w2X = [x[0]-1, x[0]]
w2Y = [y[0]-1, y[0]]

w3X = [x[len(x)-1]+1, x[len(x)-1]+2]
w3Y = [y[len(y)-1]+1, y[len(y)-1]+2]

w4X = [x[len(x)-1]+1, x[len(x)-1]+2]
w4Y = [y[0],y[0]-1]

# Drawing graphs
plt.plot(w1X, w1Y, color='red')
plt.plot(w2X, w2Y, color='red')
plt.plot(w3X, w3Y, color='red')
plt.plot(w4X, w4Y, color='red')
plt.scatter((len(x)-1)/2+0.5, -0.5, color='green')      # Agent

plt.grid(color='black', linewidth=2, axis='both')
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
plt.show()
