def solution(lottos, win_nums):
    answer = []
    cnt = 0
    lottos.sort(reverse=False)
    win_nums.sort(reverse=False)
    zero_cnt = 0
    max_cnt = 0
    min_cnt = 0
    # 0이 아닌 번호중에서 당첨된 번호가 있는지 확인
    for i in range(len(lottos)):
        if lottos[i] == 0:
            zero_cnt = i + 1
            continue
        else:

            for j in range(len(win_nums)):
                if lottos[i] == win_nums[j]:
                    # 당첨된 번호의 갯
                    cnt += 1
    # 최대 당첨 가능 개수
    max_cnt = cnt + zero_cnt
    min_cnt = cnt
    balls = [max_cnt, min_cnt]

    # 당첨된 숫자의 최고 순위
    for i in range(len(balls)):
        if balls[i] == 6:
            answer.append(1)
        elif balls[i] == 5:
            answer.append(2)
        elif balls[i] == 4:
            answer.append(3)
        elif balls[i] == 3:
            answer.append(4)
        elif balls[i] == 2:
            answer.append(5)
        else:
            answer.append(6)


    return answer


lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]

print(solution(lottos, win_nums))