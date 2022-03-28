import sys

sys.stdin = open('17086.txt', 'r')
from collections import deque

N, M = map(int, input().split())

# print(N, M)
graph = []
for i in range(N):
    temp = list(map(int, input().split()))
    graph.append(temp)

# print(graph)
# 8방향 북쪽부터 시계방향
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def bfs(a, b, graph, q):

    q.append((a, b))
    graph[a][b] = 1

    while q:
        r, c = q.popleft()
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                # print(nr, nc)
                if graph[nr][nc] == 0:
                    q.append((nr, nc))
                    if graph[r][c] == 1:
                        graph[nr][nc] = 2
                    else:
                        graph[nr][nc] = graph[r][c] + 1

q = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i, j))

i, j = q.popleft()
bfs(i, j, graph, q)
ans = max(map(max, graph))
# print(graph)
print(ans-1)
