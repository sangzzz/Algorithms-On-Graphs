# Uses python3

import sys


def reach(adj, x, y):
    # write your code here
    visited.append(x)
    if x == y:
        return 1
    for i in adj[x]:
        if i not in visited:
            if reach(adj, i, y):
                return 1
    return 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    global visited
    visited = []
    for i in range(m):
        (fr, to) = tuple(map(int, input().split()))
        edges.append((fr, to))
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = map(int, input().split())
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for i in edges:
        adj[i[0] - 1].append(i[1] - 1)
        adj[i[1] - 1].append(i[0] - 1)
    # print(adj)
    print(reach(adj, x, y))
