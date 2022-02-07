import sys
sys.stdin = open("3036.txt", "r")

N = int(input())
arr = input().split()
for _ in range(len(arr)):
    arr[_] = int(arr[_])
std = arr[0]
arr2 = arr[:]
GCD = []
ans = [[0, 0] for _ in range(len(arr)-1)]
# print(ans)
#최대공약수 구하기
for i in range(1, len(arr)):
    # print('first', arr[0], arr[i])
    if arr[i] == 1:
        GCD.append(1)
    else:
        while arr[i] > 1:
            arr[0], arr[i] = arr[i], arr[0] % arr[i]
        GCD.append(arr[0])
    arr[0] = std
# print(GCD)
#기약분수 만들기
arr = arr2
# print('arr', arr)
for i in range(1, len(arr)):
    # print(i, GCD)
    while True:
        # print(arr[0], GCD[i-1])
        arr[0] /= GCD[i-1]
        if arr[0]%GCD[i-1] <= GCD[i-1]:
            ans[i-1][0] = int(arr[0])
            # print(ans)
            break
    arr[0] = std
# print('------------------')
for i in range(1, len(arr)):
    # print(i, GCD)
    while True:
        # print(arr[i], GCD[i-1])
        arr[i] /= GCD[i-1]
        if arr[i]%GCD[i-1] <= GCD[i-1]:
            ans[i-1][1] = int(arr[i])
            # print(ans)
            break

for i in range(len(ans)):
    a, b = ans[i][0], ans[i][1]
    print(f'{a}/{b}')

