# Uses python3

import sys


def negative_cycle():
    # write your code here
    global adj, V, E, edges, tot
    dist = [tot for _ in range(V)]
    dist[0] = 0
    # print(edges)
    for _ in range(V-1):
        for (a, b, c) in edges:
            if dist[b-1] > dist[a-1]+c:
                dist[b-1] = dist[a-1] + c
    for (a, b, c) in edges:
        if dist[b-1] > dist[a-1] + c:
            return 1
    return 0


if __name__ == '__main__':
    global adj, edges, E, V, tot
    V, E = map(int, input().split())
    edges = []
    tot = 0
    for _ in range(E):
        edges.append(tuple(map(int, input().split())))
    adj = [[] for _ in range(V)]
    for (a, b, w) in edges:
        adj[a - 1].append(b - 1)
        tot += w
    tot += 1
    print(negative_cycle())
