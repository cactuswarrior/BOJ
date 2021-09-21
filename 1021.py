# import sys
from collections import deque
# sys.stdin = open('1021.txt')
N, M = map(int, input().split())
num_list = list(map(int, input().split()))

# print(N, M)
# print(num_list)
arr = deque()
# 큐 만들기
for _ in range(1, N + 1):
    arr.append(_)
# print(arr)

cnt = 0
for i in range(M):
    num = num_list[i]
    # 뽑으려는 숫자가 남은 큐 절반보다 앞에 있을 경우
    if arr.index(num) <= len(arr)/2:
        while True:
            if arr[0] == num:
                arr.popleft()
                break
            else:
                a = arr.popleft()
                arr.append(a)
                cnt += 1
    else:
        while True:
            if arr[0] == num:
                arr.popleft()
                break
            else:
                a = arr.pop()
                arr.appendleft(a)
                cnt += 1
print(cnt)


