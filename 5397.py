import sys
sys.stdin = open('5397.txt', 'r')

N = int(input())
for _ in range(N):
    pw = input()
    # print(pw)
    stack1 = []
    stack2 = []
    for i in pw:
        # print(i)
        if i == "<":
            if stack1:
                sp1 = stack1.pop()
                stack2.append(sp1)
            else:
                continue
        elif i == ">":
            if stack2:
                sp2 = stack2.pop()
                stack1.append(sp2)
            else:
                continue
        elif i == "-":
            if stack1:
                stack1.pop()
        else:
            stack1.append(i)
    if stack2:
        while stack2:
            sp2 = stack2.pop()
            stack1.append(sp2)
    # print(stack1)
    ans = ''
    for i in stack1:
        ans += i
    print(ans)