import sys
from collections import deque
sys.stdin = open('5430.txt', 'r')
queue = deque()
N = int(input())
for i in range(N):
    func = input()
    leng = int(input())
    arr = input()
    # print(arr)
    arr = arr[1:-1]
    arr = arr.split(',')
    if leng != 0:
        arr = deque(int(arr[i]) for i in range(len(arr)))
    else:
        arr = []
    # print(func)
    # print(leng)
    print('arr', arr)

    cnt = 0
    err = False
    for j in range(len(func)):
        if func[j] == 'R':
            cnt += 1
        else:
            if cnt%2:
                if arr:
                    arr.pop()
                else:
                    print('error')
                    err = True
                    break
            else:
                if arr:
                    arr.popleft()
                else:
                    print('error')
                    err = True
                    break

    if cnt%2 == 1:
        arr.reverse()
    if err == False:
        arr = list(arr)
        print(arr)