import sys
sys.stdin = open('1012.txt', 'r')

T = int(input())
for i in range(T):
    N, M, K = map(int, input().split())
    graph = [[0]*(M) for _ in range(N)]
    # print(graph)
    for _ in range(K):
        a, b = map(int, input().split())
        # print(a, b)
        graph[a][b] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    cnt = 0
    def bfs(graph, a, b):
        q = [(a, b)]
        graph[a][b] = 0
        while q:
            r, c = q.pop(0)

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < N and 0 <= nc < M:
                    if graph[nr][nc] == 1:
                        q.append((nr, nc))
                        graph[nr][nc] = 0


    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                # print(i, j)
                # 인자 값을 제대로 넘겨주자
                bfs(graph, i, j)
                cnt += 1
    print(cnt)