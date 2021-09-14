
# ###########풀이 참조함#############################################################
N, M = map(int, input().split())
# N은 바닥에 놓인 카드 개수, M은 목표 합

card = list(map(int, input().split()))
# print(card)
res = 0
for i in range(N):
    for j in range(i+1, N):  # range를 i + 1로 설정해야 한다. 위에서부터 하나씩 고정시키고
        for k in range(j + 1, N): # 3개중에 2개 고정했으니 나머지 한자리에 다 끼워 넣어 보는 것
            sum_card = card[i] + card[j] + card[k]
            if sum_card > M:
                continue
            elif sum_card > res and sum_card <= M:
                res = sum_card
print(res)
