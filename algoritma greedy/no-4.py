# Nama: [Raka Restu Saputra]
# NIM: [247006111172]

class KruskalMST:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def solve(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        
        return result

g = KruskalMST(5)
g.add_edge(0, 1, 4)  # A-B
g.add_edge(0, 2, 2)  # A-C
g.add_edge(1, 2, 1)  # B-C
g.add_edge(1, 3, 5)  # B-D
g.add_edge(2, 3, 8)  # C-D
g.add_edge(2, 4, 10) # C-E
g.add_edge(3, 4, 2)  # D-E

mst = g.solve()
print("Sisi dalam MST:")
total = 0
names = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E'}
for u, v, w in mst:
    print(f"{names[u]} - {names[v]} : {w}")
    total += w
print(f"Total Bobot MST: {total}")