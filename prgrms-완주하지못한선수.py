def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = ''

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
        else:
            if i == len(completion)-1:
                answer = participant[i+1]
                break
            continue
    return answer


participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

print(solution(participant, completion))