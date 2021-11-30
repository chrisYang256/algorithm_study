# 입력값(a, b) 오름차순으로 정렬 후 a부터 b까지 정수 합 구하기

a = int(input('정수 a를 입력하세요: '))
b = int(input('정수 b를 입력하세요: '))

if a > b:
    a, b = b, a # a -> b 오름차순 정렬

sum = 0
for i in range(a, b + 1):
    sum += i

print(f'{a}에서 {b}까지 정수의 합은 {sum}입니다.')