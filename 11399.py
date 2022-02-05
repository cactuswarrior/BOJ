import sys
sys.stdin = open('11399.txt', 'r')
N = int(input())
arr = list(input().split())
res = 0
ans = 0
for i in range(len(arr)):
    arr[i] = int(arr[i])
arr.sort()

for i in range(len(arr)):
    res += arr[i]
    ans += res

print(ans)
