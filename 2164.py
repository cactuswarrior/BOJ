import sys
from collections import deque
N = int(input())
card = deque()
# 카드를 순서대로 정렬
for i in range(1, N+1):
    card.append(i)
# 맨위에 카드 버리고 제일 위의 카드를 제일 아래로 보내는 동작
while len(card) > 1:
    card.popleft()
    first = card.popleft()
    card.append(first)
print(card[0])