array = [1, 2, 5, 9, 15, 22, 30]

my_number = int(input('찾으려는 숫자를 입력하세요.: '))

def binary_search(arr, target):
    left = 0
    right = len(arr) -1

    while left <= right:
        pivot = (left+right) // 2

        if arr[pivot] == target:
            return pivot
        elif arr[pivot] < target:
            left = pivot + 1
        else: # arr[pivot] > target
            right = pivot - 1
    
    return -1

print(f'입력한 숫자의 index는 {binary_search(array, my_number)}입니다.')