import sys
sys.stdin = open('1037.txt', 'r')

N = int(input())
arr = list(input().split())
for i in range(len(arr)):
    arr[i] = int(arr[i])
arr.sort()

if len(arr) == 1:
    print(arr[0]*arr[0])
else:
    print(arr[0]*arr[-1])