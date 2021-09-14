string = input()
alpha = [-1] * 26
for i in range(len(string)):
    idx = ord(string[i])-97
    # print(idx)
    if alpha[idx] == -1:
        alpha[idx] = i

for _ in alpha:
    print(_, end=' ')
