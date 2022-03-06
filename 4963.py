import sys
sys.stdin = open('4963.txt', 'r')
from collections import deque

while True:
    r, c = map(int, input().split())
    if (r, c) == (0, 0):
        break
    graph = []
    for i in range(c):
        arr = list(map(int, input().split()))
        graph.append(arr)
    print(graph)
    # 상하좌우대각선(시계방향 탐색)
    dr = [0, 1,  1,  1,  0,  -1, -1, -1]
    dc = [-1, -1, 0, 1, 1, 1, 0, 0, -1]
    cnt = 0
    def bfs(a, b):
        global cnt
        queue = deque()
        queue.append((a, b))
        graph[a][b] = 0

        while queue:
            a, b = queue.popleft()
            for i in range(8):
                nr = a + dr[i]
                nc = b + dr[i]

                if 0 <= nr < r-1 and 0 <= nc < c-1 and graph[nr][nc] == 1:
                    queue.append((nr, nc))
                    print('i', nr, nc)
                    graph[nr][nc] = 0



    for i in range(r):
        for j in range(c):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
    print('============')











