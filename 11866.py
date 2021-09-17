from collections import deque
# M이 전체 사람수, N이 빠지는 수
M, N = map(int, input().split())

deq = deque()
res = []
for i in range(1, M+1):
    deq.append(i)
cnt = 1
while deq:
    a = deq.popleft()
    if cnt != N:
        deq.append(a)
        cnt += 1
    else:
        res.append(a)
        cnt = 1
print('<', end='')
print(*res, sep=', ', end='')
print('>')