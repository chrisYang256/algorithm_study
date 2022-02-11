# 1000 이하의 소수 나열(알고리즘 개선)

counter = 0          # 나눗셈 횟수 카운트
find = 0             # 이미 찾은 소수 갯수
prime = [None] * 500 # 소수 저장하는 배열

prime[find] = 2 # 2는 소수이므로 초기값으로 지정
find += 1

for n in range(3, 1001, 2):     # 홀수만 대상으로 설정
    for i in range(1, find):    # 이미 찾은 소수로 나눔
        counter += 1
        if n % prime[i] == 0:   # 나누어 떨어지면 소수가 아님
            break               # 반복 중단
    else:                       # 끝까지 나누어 떨어지지 않았다면
        prime[find] = n         # 소수로 배열에 등록
        find += 1

for i in range(find):           # find의 소수를 출력
    print(prime[i])
print(f'나눗셈 실행 횟수: {counter}')