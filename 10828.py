import sys
sys.stdin = open('10828.txt', "r")
####### 시간초과 ######## 시간제한 0.5초인 문
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    order = sys.stdin.readline().split()
    # print('order', order)
    if 'push' == order[0]:

        # print(order, num)
        stack.append(order[1])
    elif order[0] == 'pop':
        if stack:
            a = stack.pop()
            print(a)
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])

        else:
            print(-1)