import sys
sys.stdin = open('1260.txt', 'r')

N, M, V = map(int, input().split())

# print(N, M, V)
graph = [[0]*(N+1) for _ in range(N+1)]
arr = []
visited = [0]*(N+1)
path = []
print(graph)

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
print(graph)

def dfs(V, graph):
    arr = []
    print(V)
    print('visited', visited)
    print(path)
    if visited[V] == 0:
        path.append(V)
        visited[V] = 1
    else:
        return
    for i in range(M):
        if graph[V][i] == 1:
            if visited[i] == 0:
                arr.append(i)
    print('arr', arr)
    if arr:
        if len(arr) > 1:
            V = (min(arr))
            arr.pop(V)
        else:
            V = arr.pop()
        dfs(V, graph)
    else:
        return

def bfs(V, graph):
    arr = []
    print(V)
    print('visited', visited)
    print(path)
    if visited[V] == 0:
        path.append(V)
        visited[V] = 1
    else:
        return
    for i in range(M):
        if graph[V][i] == 1:
            if visited[i] == 0:
                arr.append(i)
    print('arr', arr)
    if arr:
        V = arr.pop(0)
        bfs(V, graph)
    else:
        return

dfs(V, graph)
print('path', path)
visited = [0]*(N+1)
arr = []
path = []
print('dfs------------------------')
bfs(V, graph)