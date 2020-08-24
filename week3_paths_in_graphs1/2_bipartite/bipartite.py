# Uses python3

import sys
import queue
q = queue.Queue()


def bfs(i):
    global adj, dist, V
    q.put(i)
    dist[i] = 1
    while not q.empty():
        item = q.get()
        for j in adj[item]:
            if dist[j] == V:
                dist[j] = -dist[item]
                q.put(j)


def bipartite():
    # write your code here
    global adj, dist, V, edges
    for i in range(0, V):
        if dist[i] == V:
            bfs(i)

    for (a, b) in edges:
        if dist[a-1] == dist[b-1]:
            return 0
    return 1


if __name__ == '__main__':
    global adj, V, E, edges, dist
    V, E = map(int, input().split())
    edges = []
    for i in range(E):
        edges.append(tuple(map(int, input().split())))
    adj = [[] for _ in range(V)]
    dist = [V for i in range(V)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite())
