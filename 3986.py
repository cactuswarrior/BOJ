import sys
sys.stdin = open("3986.txt", "r")

N = int(input())
cnt = 0
for i in range(N):
    word = input()
    # print(word)
    stack = []
    for j in range(len(word)):
        if stack == []:
            stack.append(word[j])
        elif word[j] != stack[-1]:
            stack.append(word[j])
        else:
            stack.pop(-1)
        # print(stack)
    if stack == []:
        cnt += 1
print(cnt)



