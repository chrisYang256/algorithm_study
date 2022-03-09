# https://velog.io/@max-sum/algorithm-array-move-zeroes

array = [3, 9, 0, 1, 0, 29, 30]

def move_zero(values):
    zero_location = 0
    for i in range(len(values)):
        if values[i] != 0:
            values[zero_location] = values[i]
            zero_location += 1

    while zero_location < len(values):
        values[zero_location] = 0
        zero_location += 1

    return values

print(move_zero(array))