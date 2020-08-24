# Uses python3
import sys
import math
import heapq


def compute_distance(i, j):
    global points
    x1, y1 = points[i]
    x2, y2 = points[j]
    return math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))


def find(i):
    global parents
    if i != parents[i]:
        parents[i] = find(parents[i])
    return parents[i]


def union(i, j):
    global rank, parents
    i_ind = find(i)
    j_ind = find(j)
    if i_ind != j_ind:
        if rank[i_ind] < rank[j_ind]:
            parents[i_ind] = j_ind
        else:
            parents[j_ind] = i_ind
            if rank[i_ind] == rank[j_ind]:
                rank[i_ind] += 1


def check_num_parents():
    global parents, p
    num_parents = []
    for i in range(p):
        x = find(i)
        if x not in num_parents:
            num_parents.append(x)
    return len(num_parents)


def clustering(k):
    # write your code here
    global p, points, parents, rank
    parents = [i for i in range(0, p)]
    rank = [0 for _ in range(p)]
    q = []
    for i in range(0, p):
        for j in range(i+1, p):
            # q.put((compute_distance(i, j), i, j))
            heapq.heappush(q, (compute_distance(i, j), i, j))
    # print(q)
    d = 0
    while True:
        d, i, j = heapq.heappop(q)
        union(i, j)
        # print(d, i, j)
        # print(parents)
        n = check_num_parents()
        # print(n)
        if n < k:
            break
    return d


if __name__ == '__main__':
    global p, points, distance, parents, rank
    points = []
    parents = []
    rank = []
    p = int(input())
    distance = [None for _ in range(p)]
    for _ in range(p):
        points.append(tuple(map(int, input().split())))
    cluster = int(input())
    print("{0:.9f}".format(clustering(cluster)))
