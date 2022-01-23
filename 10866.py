import sys
sys.stdin = open('10866.txt', 'r')
input = sys.stdin.readline
from collections import deque
N = int(input())
arr = []
queue = deque()
for i in range(N):
    arr = input().split()
    if arr[0] == "push_back":
        queue.append(int(arr[1]))
    elif arr[0] == "push_front":
        queue.appendleft(int(arr[1]))
    elif arr[0] == 'pop_front':
        if len(queue):
            print(queue.popleft())
        else:
            print(-1)
    elif arr[0] == 'pop_back':
        if len(queue):
            print(queue.pop())
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(queue))
    elif arr[0] == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)
    elif arr[0] == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif arr[0] == 'back':
        if len(queue):
            print(queue[-1])
        else:
            print(-1)

# 시간 단축 1참조: https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-10866%EB%B2%88-%EB%8D%B1-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython