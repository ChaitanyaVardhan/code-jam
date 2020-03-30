class Graph:
    def __init__(self, R, C):
        self.rows = R
        self.columns = C
        self.G = {}
        self.hash_dict = {}
        self.parent = {}
        self.add_vertices()
        self.add_edges()

    def add_vertices(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.G[self.make_key(i, j)] = {}
                self.parent[self.make_key(i, j)] = {}

    def add_edges(self):
        for key in self.G.keys():
            coords = self.get_coord(key)
            if coords[1] + 1 < self.columns:
                self.G[key]["W"] = self.make_key(coords[0], coords[1] + 1)
                self.parent[self.make_key(coords[0], coords[1] + 1)]["W"] = key
            else:
                self.G[key]["W"] = None

            if coords[0] + 1 < self.rows:
                self.G[key]["S"] = self.make_key(coords[0] + 1, coords[1])
                self.parent[self.make_key(coords[0] + 1, coords[1])]["S"] = key
            else:
                self.G[key]["S"]  = None

    def make_key(self, i, j):
        k = hash((i, j))
        if not self.hash_dict.get(k):
            self.hash_dict[k] = (i, j)
        return k

    def get_coord(self, k):
        return self.hash_dict.get(k, "Key not Found")


class DFS:
    def __init__(self, G, parent, start, end):
        self.G = G
        self.parent = parent
        self.start = hash(start)
        self.end = hash(end)
        self.discovered = {}
        self.discovered[self.start] = None
        self.path = []
        self.run(self.start)

    def run(self, v):
        for key in self.G[v].keys():
            if self.G[v].get(key):
                if self.G[v][key] not in self.discovered:
                    self.discovered[self.G[v][key]] = key
                    self.run(self.G[v][key])

    def find_path(self):
        if self.end in self.discovered:
            self.path.append(self.discovered[self.end])
            walk = self.parent[self.end][self.discovered[self.end]]
            while walk != self.start:
                self.path.append(self.discovered[walk])
                walk = self.parent[walk][self.discovered[walk]]
                
    
if __name__ == "__main__":
    g = Graph(100, 100)
    print(g.G)
    print(g.parent)
    print(g.G[hash((1,1))])
    start = (0,0)
    end = (99, 99)
    dfs = DFS(g.G, g.parent, start, end)
    print(dfs.discovered)
    dfs.find_path()
    print(dfs.path)

