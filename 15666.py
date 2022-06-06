import sys
sys.stdin = open('test.txt', 'r')

def bt(depth, ans):
    if depth == N:
        print(" ".join(map(str, ans)))
        return

    for i in range(len(arr)):
        if depth == 0 or ans[-1] <= arr[i]:
            ans.append(arr[i])
            bt(depth+1, ans)
            ans.pop()

M, N = map(int, input().split())
arr = list(set(map(int, input().split())))
arr.sort()
# print(M, N, arr)
ans = []
bt(0, ans)
