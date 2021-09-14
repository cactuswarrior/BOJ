N = int(input())
NUM = []

M = N
ans = 0 # ans 를 선언을 안해줘서 NameError 났다. 파이참에선 문제없었는데 boj에서는 선언이 필요한듯
while M >= (N/2):
    res = 0
    for i in range(len(str(M))):
        res += int(str(M)[int(i)])
    # print(NUM)
    res += M

    # print('M', M)
    # print('res', res)
    if res == N:
        ans = M
        M -= 1
    else:
        M -= 1
print(ans)