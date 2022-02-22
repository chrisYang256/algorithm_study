""" 
문제: [1~n]까지 모든 숫자가 하나씩 들어있는데 1개의 숫자가 추가되어 n+1개의 숫자가 들어있는 배열이 됨.
여기서 추가로 들어간 숫자를 찾는 문제.
[5,4,2,1,3]에 2가 추가되어 [5,4,2,1,3,2]가 되었다면 2를 찾으면 됨.
"""

arr = [1,2,3,4,2]

def find_duplicate_number(nums):
    store = []
    for i in range(len(nums)):
        if nums[i] in store:
            return nums[i]
        else:
            store.append(nums[i]) 

    return -1

print(find_duplicate_number(arr))


# def find_duplicate_number2(nums):
#     for i in range(len(nums)):
#         # print('i',i)
#         if nums[abs(nums[i])] > 0:
#             # print(nums[nums[i]])
#             nums[nums[i]] = -nums[nums[i]]
#         else: 
#             return nums[i]
            
# print(find_duplicate_number2(arr))