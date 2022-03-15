import sys
sys.stdin = open("2468.txt", "r")
from collections import deque
N = int(input())

# graph = [[0]*(N+1) for _ in range(N+1)]
# 인덱스와 위치를 맞추기 위해 0 추가
graph = [[0]*(N+1)]
visited = list([0]*(N+1) for _ in range(N+1))
for i in range(N):
    arr = [0] + list(map(int, input().split()))
    graph.append(arr)

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
cnt = 0
# print(graph)
# print(visited)

# 수위별로 bfs를 돌려야 하므로 수위도 인자로 넘길 수 있게
def bfs(hight, r, c, graph, visited):
    q = deque()
    q.append((r, c))
    # 내리는 비양에 따라 반복처리해야 해서 방문 처리를 어떻게 해야할지 고민
    visited[r][c] = 1

    while q:
        r, c = q.popleft()
        # 4방향 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 그래프 안이고, 방문하지 않았으며, 수위 보다 높은 지역이면 방문
            if 0 < nr <= N and 0 < nc <= N and not visited[nr][nc]:
                if graph[nr][nc] > hight:
                    q.append((nr, nc))
                    visited[nr][nc] = 1

# 수위별로 그래프 순환해야하므로 3중 반복문
for h in range(0, 101): #아무곳도 잠기지 않는 경우가 있었다,,, 그러므로 수위가 0인 경우도 포함했다
    temp = 0 # temp 위치를 바꿨더니 맞게 풀기 시작했다,,
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] > h and not visited[i][j]:
                bfs(h, i, j, graph, visited)
                temp += 1
    # 그래프 하나 다 돌면 방문 초기화
    visited = list([0]*(N+1) for _ in range(N+1))
    if temp > cnt:
        cnt = temp
    # temp 를 밖에 선언하고 여기서 초기화를 시켰었는데 뭔가 잘못됐었던 것 같다

print(cnt)