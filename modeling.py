import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

fig = plt.figure()
ax = plt.subplot()

# Coordinates of the upper-left points occupied by the box.
box_coord = []

# Defining the coordinate system
x = [i for i in range(0, 25)]
y = [i for i in range(0, 25)]

# Coordinates of the agent.
ag_coord = [(len(x)-1)/2+0.5, -0.5]
ag_box = True
ag_color = 'blue'

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

# Setting the grid parameters.
plt.title('Storehouse', color='white')
plt.xlabel('Length', color='white')
plt.ylabel('Width', color='white')

# Drawing the walls of the storehouse.
w1X = [x[0]-1, x[0]]
w1Y = [y[len(y)-1]+2, y[len(y)-1]+1]

w2X = [x[0]-1, x[0]]
w2Y = [y[0]-1, y[0]]

w3X = [x[len(x)-1]+1, x[len(x)-1]+2]
w3Y = [y[len(y)-1]+1, y[len(y)-1]+2]

w4X = [x[len(x)-1]+1, x[len(x)-1]+2]
w4Y = [y[0], y[0]-1]

# Fills in the grid cell occupied by the box.
def box_in_position(x1, y1, y2):
    ax.fill_between(x1, y1, y2, color='green')
    box_coord.append((x1, y1))

# Fills in the area that the agent left.
def ag_fill():
    if ag_coord[1] < 0:
        ax.fill_between(0, 0, -3, color='black')
    elif ag_box:
        ax.fill_between(ag_coord[0]-0.5, ag_coord[1]+0.5, ag_coord[1]-0.5, color='#F0E6E6')
    else:
        box_in_position(ag_coord[0]-0.5, ag_coord[1]+0.5, ag_coord[1]-0.5)

# Agent moves.
def ag_moves():
    ag_coord[1] += 1
    plt.scatter(ag_coord[0], ag_coord[1], color=ag_color)

# Agent status (whether the box is transporting or not).
def ag_status():
    if ag_box:
        ag_color = 'yellow'
    else:
        ag_color = 'blue'

# Drawing graphs.
plt.plot(w1X, w1Y, color='red')
plt.plot(w2X, w2Y, color='red')
plt.plot(w3X, w3Y, color='red')
plt.plot(w4X, w4Y, color='red')
if not ag_box:
    ag_status(ag_color)
    plt.scatter(ag_coord[0], ag_coord[1], color=ag_color)      # Agent
else:
    plt.scatter(ag_coord[0], ag_coord[1], color=ag_color)

# ag_moves()
# ag_fill()
# ag_moves()
# ag_fill()
plt.grid(color='black', linewidth=2, axis='both')
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
plt.show()
