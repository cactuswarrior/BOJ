import sys
sys.stdin = open('1966.txt', 'r')
from collections import deque

TC = int(input())
for _ in range(TC):
    l, num = map(int, input().split())
    idx = [0]*l
    idx[num] = 1
    doc = deque(map(int, input().split()))
    cnt = 1
    while True:

        if doc[0] == max(doc) and idx[0] == 1:
            print(cnt)
            break
        elif doc[0] == max(doc):
            doc.popleft()
            idx.pop(0)
            cnt += 1
        else:
            a = doc.popleft()
            doc.append(a)
            b = idx.pop(0)
            idx.append(b)
