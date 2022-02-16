# 1000이하의 소수 나열하기

counter = 0 # 나눗셈 횟수 카운트

for n in range(2, 1001):
    print(n)
    for i in range(2, n):
        counter += 1
        if n % i == 0: # 나누어 떨어지면 소수 아님
            break      # 더이상 반복이 불필요하면 중단
    else:              # 끝까지 나누어 떨어지지 않으면 다음을 수행
        print(n)
print(f'나눗셈을 실행한 횟수: {counter}')