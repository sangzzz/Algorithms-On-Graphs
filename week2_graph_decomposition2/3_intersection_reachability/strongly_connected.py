# Uses python3

import heapq
import sys

sys.setrecursionlimit(200000)


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
    used[i] = True
    predfs(i)
    for j in rev[i]:
        if not used[j]:
            modified_dfs(j)
    postdfs(i)


def dfs(i):
    used[i] = True
    for _ in adj[i]:
        if not used[_]:
            dfs(_)


def number_of_strongly_connected_components():
    result = 0
    # write your code here

    global used
    for i in range(0, V):
        if not used[i]:
            modified_dfs(i)

    postorder = []
    used = [False for _ in range(V)]
    for i in range(0, V):
        heapq.heappush(postorder, (-post[i], i))

    for i in range(0, V):
        _, index = heapq.heappop(postorder)
        if not used[index]:
            dfs(index)
            result += 1

    return result


def main():
    global adj, rev, used, V, E, clock,  pre, post
    V, E = map(int, input().split())
    edges = []
    for i in range(0, E):
        edges.append(tuple(map(int, input().split())))

    used = [False for _ in range(V)]
    adj = [[] for _ in range(V)]
    rev = [[] for _ in range(V)]
    pre = [0 for _ in range(V)]
    post = [0 for _ in range(V)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        rev[b - 1].append(a - 1)
    print(number_of_strongly_connected_components())


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    main()
