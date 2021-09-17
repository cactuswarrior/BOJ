# import sys
# sys.stdin = open('4949.txt', 'r')

# N = int(input())
# for _ in range(N):
while True:
    line = input()
    if line != '.':
        line = line.split()
    if line == '.':
        break
    # print(line)
    stack = []
    ans = ''
    for i in line:
        for j in i:
            if j == '(':
                stack.append('(')
            if j == ')':
                if stack:
                    a = stack.pop()
                    if a != '(':
                        ans = 'no'
                        break
                else:
                    ans = 'no'
                    break
            if j == '[':
                stack.append('[')
            if j == ']':
                if stack:
                    a = stack.pop()
                    if a != '[':
                        ans = 'no'
                        break
                else:
                    ans = 'no'
                    break
    if ans == 'no':
        print(ans)
    else:
        if stack:
            print('no')
        else:
            print('yes')
    # print('stack', stack)


