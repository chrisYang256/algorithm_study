# 세 정수 중 최댓값 구하기

def max3(a, b, c):
    """a, b, c 중 최댓값 구하여 반환"""
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum

print(f'max3(3, 2, 1) = {max(3, 2, 1)}')
print(f'max3(2, 3, 1) = {max(2, 3, 1)}')
print(f'max3(1, 2, 3) = {max(1, 2, 3)}')
print(f'max3(3, 2, 3) = {max(3, 2, 3)}')