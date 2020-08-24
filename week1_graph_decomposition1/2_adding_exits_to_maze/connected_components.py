# Uses python3

import sys


def dfs(i):
    visited.append(i)
    for j in adj[i]:
        if j not in visited:
            dfs(j)


def number_of_components(adj):
    result = 0
    # write your code here
    n = len(adj)
    for i in range(0, n):
        x = len(visited)
        if i not in visited:
            dfs(i)
        if len(visited) != x:
            result += 1
        if len(visited) == n:
            break
    return result


if __name__ == '__main__':
    n, m = map(int, input().split())
    # data = list(map(int, input.split()))
    edges = []
    global visited, adj
    visited = []
    for i in range(m):
        edges.append(tuple(map(int, input().split())))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # print(adj)
    print(number_of_components(adj))
