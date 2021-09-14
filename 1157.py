string = input()
alpha = [0]*26
for i in string:
    if ord(i) >= 97:
        idx = ord(i)-97
    else:
        idx = ord(i)-65
    alpha[idx] += 1
max = 0
for i in alpha:
    if i > max:
        max = i
ans = []
for j in alpha:
    if j == max:
        ans.append(j)
        idx = alpha.index(j)

if len(ans) > 1:
    print("?")
else:
    print(chr(idx + 65))
