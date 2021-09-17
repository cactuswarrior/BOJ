import sys
from collections import deque
sys.stdin = open('18258.txt', 'r')

N = int(sys.stdin.readline())
queue = deque()
for _ in range(N):

    command = sys.stdin.readline().split()
    # print(command)
    if command[0] == 'push':
        a = command[1]
        queue.append(a)

        # print('q', queue)
    elif command[0] == 'pop':
        if queue:
            a = queue.popleft()
            print(a)
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)