# https://velog.io/@max-sum/algorithm-array-merge-intervals
# 규칙: 2차원 배열 중 n번째 배열 안에 n+1번째 배열의 값이 포함되면 merge, 아니면 저장

arr = [[8, 16], [1, 5], [10, 15], [3, 7]]

def merge_intervals(values):
    values.sort(key=lambda x:x[0]) # 0번째 index 기준 오름차순 정렬
    # pointer = 0 # 솔팅 구현해봄
    # idx = 1
    # while pointer < len(values):
    #     while idx < len(values):
    #         if values[pointer][0] > values[idx][0]:
    #             values[pointer], values[idx] = values[idx], values[pointer]
    #         idx += 1
    #     pointer += 1
    #     idx = pointer + 1
    # print('values::', values)

    last_idx_0 = values[0][0]
    last_idx_1 = values[0][1]
    merged = []

    for idx_0, idx_1 in values[1:]:
        if last_idx_1 >= idx_0:                 # n번째 배열값에 n+1번째 배열의 0번째 값이 포함되는 경우 merge
            last_idx_1 = max(idx_1, last_idx_1) # index 1 중 가장 큰 값을 저장

        else:
            result = [last_idx_0, last_idx_1]   # n번째 배열값에 n+1번째 배열의 0번째 값이 포함되지 않는 경우 not merge
            merged.append(result)               # 더이상 merge 대상이 아니므로 값 그대로 저장

            last_idx_0 = idx_0                  # n+1번째 배열의 값들이 새로운 기준이 됨
            last_idx_1 = idx_1

    result = [last_idx_0, last_idx_1]           # 최종 값은 비교 대상이 없으므로 저장 후 operation 종료
    merged.append(result)

    return merged

print(merge_intervals(arr))