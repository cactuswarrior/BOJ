import sys
sys.stdin = open('9012.txt', 'r')

tc = int(input())
# print(tc)

for _ in range(tc):
    # print(_)
    bra = input()
    # print('bra', bra)
    stack = []
    for i in bra:
        if i == '(':
            stack.append('(')
            # print(stack)
        else:
            if i == ')' and len(stack) == 0:
                stack.append('NO')
                break
            else:
                stack.pop()
                # print(stack)
    if len(stack):
        print('NO')
    else:
        print('YES')
