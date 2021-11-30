# a부터 b까지 정수의 합 구하고 최종값 출력하기1-1
# 여기서 for문 안의 if문은 비추천::: if행이 999번 실행되어도 else행은 단 한 번 실행되므로 else행을 위해 if문이 매우 많이 실행되는 꼴.

a = int(input('정수 a를 입력하세요 :'))
b = int(input('정수 b를 입력하세요 :'))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b + 1):
    if i < b:
        print(f'{i} + ', end='')
    else:
        print(f'{i} = ', end='') # sum에 i를 더함
    sum += i

print(sum)