import sys
from collections import deque
sys.stdin = open('1260.txt', 'r')

N, M, V = map(int, input().split())

# print(N, M, V)
graph = [[0]*(N+1) for _ in range(N+1)]
arr = []
visited = [0]*(N+1)
path = []
# print(graph)

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
# print(graph)

def dfs(V, graph, visited):
    visited[V] = 1
    print(V, end=' ')
    for i in range(N+1):
        if graph[V][i] == 1:
            if visited[i] == 0:
                dfs(i, graph, visited)
    return

def bfs(V, graph, arr):
    queue = deque()
    queue.append(V)
    visited[V] = 1
    while queue:
        V = queue.popleft()
        print(V, end=' ')

        for i in range(N+1):
            if graph[V][i] == 1:
                if not visited[i]:
                    visited[i] = 1
                    queue.append(i)
dfs(V, graph, visited)
print()
visited = [0]*(N+1)
bfs(V, graph, visited)