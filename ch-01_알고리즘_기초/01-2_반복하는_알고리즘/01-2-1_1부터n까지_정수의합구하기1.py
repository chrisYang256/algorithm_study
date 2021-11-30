# 1부터 n까지 정수의 합 구하기1(while)
# n값이 2면 1 + 2, n값이 3이면 1 + 2 + 3

n = int(input('n값을 입력하세요: '))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')