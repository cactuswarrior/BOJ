import sys
sys.stdin = open('7576.txt', 'r')
from collections import deque

M, N = map(int, input().split())
# M은 가로 칸수 N은 세로 칸 수 [N][M]

#토마토가 모두 익을 떄까지 거리는 최소날짜 출력
#단 저장될 때부터 모든 토마토가 익어있는 상태이면 0출력 >> 그래프에 0이 없는 경우
#토마토가 모두 익지는 못하는 상황이면 -1 출력 >> bfs 다 돌았는데 그래프상에 0이 있는 경우 >> 그래프에 0이 있는 경우

graph = []
visited = list([0]*M for _ in range(N))

# 세로 높이만큼 반복 돌면서 그래프 입력(기존에 0을 추가해 인덱스와 위치를 일치시키는 방법을 사용할 수 없음(0이 없는지 탐지해야 하므로))
for i in range(N):
    arr = list(map(int, input().split()))
    graph.append(arr)
temp = 1
if max(map(max, graph)) == 1:
    if min(map(min, graph)) == 1:
        temp = 0


# print(graph)
# print(visited)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]



def bfs(graph, r, c, q):
    q.append((r, c))
    graph[r][c] = 1
    visited[r][c] = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if graph[nr][nc] == -1:
                    continue
                else:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    graph[nr][nc] = graph[r][c] + 1
q = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:

            q.append((i,j))

i, j = q.popleft()
bfs(graph, i, j, q)
ans = max(map(max, graph))-1

#모두 익지 못하는 상황 걸러내기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            ans = -1

if temp == 0:
    ans = 0
print(ans)

