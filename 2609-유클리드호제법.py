import sys
sys.stdin = open('2609.txt', 'r')
M, N = input().split()
M, N = int(M) ,int(N)

arr = [M, N]
PN = 1
while True:
    if M%N:
        M, N = N, M%N
    else:
        mi = N
        break
ma = int((arr[0]*arr[1])/mi)
print(mi)
print(ma)
