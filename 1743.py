import sys
sys.stdin = open('1743.txt', 'r')
from collections import deque
# N 세로 M 가로 K 쓰레기 갯수
N, M, K = map(int, input().split())
# print(N, M, K)
# 그래프
graph = list([0]*(M+1) for _ in range(N+1))
# 음식물 위치
for a in range(K):
    r, c = map(int, input().split())
    graph[r][c] = 1

# print(graph)

dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]
cnt = 0
temp = 0
def bfs(r, c):
    global cnt
    global temp
    q = deque()
    q.append((r, c))
    graph[r][c] = 0
    temp = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 < nr <= N and 0 < nc <= M and graph[nr][nc] == 1: #나는 그래프 위치와 인덱스를 맞추기 위해 한 줄씩 더하므로 0을 포함하지 않고 N은 포함해야
                q.append((nr, nc))
                graph[nr][nc] = 0
                temp += 1

    if temp > cnt:
        cnt = temp

# 그래프 전체 순회함
for i in range(1, N+1):
    for j in range(1, M+1):
        if graph[i][j] == 1:
            bfs(i, j)
            # print(temp)

print(cnt)

