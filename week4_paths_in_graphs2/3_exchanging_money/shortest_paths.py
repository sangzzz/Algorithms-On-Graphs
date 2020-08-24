# # Uses python3

# import sys
# import queue


# def shortet_paths(adj, cost, s, distance, reachable, shortest):
#     # write your code here
#     pass


# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     n, m = data[0:2]
#     data = data[2:]
#     edges = list(
#         zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
#     data = data[3 * m:]
#     adj = [[] for _ in range(n)]
#     cost = [[] for _ in range(n)]
#     for ((a, b), w) in edges:
#         adj[a - 1].append(b - 1)
#         cost[a - 1].append(w)
#     s = data[0]
#     s -= 1
#     distance = [10**19] * n
#     reachable = [0] * n
#     shortest = [1] * n
#     shortet_paths(adj, cost, s, distance, reachable, shortest)
#     for x in range(n):
#         if reachable[x] == 0:
#             print('*')
#         elif shortest[x] == 0:
#             print('-')
#         else:
#             print(distance[x])


# Uses python3
import sys
import queue

q = queue.Queue()


def negative_cycle(start):
    # write your code here
    global adj, V, E, edges, tot, dist, used
    dist[start] = 0
    # print(edges)
    for _ in range(V-1):
        changed = False
        # print(changed)
        for (a, b, c) in edges:
            if dist[a-1] == tot:
                continue
            if dist[b-1] > dist[a-1]+c:
                dist[b-1] = dist[a-1] + c
                changed = True
        if not changed:
            _ = False
            break
    if _ == False:
        return 0
    cycle = []
    for (a, b, c) in edges:
        if dist[b-1] > dist[a-1] + c:
            cycle.append(b-1)
    # print(cycle)
    q = queue.Queue()
    for i in cycle:
        if not used[i]:
            q.put(i)
            used[i] = True
        while not q.empty():
            item = q.get()
            for i in adj[item]:
                if not used[i]:
                    used[i] = True
                    q.put(i)

    return 0


# def bfs(i, used):
#     global adj
#     if used[i] == True:
#         return True
#     q.put(i)
#     while not q.empty():
#         item = q.get()
#         for j in adj[item]:
#             q.put(j)
#             used[j] = True

#     return used


if __name__ == '__main__':
    global adj, edges, E, V, tot, dist, used
    V, E = map(int, input().split())
    edges = []
    tot = 0
    for _ in range(E):
        edges.append(tuple(map(int, input().split())))
    adj = [[] for _ in range(V)]
    for (a, b, w) in edges:
        adj[a - 1].append(b - 1)
        if w > 0:
            tot += w
    tot += 1
    start = int(input()) - 1
    dist = [tot for _ in range(V)]
    used = [False for _ in range(V)]
    negative_cycle(start)
    for i in range(0, V):
        if dist[i] == tot:
            print('*')
        elif used[i] == True:
            print('-')
        else:
            print(dist[i])
