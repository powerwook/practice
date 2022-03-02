def solution(food_times, k):
    answer = 0
    next_num = 0
    n = len(food_times)
    if sum(food_times) <= k:
        return -1
    for i in range(k):
        index = i % n + next_num
        while food_times[index] == 0:
            index += 1
            next_num += 1
        food_times[index] -= 1
        
    index += 1
    answer = index % n + 1


    return answer