class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = []
        self.discovery = 0
        self.finish = 0
        self.color = "black"

    def add_neighbor(self, v):
        nset = set(self.neighbors)
        if v not in nset:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    verices = {}
    time = 0

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors + "  " + str(self.vertices[key].discovery)))

    def _dfs(self, vertex):
        global time
        vertex.color = "red"
        vertex.discovery = time
        time += 1
        for v in vertex.neighbors:
            if self.vertices[v].color = "black":
                self._dfs(self.vertices[v])
        vertex.color = "blue"
        vertex.finish = time
        time += 1

    def dfs(self, vertex):
        global time
        time = 1
        self._dfs(vertex)


g = Graph()

