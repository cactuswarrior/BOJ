# 각 수를 3으로 나눈 몫으로 (3,6,9는 몫에서 1일 빼서) 같은 가로 라인끼리 층을 나눴다. 그런데 두 손가락 중에 한 손가락이 2580라인에 있다면 라인은 다르지만 거리는 같아질 수 있는 상황이 된다
def solution(numbers, hand):
    answer = ''
    pos_r = 10
    pos_l = 10
    for i in range(len(numbers)):
        if numbers[i] in [1,4,7]:
            pos_l = numbers[i]
            answer += 'L'
        elif numbers[i] in [3,6,9]:
            pos_r = numbers[i]
            answer += 'R'
        elif numbers[i] in [2,5,8]:
            temp_l = (pos_l)//3
            temp_r = (pos_r)//3
            if pos_r in [3, 6, 9]:
                temp_r -= 1
            temp_i = (numbers[i])//3
            # 왼손이 더 가까운 경우
            if abs(temp_l-temp_i) < abs(temp_r-temp_i):

                pos_l = numbers[i]
                answer += 'L'
            # 오른손이 더 가까운 경우
            elif abs(temp_l-temp_i) > abs(temp_r-temp_i):
                pos_r = numbers[i]
                answer += 'R'
            # 거리가 같은 경우
            else:
                if hand[0] == 'right':
                    pos_r = numbers[i]
                    answer += 'R'
                else:
                    pos_l = numbers[i]
                    answer += 'L'
        # 0인 경우
        else:
            temp_l = pos_l // 3
            temp_r = pos_r // 3
            # 왼손이 더 가까운 경우(가까울 수록 몫이 크)
            if temp_l > temp_r:
                pos_l = numbers[i]
                answer += 'L'
            elif temp_r > temp_l:
                pos_r = numbers[i]
                answer += 'R'
            else:
                if hand == 'right':
                    pos_r = numbers[i]
                    answer += 'R'
                else:
                    pos_l = numbers[i]
                    answer += 'L'





    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

print(solution(numbers, hand))