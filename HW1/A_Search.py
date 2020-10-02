import numpy as np
import heapq
import itertools

def reconstructPath(cameFrom, cur):
    # function to recontruct path of ASearch
    res = [cur]
    while cur in cameFrom:
        cur = cameFrom[cur]
        res.insert(0, cur)
    return '->'.join(res)


def ASearch(graph, start, end, h):
    # ASearch algorithm
    openHeap = [[0, start]]
    openSet = set([start])
    heapq.heapify(openHeap)

    gScore = {i:np.inf for i in graph}
    gScore[start] = 0

    fScore = {i: np.inf for i in graph}
    fScore[start] = 0

    cameFrom = {}

    while len(openSet):
        # Pop out the root of heap
        while True:
            curScore, cur = heapq.heappop(openHeap)
            if cur in openSet:
                break
        openSet.remove(cur)
        # Check if target arrived
        if cur == end:
            return curScore, reconstructPath(cameFrom, end)

        for i in graph[cur]:
            tentativeGScore = gScore[cur]+graph[cur][i]
            if tentativeGScore < gScore[i]:
                cameFrom[i] = cur
                gScore[i] = tentativeGScore
                fScore[i] = gScore[i]+h(i)
                heapq.heappush(openHeap, [fScore[i], i])
                if i not in openSet:
                    openSet.add(i)

    return -1, reconstructPath(cameFrom, end)

graph = {
    'A':{'B':6, 'F':3},
    'B':{'A':6, 'C':3, 'D':2},
    'C':{'B':3, 'D':1, 'E':5},
    'D':{'B':2, 'C':1, 'E':8},
    'E':{'C':5, 'D':8, 'J':5, 'I':5},
    'F':{'A':3, 'G':1, 'H':7},
    'G':{'F':1, 'I':3},
    'H':{'F':7, 'I':2},
    'I':{'E':5, 'J':3, 'G':3, 'H':2},
    'J':{'E':5, 'I':3}
}

if __name__ == '__main__':
    testH = lambda x:0
    node = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    for start, end in itertools.product(node, node):
        if start != end:
            distance, path = ASearch(graph, start, end, testH)

            print(distance)
            print(path)