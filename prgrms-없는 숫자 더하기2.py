def solution(numbers):
    answer = -1
    res = 0
    for i in range(len(numbers)):
        res += numbers[i]
    if res > 0:
        answer = 45-res
    return answer



numbers = [1,2,3,4,6,7,8,0]

print(solution(numbers))