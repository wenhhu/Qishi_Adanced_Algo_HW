# Leetcode 743
class Problem1:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        D = [-1 for i in range(N)]
        D[K - 1] = 0

        for i in range(N):
            for j in times:
                if D[j[0] - 1] != -1:
                    if (D[j[1] - 1] == -1) or (D[j[1] - 1] > D[j[0] - 1] + j[2]):
                        D[j[1] - 1] = D[j[0] - 1] + j[2]

        return max(D) if -1 not in D else -1

# Leetcode 787
# sol1
class Problem2_Sol1:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        D1, D2 = [-1]*n, [-1]*n
        D1[src], D2[src] = 0, 0
        for k in range(K+1):
            for i in range(n):
                for j in flights:
                    if D2[j[0]] != -1:
                        if D1[j[1]] == -1 or (D1[j[1]]>D2[j[0]]+j[2]):
                            D1[j[1]] = D2[j[0]]+j[2]
            D2 = D1.copy()
        return D1[dst]

#sol 2
import heapq

class Problem2_Sol2:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        queue = [(0, 0, src)]
        graph = {}
        D = [-1] * n
        D[src] = 0
        for i in flights:
            if i[0] not in graph:
                graph[i[0]] = {i[1]: i[2]}
            else:
                graph[i[0]][i[1]] = i[2]

        while len(queue):
            cur = heapq.heappop(queue)
            if cur[2] == dst:
                return cur[0]
            if cur[2] in graph:
                for k in graph[cur[2]]:
                    if cur[1] >= K + 1:
                        continue
                    else:
                        heapq.heappush(queue, (cur[0] + graph[cur[2]][k], cur[1] + 1, k))

        return -1