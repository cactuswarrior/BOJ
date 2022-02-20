import sys
sys.stdin = open("17608.txt", "r")

N = int(sys.stdin.readline())

stack = []
hight = 0
cnt = 0
for i in range(N):
    stack.append(int(sys.stdin.readline()))

limit = max(stack)
while stack:
    a = stack.pop()
    if a == limit:
        cnt += 1
        break
    elif hight < a:
        hight = a
        cnt += 1


print(cnt)