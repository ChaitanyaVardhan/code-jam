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
                self.G[key]["E"] = self.make_key(coords[0], coords[1] + 1)
                self.parent[self.make_key(coords[0], coords[1] + 1)]["E"] = key
            else:
                self.G[key]["E"] = None

            if coords[0] + 1 < self.rows:
                self.G[key]["S"] = self.make_key(coords[0] + 1, coords[1])
                self.parent[self.make_key(coords[0] + 1, coords[1])]["S"] = key
            else:
                self.G[key]["S"]  = None

    def remove_path(self, path, start, end):
        i = hash(start)
        j = 0
        end = hash(end)
        while i != end:
            i = self.G[i].pop(path[j])
            j += 1

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
            self.path.reverse()


class BFS:
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
        level = [v]
        while len(level) > 0:
            next_level = []
            for v in level:
                for key in self.G[v].keys():
                    if self.G[v].get(key):
                        if self.G[v][key] not in self.discovered:
                            self.discovered[self.G[v][key]] = key
                            next_level.append(self.G[v][key])
            level = next_level       

    def find_path(self):
        if self.end in self.discovered:
            self.path.append(self.discovered[self.end])
            walk = self.parent[self.end][self.discovered[self.end]]
            while walk != self.start:
                self.path.append(self.discovered[walk])
                walk = self.parent[walk][self.discovered[walk]]
            self.path.reverse()

            
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        path = input()
        g = Graph(N, N)
        start = (0,0)
        end = (N-1, N-1)
        g.remove_path(path, start, end)
        bfs = BFS(g.G, g.parent, start, end)
        bfs.find_path()
        print("Case #{}: {}".format(str(i+1), ''.join(bfs.path)))

