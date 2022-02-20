import sys

sys.stdin = open("2304.txt", "r")
input = sys.stdin.readline
N = int(input())

last = 0
first = 1000
arr = [0]*1001
for _ in range(N):
    a, b = input().split()
    a, b = int(a), int(b)
    if last < a:
        last = a
    if first > a:
        first = a
    arr[a] += b

arr = arr[first:last+1]
print(arr)
hight = arr[0]
stack = []
res = []



print(sum(res))