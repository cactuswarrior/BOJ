import sys
import math
sys.stdin = open('1331.txt', 'r')

arr = []
dx = [-2, -2, -1, +1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]
alpha = ['A', 'B', 'C', 'D', 'E', 'F']
num = ['1', '2', '3', '4', '5', '6']
ans = True
res = False
visit = [[0]*6 for _ in range(6)]
for _ in range(36):
    arr.append(input())
print(arr)

for i in range(36):
    x = alpha.index(arr[i][0])
    y = num.index((arr[i][1]))
    if i == 0:
        visit[x][y] = 1
        continue
    # 이미 방문한 적이 있는 경우
    if i != 0 and visit[x][y] == 1:
        ans = False
        break
    for _ in range(8):
        nx = x + dx[_]
        ny = y + dy[_]
        if nx >= 0 and  nx< 6 and ny >= 0 and ny< 6:
            if alpha[nx] + num[ny] == arr[i-1]:
                x = nx
                y = ny
                visit[x][y] = 1
                res = True
                break
    # 다음 경로가 적절치 못한 경우
    if res == False:
        ans = False
        break
if ans == True:
    print('Valid')

else:
    print('Invalid')



