# *을 n개 출력하면서 w개마다 줄바꿈하기2
# 3-2에서 for문을 제거하고 // 연산자를 사용하여 연산횟수를 줄임.

n = int(input('몇 개의 *을 출력할까요: '))
w = int(input('몇 개마다 줄바꿈을 할까요?: '))

for _ in range(n // w): # n // w 만큼 반복
    print('*' * w)

rest = n % w # for문에서 나눈 나머지가 있으면 rest에 저장(예: n = 14, w = 5인 경우 *이 4개 저장됨)

if rest:
    print('*' * rest)

print(n // w)