import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Starting data for the graph.
class GraphData:
    def __init__(self):
        # Defining the coordinate system
        self.x = [i for i in range(0, 5)]
        self.y = [i for i in range(0, 5)]

        # Coordinates of the agent.
        self.ag_coord = [(len(self.x)-1)/2+0.5, -0.5]
        self.ag_box = True
        self.ag_color = 'blue'

        # Coordinates of the upper-left points occupied by the box.
        self.box_coordinates = []

# Contains methods for drawing the graph.
class Graph:
    my_GraphData = GraphData()
    fig = plt.figure()
    ax = plt.subplot()

    def __init__(self):
        self.y1_width = 0
        self.y2_width = len(self.my_GraphData.y)
        self.x_length = np.linspace(0, len(self.my_GraphData.x))

    def draw_graph(self):
        Graph.ax.set_facecolor("black")
        Graph.ax.fill_between(self.x_length, self.y1_width, self.y2_width, color='#F0E6E6')

        # Setting the grid parameters.
        plt.title('Storehouse', color='white')
        plt.xlabel('Length', color='white')
        plt.ylabel('Width', color='white')

        points = Graph.draw_graph_area(self)
        Graph.ag_status(self)
        # Drawing graphs.
        plt.plot(points[0][0], points[0][1], color='red')
        plt.plot(points[1][0], points[1][1], color='red')
        plt.plot(points[2][0], points[2][1], color='red')
        plt.plot(points[3][0], points[3][1], color='red')

        plt.grid(color='black', linewidth=2, axis='both')
        Graph.ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        Graph.ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
        plt.show()

    # Drawing the walls of the storehouse.
    def draw_graph_area(self):
        w1x = [self.my_GraphData.x[0] - 1, self.my_GraphData.x[0]]
        w1y = [self.my_GraphData.y[self.y2_width - 1] + 2, self.my_GraphData.y[self.y2_width - 1] + 1]

        w2x = [self.my_GraphData.x[0] - 1, self.my_GraphData.x[0]]
        w2y = [self.my_GraphData.y[0] - 1, self.my_GraphData.y[0]]

        w3x = [self.my_GraphData.x[len(self.my_GraphData.x) - 1] + 1, self.my_GraphData.x[len(self.my_GraphData.x) - 1] + 2]
        w3y = [self.my_GraphData.y[self.y2_width - 1] + 1, self.my_GraphData.y[self.y2_width - 1] + 2]

        w4x = [self.my_GraphData.x[len(self.my_GraphData.x) - 1] + 1, self.my_GraphData.x[len(self.my_GraphData.x) - 1] + 2]
        w4y = [self.my_GraphData.y[0], self.my_GraphData.y[0] - 1]
        return [[w1x, w1y], [w2x, w2y], [w3x, w3y], [w4x, w4y]]

    # Fills in the grid cell occupied by the box.
    def box_in_position(self, x1, y1, y2):
        Graph.ax.fill_between(x1, y1, y2, color='green')
        self.my_GraphData.box_coordinates.append((x1, y1))

    # Fills in the area that the agent left.
    def ag_fill(self):
        if self.my_GraphData.ag_coord[1] < 0:
            Graph.ax.fill_between(0, 0, -3, color='black')
        elif self.my_GraphData.ag_box:
            Graph.ax.fill_between(self.my_GraphData.ag_coord[0]-0.5, self.my_GraphData.ag_coord[1]+0.5, self.my_GraphData.ag_coord[1]-0.5, color='#F0E6E6')
        else:
            Graph.box_in_position(self.my_GraphData.ag_coord[0]-0.5, self.my_GraphData.ag_coord[1]+0.5, self.my_GraphData.ag_coord[1]-0.5)

    # Agent moves.
    def ag_moves(self):
        self.my_GraphData.ag_coord[1] += 1
        plt.scatter(self.my_GraphData.ag_coord[0], self.my_GraphData.ag_coord[1], color=self.my_GraphData.ag_color)

    # Agent status (whether the box is transporting or not).
    def ag_status(self):
        if self.my_GraphData.ag_box:
            ag_color = 'yellow'
        else:
            ag_color = 'blue'

        if not self.my_GraphData.ag_box:
            self.ag_status(ag_color)
            plt.scatter(self.my_GraphData.ag_coord[0], self.my_GraphDataag_coord[1], color=self.my_GraphData.ag_color)      # Agent
        else:
            plt.scatter(self.my_GraphData.ag_coord[0], self.my_GraphData.ag_coord[1], color=self.my_GraphData.ag_color)

def main():
    my_Graph = Graph()
    my_Graph.draw_graph()

if __name__ == "__main__":
    main()
