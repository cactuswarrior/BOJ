import sys
sys.stdin = open('test.txt', 'r')

def bt(start, next, value, visited):
    global ans
    if value > ans:
        return

    if len(visited) == N:
        if arr[next][start] != 0:
            # ans 최소값 비교
            ans = min(value + arr[next][start], ans)
            return

    for i in range(N):
        if i not in visited and i != start and arr[next][i] != 0:
            visited.append(i)
            bt(start, i, value + arr[next][i], visited)
            visited.pop()


N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
visited = []
# print(arr)
ans = 7777777
temp = 0
for i in range(N):
    bt(i, i, 0, [i])

print(ans)