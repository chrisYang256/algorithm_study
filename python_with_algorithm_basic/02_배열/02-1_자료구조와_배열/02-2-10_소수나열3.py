# 1000 이하 소수 나열(알고리즘 개선 2)

counter = 0          # 곱셈과 나눗셈을 합한 횟수
find = 0             # 이미 찾은 소수의 갯수
prime = [None] * 500 # 소수를 저장하는 배열

prime[find] = 2 # 2는 소수
find += 1
prime[find] = 3 # 3도 소수
find += 1

for n in range(5, 1001, 2):  # 홀수만 대상으로 설정
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0: # 나누어 떨어지므로 소수가 아님
            break
        i += 1
    else:                     # 끝까지 나누어 떨어지지 않았다면
        prime[find] = n       # 소수로 배열에 등록
        find += 1
        counter += 1

for i in range(find):         # find의 소수를 출력
    print(prime[i])
print(f'곱셈과 나눗셈 실행 횟수 : {counter}')