import drawsvg as draw
import matplotlib.pyplot as plt
import numpy as np
class Visualizer:
    """ network: the INDEX graph, NOT the original
        nodes_array: the original Tuple coordinates
        """
    def __init__(self, network, nodes_array, cycles, detes):
        self.graph = network
        self.nodes = nodes_array
        self.cycles = cycles
        self.detes = detes
        # for sensible display
        all_x_coords = []
        all_y_coords = []
        for node in nodes_array:
            x, y = node
            all_x_coords.append(x)
            all_y_coords.append(y)
        y_maximum = max(all_y_coords)
        self.change = y_maximum
        # set plot size
    def adjust(self, x, y):
        return (x, y * -1 + self.change)
    def plot_node(self):
        index = 0
        for node in self.nodes:
            x, y = node
            x, y = self.adjust(x, y)
            plt.plot(x, y, 'o')
            plt.annotate(index, (x, y), fontsize=36)
            index += 1
    def plot_edge(self):
        counter = 0
        for edge in self.graph.edges():
            u, v = edge
            u = int(u)
            v = int(v)
            x_this_edge = [self.nodes[u][0], self.nodes[v][0]]
            y_this_edge = [self.nodes[u][1], self.nodes[v][1]]
            midpoint_x = np.mean(x_this_edge)
            midpoint_y = np.mean(y_this_edge)
            plt.plot(x_this_edge,
                    [y * -1 + self.change for y in y_this_edge],
                    '-', scalex=10, scaley=10)
            plt.annotate(counter, self.adjust(midpoint_x, midpoint_y))
            counter += 1
    def plot_cycle_edge_all(self, detail_level, detail_type, centroid):
        for i in range(len(self.cycles)):
            if(detail_level == "low"):
                self.plot_cycle_edge(i, detail_type, centroid)
            else:
                self.plot_cycle_edge_detailed(i, detail_type, centroid)    
    def plot_cycle_edge(self, i, setting, centroid):
        # print(f"cycle no. {i}: {cycles[i]}")
        cycle = self.cycles[i]
        x_coords = []
        y_coords = []
        for i in range(len(cycle)):
            u = int(cycle[i])
            u_node = self.nodes[u]
            x_coords.append(u_node[0])
            y_coords.append(u_node[1])
        start = self.nodes[int(cycle[0])]
        centroid_x = np.mean(x_coords)
        centroid_y = np.mean(y_coords)
        x_coords.append(start[0])
        y_coords.append(start[1])
        if(setting == "lines"):
            plt.plot(x_coords, 
                    [y * -1 + self.change for y in y_coords], 
                    '-', scalex=10, scaley=10)
        if(setting == "fill"):
            plt.fill(x_coords, 
                    [y * -1 + self.change for y in y_coords], 
                    )
        if(centroid == True):
            plt.annotate(i, (centroid_x, centroid_y * -1 + self.change))
        return len(x_coords) - 1
    def plot_cycle_edge_detailed(self, c, setting, centroid):
        cycle = self.cycles[c]
        x_coords = []
        y_coords = []
        for i in range(len(cycle)):
            u = cycle[i]
            if(i + 1) > len(cycle) - 1:
                v = cycle[0]
            else:
                v = cycle[i + 1]
            u = int(u)
            v = int(v)
            # starting node (array)
            u_node = list(self.nodes[u])
            v_node = list(self.nodes[v])
            x_coords.append(u_node[0])
            y_coords.append(u_node[1])
            # middle nodes (tuples)
            coordinates = self.graph[u][v]['details'] # <- how the code works
            start = list(coordinates[0]) # <- paths here are 'directed'!
            if(u_node == start):
                pass
            else:
                coordinates.reverse()
            # ditch the start & middle elements of the list!
            intermediary_coordinates = coordinates[1:len(coordinates) - 1]
            for x, y in intermediary_coordinates:
                x_coords.append(x)
                y_coords.append(y)
            # ending node 
            x_coords.append(v_node[0])
            y_coords.append(v_node[1])
            centroid_x = np.mean(x_coords)
            centroid_y = np.mean(y_coords)
        if(setting == "lines"):
            plt.plot(x_coords, 
                    [y * -1 + self.change for y in y_coords], 
                    '-', scalex=10, scaley=10)
        if(setting == "fill"):
            plt.fill(x_coords, 
                    [y * -1 + self.change for y in y_coords], 
                    )
        if(centroid == True):
            plt.annotate(c, (centroid_x, centroid_y * -1 + self.change))
    def draw_edge(self, canvas):
        counter = 0
        for edge in self.graph.edges():
            u, v = edge
            u = int(u)
            v = int(v)
            coords = [self.nodes[u][0], self.nodes[u][1],
                      self.nodes[v][0], self.nodes[v][1]]
            canvas.append(draw.Line(*coords, cw=True, stroke='yellow', stroke_width=1))
            counter += 1
    def draw_cycle_edge_all(self, detail_level, canvas):
        for i in range(len(self.cycles)):
            if(detail_level == "low"):
                self.draw_cycle_edge(i, canvas)
            else:
                self.draw_cycle_edge_detailed(i, canvas) 
    def draw_cycle_edge(self, i, canvas):
        cycle = self.cycles[i]
        x_coords = []
        y_coords = []
        for i in range(len(cycle)):
            u = int(cycle[i])
            u_node = self.nodes[u]
            x_coords.append(u_node[0])
            y_coords.append(u_node[1])
        coords = [a for b in zip(x_coords, y_coords) for a in b]
        canvas.append(draw.Lines(*coords,
                    fill='none', stroke='yellow', close='true'))
    def draw_cycle_edge_detailed(self, c, canvas):
        cycle = self.cycles[c]
        x_coords = []
        y_coords = []
        for i in range(len(cycle)):
            u = cycle[i]
            if(i + 1) > len(cycle) - 1:
                v = cycle[0]
            else:
                v = cycle[i + 1]
            u = int(u)
            v = int(v)
            # starting node (array)
            u_node = list(self.nodes[u])
            x_coords.append(u_node[0])
            y_coords.append(u_node[1])
            # middle nodes (tuples)
            coordinates = self.graph[u][v]['details'] # <- how the code works
            start = list(coordinates[0]) # <- paths here are 'directed'!
            if(u_node == start):
                pass
            else:
                coordinates.reverse()
            # ditch the start & middle elements of the list!
            intermediary_coordinates = coordinates[1:len(coordinates) - 1]
            for x, y in intermediary_coordinates:
                x_coords.append(x)
                y_coords.append(y)
            # ending node SKIP!
        coords = [a for b in zip(x_coords, y_coords) for a in b]
        canvas.append(draw.Lines(*coords,
                   fill='none', stroke='yellow', close='true'))