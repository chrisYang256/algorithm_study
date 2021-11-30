# a부터 b까지 정수의 합 구하고 최종값 출력하기1-2
# for문에서 i와 b의 비교를 하지 않기 때문에 for문 안에 if문을 썼을 때보다 효율이 더 좋음.(판단 횟수 n번에서 0번이 됨)

a = int(input('정수 a를 입력하세요 :'))
b = int(input('정수 b를 입력하세요 :'))

if a > b:
    # a, b = b, a
    c = a
    a = b
    a = c


sum = 0
for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i

print(f'{b} = ', end='')
sum += b

print(sum)