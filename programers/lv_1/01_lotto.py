"""
문제: 로또의 최고 순위와 최저 순위
목표: TC O(n)
채점 결과 = {
정확성: 100.0
합계: 100.0 / 100.0
}
"""

def solution(lottos, win_nums):
    answer = []

    hit_count = 0
    zero_count = 0
    
    pivot = 0
    win_idx = 0
    while pivot < len(lottos):
        if lottos[pivot] == 0:
            zero_count +=1
            win_idx = 0
            pivot +=1
        elif lottos[pivot] == win_nums[win_idx]:
            hit_count +=1
            win_idx = 0
            pivot +=1
            # print(hit_count)
        else:
            win_idx +=1

        if win_idx == len(win_nums):
            win_idx = 0
            pivot +=1
          # print(pivot, win_idx)
          # print(hit_count)
            
    if hit_count == 0 and zero_count == 0:
        answer = [6, 6]
    elif hit_count == 0:
        answer.append(7 - zero_count)
        answer.append(6)
    elif hit_count == 6:
        answer = [1, 1]
    else:
        answer.append(7 - (hit_count+zero_count))
        answer.append(7 - hit_count)
        
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
print(solution([0, 0, 0, 0, 0, 9],	[20, 2, 3, 45, 4, 9]))