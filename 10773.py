# 제로
N = int(input())
stack = []
for i in range(N):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
ans = 0
for i in range(len(stack)):
    ans += stack[i]
print(ans)