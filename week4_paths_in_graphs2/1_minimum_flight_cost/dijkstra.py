# Uses python3

import sys
import queue
import heapq
# q = queue.PriorityQueue()
q = []


def distance(s, t):
    # write your code here
    global adj, cost, V, tot, q
    # tot is the total sum of all the edge lengths. No path can have a greater value, so it serves as infinity here...
    dist = [tot for _ in range(V)]
    dist[s] = 0
    heapq.heappush(q, (0, s))
    while len(q) > 0:
        distance, index = heapq.heappop(q)
        if index == t:
            return dist[index]
        for i in range(len(adj[index])):
            if distance + cost[index][i] < dist[adj[index][i]]:
                dist[adj[index][i]] = distance + cost[index][i]
                heapq.heappush(q, (dist[adj[index][i]], adj[index][i]))

    return -1


if __name__ == '__main__':
    global adj, edges, E, V, cost, tot
    V, E = map(int, input().split())
    edges = []
    tot = 0
    for _ in range(E):
        edges.append(tuple(map(int, input().split())))
    adj = [[] for _ in range(V)]
    cost = [[] for _ in range(V)]
    for (a, b, w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
        tot += w
    tot += 1
    s, t = map(int, input().split())
    s, t = s-1, t-1
    print(distance(s, t))
