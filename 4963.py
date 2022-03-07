import sys
sys.stdin = open('4963.txt', 'r')
from collections import deque
# 가로, 세로 잘 보기, dr, dc 잘 주기
while True:
    c, r = map(int, input().split())
    if (c, r) == (0, 0):
        break
    graph = []
    for i in range(r):
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
                nc = b + dc[i]

                if 0 <= nr < r and 0 <= nc < c and graph[nr][nc] == 1:
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











