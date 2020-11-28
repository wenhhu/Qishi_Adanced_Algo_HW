import numpy as np

class DSU:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}

    def make_set(self, v):
        self.parent[v] = v

    def find_set(self, v):
        if v == self.parent[v]:
            return v
        return self.find_set(self.parent[v])

    def union_set(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
            self.parent[a] = b

    def add_edge(self, a, b):
        self.parent[self.find_set(b)] = self.find_set(a)
        self.parent[b] = a

    def remove_edge(self, a, b):
        if self.parent[a] == b:
            self.parent[a] = a
        elif self.parent[b] == a:
            self.parent[b] = b


def Kruskal(edges, n, r, e=None):
    dsu = DSU(n)
    res, count = 0, 0
    if e is not None:
        dsu.add_edge(e[0], e[1])
        res, count = e[2], 1
    edges = sorted(edges, key=lambda x: x[2])
    for e in edges:
        if dsu.find_set(e[0]) == dsu.find_set(e[1]):
            continue
        dsu.add_edge(e[0], e[1])
        res += e[2]
        count += 1
    return (count == n - 1) and (res == r), res


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        dsu = DSU(n)
        _, r = Kruskal(edges, n, None)
        res = [[], []]
        for e in range(len(edges)):
            flag1, _ = Kruskal(edges[:e] + edges[e + 1:], n, r)
            flag2, _ = Kruskal(edges[:e] + edges[e + 1:], n, r, edges[e])
            if flag1 and flag2:
                res[1].append(e)
            elif ~flag1 and flag2:
                res[0].append(e)
        return res


