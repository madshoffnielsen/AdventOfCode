class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def read_input(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            points.append(tuple(map(int, line.strip().split(','))))
    return points

def manhattan_distance(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))

def part1(points):
    n = len(points)
    uf = UnionFind(n)
    
    for i in range(n):
        for j in range(i + 1, n):
            if manhattan_distance(points[i], points[j]) <= 3:
                uf.union(i, j)
    
    constellations = len(set(uf.find(i) for i in range(n)))
    return constellations

if __name__ == "__main__":
    input_file = "2018/Day25/input.txt"
    points = read_input(input_file)
    
    result_part1 = part1(points)
    print(f"Part 1: {result_part1}")