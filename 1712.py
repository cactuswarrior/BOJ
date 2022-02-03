import sys
sys.stdin = open('1712.txt', 'r')

import math
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
if c <= b:
    print(-1)
elif a/(c-b) < 1:
    print(1)
else:
    print((a//(c-b)) + 1)