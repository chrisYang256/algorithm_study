arr = [1, 3, 2, 4, 5, 7, 6]

def find_peak_element(nums):
    left_reading = 0
    right_reading = len(nums) - 1

    if len(nums) <= 1:
        return 0

    while left_reading < right_reading:
        pivot = (left_reading + right_reading) // 2
        num = nums[pivot]
        next_num = nums[pivot + 1]

        if num < next_num:
            left_reading = pivot + 1
        else:
            right_reading = pivot

    return left_reading

print(find_peak_element(arr))