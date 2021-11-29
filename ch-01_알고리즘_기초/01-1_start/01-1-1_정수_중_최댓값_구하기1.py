# 3개의 정숫값을 비교하여 최댓값을 구하는 프로그램

print('세 정수 중 최댓값을 구합니다.')

a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 의 값을 입력하세요.: '))

maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c

print(f'최댓값은 {maximum}입니다.')



