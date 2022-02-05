N = int(input())
k = 1
i = 0
while True:
    if N > k:
        i += 1
        k += (i*6)
    else:
        print(i+1)
        break
