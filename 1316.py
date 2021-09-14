M = int(input())
cnt = 0
for _ in range(M):
    word = input()
    alpha = [0]*26

    for i in range(len(word)):
        idx = ord(word[i])-97
        if alpha[idx] == 0:
            alpha[idx] = 1
        elif word[i-1] != word[i] and alpha[idx] != 0:
            cnt -= 1
            break
    cnt += 1

print(cnt)