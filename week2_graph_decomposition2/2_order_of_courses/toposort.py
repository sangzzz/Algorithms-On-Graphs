# Uses python3

import sys
import threading

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)


def dfs(x):
    # write your code
    global order
    used[x] = 1
    for i in adj[x]:
        if used[i] == 0:
            dfs(i)
    # order.insert(0, x)
    # Takes more time because more time is taken to insert at the front of the list than the end.

    order.append(x)


def toposort():
    global used, order
    used = [0] * len(adj)
    order = []
    # write your code here
    for i in range(0, V):
        if used[i] == 0:
            dfs(i)
    # return order

    return order[::-1]


if __name__ == '__main__':
    #     input = sys.stdin.read()
    #     data = list(map(int, input.split()))
    #     n, m = data[0:2]
    #     data = data[2:]
    #     edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    global adj, V, E, edges
    visited = []
    edges = []
    V, E = map(int, input().split())
    adj = [[] for _ in range(V)]
    for i in range(0, E):
        edges.append(tuple(map(int, input().split())))
        adj[edges[-1][0] - 1].append(edges[-1][1] - 1)
    order = toposort()
    for i in range(0, V):
        print(order[i]+1, end=' ')
    print(' ')


threading.Thread(target=main).start()
