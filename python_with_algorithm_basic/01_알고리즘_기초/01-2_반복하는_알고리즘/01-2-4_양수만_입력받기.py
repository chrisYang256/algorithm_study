# 1부터 n까지 정수의 합 구하기(n값은 양수만 입력)
# while True:와 break의 조합::: 무한루프 생성 / 빠져나오기 패턴

while True:
    n = int(input('n값을 입력하세요: '))
    if n > 0: break # n이 0보다 커질 때 까지 반복
    
sum = 0
i   = 1

for i in range(1, n + 1):
    sum += i
    i += 1

print(f'i부터 {n}까지 정수의 합은 {sum}입니다.')