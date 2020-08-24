# Uses python3

import sys
import queue
q = queue.Queue()


def distance(s, t):
    # write your code here
    global adj, dist, q
    q.put(s)
    dist[s] = 0
    while not q.empty():
        item = q.get()
        for i in adj[item]:
            if dist[i] == V:
                dist[i] = dist[item] + 1
                q.put(i)
                if i == t:
                    return dist[i]
    return -1


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
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
    s, t = map(int, input().split())
    print(distance(s-1, t-1))
