# https://velog.io/@kimdukbae/BOJ-14888-%EC%97%B0%EC%82%B0%EC%9E%90-%EB%81%BC%EC%9B%8C%EB%84%A3%EA%B8%B0-Python

import sys
sys.stdin = open('test.txt', 'r')

N = int(input())
num = list(map(int, input().split()))
check = list(map(int, input().split()))
# print(N)
# print(num)
# print(check)
maximum = -99999999999999999
minimum = 9999999999999999

def dfs(depth, total, plus, minus, multi, divide):
    global maximum
    global minimum
    # print(depth)
    if depth == len(num):
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth+1, total+num[depth], plus-1, minus, multi, divide)
    if minus:
        dfs(depth+1, total-num[depth], plus, minus-1, multi, divide)
    if multi:
        dfs(depth+1, total*num[depth], plus, minus, multi-1, divide)
    if divide:
        dfs(depth+1, int(total/num[depth]), plus, minus, multi, divide-1)

dfs(1, num[0], check[0], check[1], check[2], check[3])

print(int(maximum))
print(int(minimum))