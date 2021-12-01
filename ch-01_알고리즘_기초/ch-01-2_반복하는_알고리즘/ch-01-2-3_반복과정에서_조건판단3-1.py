# *을 n개 출력하면서 w개마다 줄바꿈하기1
# for문 반복마다 if문 실행하므로 효율적이지 않음.

n = int(input('몇 개의 *을 출력할까요: '))
w = int(input('몇 개마다 줄바꿈을 할까요?: '))

for i in range(n):
    print('*', end='')
    if i % w == w - 1:
        print()

if n % w:
    print()
