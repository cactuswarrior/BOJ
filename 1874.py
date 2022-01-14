import sys
sys.stdin = open('1874.txt', 'r')
N = int(sys.stdin.readline())
arr = list(int(input()) for _ in range(N))
rev = list(reversed(arr))
# print(arr)
# print(rev)


answer = []
temp = []
temp_arr = []
stack = []
num_list = list(range(1, N + 1))
k = 0
for i in range(1, len(num_list) + 1):

    if i == rev[k]:
         while len(stack) and k> 0 and stack[-1] != rev[k-1]:
             temp.append(stack.pop())
             answer.append('-')
         stack.append(i)
         k += 1
    elif i < rev[k]:
        stack.append(i)
    answer.append('+')
# print(stack)
# print(temp)
while stack:
    temp.append((stack.pop()))
    answer.append('-')
if temp != arr:
    print('NO')
else:
    for _ in range(len(answer)):
        print(answer[_])



