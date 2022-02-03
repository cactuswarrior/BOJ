import sys
sys.stdin = open('1712.txt', 'r')

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
i = 1
if a/(c-b) <= 0:
    print(-1)
else:
    print(round(a/(c-b) + 1))
