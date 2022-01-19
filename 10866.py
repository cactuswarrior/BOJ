import sys
sys.stdin = open('10866.txt', 'r')
from collections import deque
N = int(input())
arr = []
queue = deque()
for i in range(N):
    arr = input().split()
    k = arr[0]
    if k == "push_back":
        queue.append(int(arr[1]))
    elif k == "push_front":
        queue.appendleft(int(arr[1]))
    elif k == 'pop_front':
        if len(queue):
            q = queue.popleft()
            print(q)
        else:
            print(-1)
    elif k == 'pop_back':
        if len(queue):
            q = queue.pop()
            print(q)
        else:
            print(-1)
    elif k == 'size':
        print(len(queue))
    elif k == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)
    elif k == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif k == 'back':
        if len(queue):
            print(queue[-1])
        else:
            print(-1)
