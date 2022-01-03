
# 테스트 케이스에서 계속 틀림#############
import sys
import math
sys.stdin = open('1331.txt', 'r')

arr = []
alpha = ['A', 'B', 'C', 'D', 'E', 'F']
num = ['1', '2', '3', '4', '5', '6']
visit = [[0]*6 for _ in range(6)]

ans = True
for _ in range(36):
    arr.append(input())

for i in range(len(arr)):
    a = arr[i][0]
    n = arr[i][1]
    if visit[alpha.index(a)][num.index(n)] == 1:

        ans = False
        break
    if i == 0:

        visit[alpha.index(a)][num.index(n)] = 1
    # 알파벳 두칸 차이나고 숫자가 1칸 차이나면 적절한 경
    elif abs(alpha.index(arr[i][0]) - alpha.index(arr[i-1][0])) == 2:
        if abs(num.index(arr[i][1]) - num.index(arr[i-1][1])) == 1:
            visit[alpha.index(a)][num.index(n)] = 1

    elif abs(alpha.index(arr[i][0]) - alpha.index(arr[i-1][0])) == 1:
        if abs(num.index(arr[i][1]) - num.index(arr[i - 1][1])) == 2:
            visit[alpha.index(a)][num.index(n)] = 1
    else:
        ans = False

        break
for i in range(6):
    for j in range(6):
        if visit[i][j] == 0:
            ans = False
            break
if ans == True:
    print('Valid')

else:
    print('Invalid')

