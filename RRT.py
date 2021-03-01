import random
import math

"""
This class represents a field of exploration for the rapidly expanding tree
It will contain a field represented as an array of coordinates
The field will be 100x100 units
"""


class Environment:
    def __init__(self, start, end):
        self.field = []
        self.start = start
        self.end = end
        self.visited = []
        for i in range(1, 100):
            for j in range(1, 100):
                self.field.append([i,j])

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end


"""
This class represents the tree data structure that will be used
to implement the rrt. It will be implemented as a graph with and adjaceny matrix
"""


class Tree:
    def __init__(self, start):
        self.graph_dict = {}
        self.root = start

    def addEdge(self, node, neighbor):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbor]
        else:
            self.graph_dict[node].append(neighbor)


class RRT:
    def __init__(self, start, end, step_size):
        self.environment = Environment(start, end)
        self.tree = Tree(start)
        self.step_size = step_size
        self.valid_path = False
        self.path = None

    def get_random_node(self):
        valid = False
        while valid is False:
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            if x != self.environment.start[0] and y != self.environment.start[1]:
                if not self.environment.visited.__contains__([x, y]):
                    self.environment.visited.append([x, y])
                    return [x, y]

    def find_nearest_node(self, node):
        distance = float('inf')
        nearest_node = None
        for visited_node in self.environment.visited:
            new_distance = self.euclidean(node, visited_node)
            if new_distance < distance:
                distance = new_distance
                nearest_node = visited_node
        return nearest_node

    def euclidean(self, node1, node2):
        return math.sqrt(math.pow(node1[0] - node2[1]) + math.pow(node1[1] - node2[1]))

    def get_new_node(self):
        pass

    def dfs(self):
        pass

    def find_path(self):
        pass

    def path_found(self):
        pass

    def print_path(self):
        for point in self.path:
            print(point[0], ", ", point[1])

    def explore(self):
        while self.path_found is False:
            random_node = self.get_random_node()
            self.tree.addEdge(random_node, self.find_nearest_node())
            if self.path_found() is True:
                self.path = self.find_path()
                self.valid_path = True
                self.print_path()
