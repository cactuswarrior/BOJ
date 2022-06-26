import sys
sys.stdin = open('test.txt', 'r')

N = int(input())
# print(N)
cnt = 0
num = -1

def bt(num, i):
    global cnt
    if i == len(str(num))-1:
        # print(num)
        cnt += 1
        return

    if int(str(num)[i]) <= int(str(num)[i+1]):
        return

    else:
        bt(num, i + 1)

while num <= 9876543210:
    num += 1
    # print(num)
    bt(num, 0)
    if cnt == N:
        print(num)
        break
    # if num = 1000000:
    #     print(-1)1