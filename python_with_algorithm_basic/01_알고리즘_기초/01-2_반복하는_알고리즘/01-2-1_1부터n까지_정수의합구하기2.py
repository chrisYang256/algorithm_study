# 1부터 n까지 정수의 합 구하기1(for)
# 변수가 1개만 있다면 while문보다 for문을 사용하는 것이 좋음.
# range(n) -> 0 이상 n "미만"인 수를 차례대로 나열
# range(a, b) -> a 이상 b "미만"인 수를 차례대로 나열
# range(a, b, step) -> a 이상 b "미만"인 수를 차례대로 나열

n = int(input('n의 값을 입력하세요: '))

sum = 0
for i in range(1, n + 1):
    print('i:::', i)
    sum += i

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')