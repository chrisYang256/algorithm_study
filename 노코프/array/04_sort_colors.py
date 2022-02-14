nums = [1, 0, 2, 2, 0, 1, 2, 1, 0]

def sort_colors(arr):
    a_pointer = 0
    b_pointer = len(arr) - 1
    c_pointer = 0

    while c_pointer <= b_pointer:
        print('check loop_top:::', 'arr:', arr, '/', 'c_pointer:', c_pointer)
        if arr[c_pointer] == 0:
            arr[a_pointer], arr[c_pointer] = arr[c_pointer], arr[a_pointer]
            a_pointer += 1
            c_pointer += 1
        elif arr[c_pointer] == 2:
            arr[c_pointer], arr[b_pointer] = arr[b_pointer], arr[c_pointer]
            b_pointer -= 1
        else: # arr[c_pointer] == 1
            c_pointer += 1
        print('check loop_bot:::', 'arr:', arr, '/', 'c_pointer:', c_pointer)

print(sort_colors(nums))
print(f'result: {nums}')