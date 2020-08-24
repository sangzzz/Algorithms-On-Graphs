# Uses python3
import sys
import math
import queue


def compute_distance(i, j):
    global points
    x1, y1 = points[i]
    x2, y2 = points[j]
    return math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))


def minimum_distance():
    result = 0.
    global p, points, distance
    # write your code here
    distance[0] = 0
    q = queue.PriorityQueue()
    q.put((0, 0))
    for i in range(1, p):
        distance[i] = compute_distance(0, i)
        q.put((distance[i], i))

    # (distance, index)
    fixed_points = []
    while len(fixed_points) < p:
        dist, index = q.get()
        if index not in fixed_points:
            result += dist
            fixed_points.append(index)
        # print(fixed_points)
        for i in range(p):
            if i not in fixed_points:
                d = compute_distance(i, index)
                if d < distance[i]:
                    distance[i] = d
                    q.put((d, i))
                    # heapq.heappush(q, (d, i))
    # for i in distance:
    #     result += i
    return result


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # x = data[1::2]
    # y = data[2::2]
    global p, points, distance
    points = []
    edges = []
    p = int(input())
    distance = [None for _ in range(p)]
    for _ in range(p):
        points.append(tuple(map(int, input().split())))
    print("{0:.9f}".format(minimum_distance()))
