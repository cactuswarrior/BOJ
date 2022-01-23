import sys
sys.stdin = open('17298.txt', 'r')
input = sys.stdin.readline
N = int(input())
arr = input().split()
arr = [ int(arr[_]) for _ in range(len(arr))]
res = [0]*N
stack = []
print(arr)
for i in range(len(arr)):
    print('i', i)
    if i == len(arr)-1:
        res[i] = -1
    elif i + 1 <= len(arr)-1 and arr[i] < arr[i+1]:
        res[i] = arr[i+1]
        while stack:
            temp = stack.pop()
            if temp[0] < arr[i+1]:
                res[temp[1]] = arr[i+1]
            else:
                stack.append(temp)
                break
    else:
        stack.append((arr[i], i))
    print('arr', arr[i])
    print('stack', stack)
    print('res', res)
if stack:
    while stack:
        temp = stack.pop()
        res[temp[1]] = -1
print('res', res)

print(*res, sep=' ')