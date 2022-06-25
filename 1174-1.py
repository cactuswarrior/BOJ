# 조합으로 풀기
# https://deok2kim.tistory.com/322
import sys

sys.stdin = open('test.txt', 'r')
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
N = int(input())
res = []
# arr에서 i개의 정수를 뽑아서 조합
temp = 0
def bt(temp):
    res.append(int(temp))
    for i in range(10):
        if int(temp[-1]) > i:
            temp += (str(i))
            bt(str(temp))
            temp = temp[:-1]


if N > 1023:
    print(-1)
else:
    for j in range(10):
        bt(str(j))
    print(sorted(res)[N-1])




