import sys
sys.stdin = open("1325.txt", "r")
# 메모리 초과
# ㄹㅣ드라인과 인접리스트로 다시 풀어보기
N, M = map(int, input().split())
# print(N, M)

graph = [[0]*(N+1) for _ in range(N+1)]
# print(graph)

for i in range(M):
    a, b = map(int, input().split())
    # print(a, b)
    graph[b][a] = 1

# print(graph)
cnt = 0
def dfs(a, graph):
    global cnt
    cnt += 1
    for i in range(N):
        if graph[a][i] == 1:
            dfs(i, graph)


# 한번 거친 곳은 안거치게 해야 할듯

res = []
for i in range(1, N+1):
    dfs(i, graph)
    res.append(cnt)
    cnt = 0
print(res)
m_res = max(res)
print(m_res)
ans = []
for i in range(len(res)):
    if res[i] == m_res:
       ans.append(i+1)
print(*ans)