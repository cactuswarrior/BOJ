import sys
sys.stdin = open('7568.txt', "r")

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
res = []
for i in range(N):
    cnt = N
    for j in range(N):
        if arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
            cnt -= 1
    res.append(cnt)
ans = [0]*N
mini = 100
rank = 1
while rank <= N:

    for i in range(N):
        if mini > res[i]:
            mini = res[i]
    cnt = res.count(mini)
    if cnt > 1:

        for i in range(N):
            if mini == res[i]:
                ans[i] += rank
                res[i] = 100
        rank += cnt
    else:
        for i in range(N):
            if mini == res[i]:
                ans[i] += rank

                res[i] = 100
        rank += 1
    mini = 100
for i in ans:
    print(i, end=' ')