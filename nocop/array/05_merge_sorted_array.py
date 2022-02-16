# https://velog.io/@max-sum/algorithm-array-merge-sorted-array

arr1 = [1, 3, 5, 0, 0, 0]
count1 = 3

arr2 = [2, 4, 8]
count2 = 3

def merge_sorted_array(nums1, m, nums2, n):
    reading_idx_1 = m - 1
    reading_idx_2 = n - 1
    writing_idx = len(nums1) - 1

    if reading_idx_2 < 0: # arr2가 빈 배열인 경우
        return

    while 0 <= reading_idx_1 and 0 <= reading_idx_2:
        num1 = nums1[reading_idx_1]
        num2 = nums2[reading_idx_2]

        if num1 >= num2:
            nums1[writing_idx] = num1
            reading_idx_1 -= 1
            writing_idx -= 1
        else:
            nums1[writing_idx] = num2
            reading_idx_2 -= 1
            writing_idx -= 1

    # case:: arr1 = [5, 6, 7, 0, 0, 0] / arr2 = [1, 2, 3]
    while 0 <= reading_idx_2:
        num = nums2[reading_idx_2]
        nums1[writing_idx] = num
        reading_idx_2 -= 1
        writing_idx -= 1

merge_sorted_array(arr1, count1, arr2, count2)
print(arr1)