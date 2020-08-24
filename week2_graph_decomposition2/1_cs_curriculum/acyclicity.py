# Uses python3

import sys
import heapq

clock = 1


def predfs(i):
    global clock
    pre[i] = clock
    clock += 1


def postdfs(i):
    global clock
    post[i] = clock
    clock += 1


def modified_dfs(i):
    # print(pre, post)
    visited.append(i)
    predfs(i)
    for j in rev[i]:
        if j not in visited:
            modified_dfs(j)
    postdfs(i)


def acyclic():
    global visited
    for i in range(0, V):
        if i not in visited:
            modified_dfs(i)
    postorder = []

    visited = []
    for i in range(0, V):
        heapq.heappush(postorder, (-post[i], i))
    for i in range(V):
        _, index = heapq.heappop(postorder)
        # print(_, index)
        visited.append(index)
        for i in adj[index]:
            if i not in visited:
                return 1
    return 0


def main():
    global adj, rev, visited, V, E, clock,  pre, post
    # cloc
    V, E = map(int, input().split())
    edges = []
    for i in range(0, E):
        edges.append(tuple(map(int, input().split())))

    visited = []
    adj = [[] for _ in range(V)]
    rev = [[] for _ in range(V)]
    pre = [0 for _ in range(V)]
    post = [0 for _ in range(V)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        rev[b - 1].append(a - 1)
    print(acyclic())


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    main()
