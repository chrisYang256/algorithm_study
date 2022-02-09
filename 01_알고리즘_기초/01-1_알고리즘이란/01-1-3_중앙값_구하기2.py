# 3개 정수를 받아 중앙값 구하기2 
# 5번째 줄에서 조건에 걸리지 않는다면 7번째 줄에서 a와 b의 동일한 내용의 비교 반복이 있으므로 1보다 비효율적입니다.

def med3(a, b, c):
    if (a <= b and a >= c) or (a >= b and a <= c):
        return a
    elif (a < b and b < c) or (a > b and b > c):
        return b
    return c

print('세 정수의 중앙 값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요: '))
b = int(input('정수 b의 값을 입력하세요: '))
c = int(input('정수 c의 값을 입력하세요: '))

print(f'중앙값은 {med3(a, b, c)}입니다!')