# 뮤터블 시퀸스 원소를 역순으로 정렬하기

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    """뮤터블 시퀸스 a의 원소를 역순으로 정렬"""
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]

if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    get_int = int(input('원소 수를 입력하세요.: '))
    value = [None] * get_int

    for i in range(get_int):
        value[i] = int(input(f'x[{i}]값을 입력하세요.: '))

    reverse_array(value)

    print('배열의 원소를 역순으로 정렬하였습니다.')
    for i in range(get_int):
        print(f'value[{i}] = {value[i]}')



print('------------------------')

# 배열 원소 역순 정렬 알고리즘
v = ['jhon', 'george', 'paul', 'ringo']

for i in range(len(v) // 2): # 교차는 배열 길이의 절반만큼 이루어짐
    v[i], v[len(v) - i - 1] = v[len(v) - i - 1], v[i] # 1번째, 2번째 값을 서로 대입(교환)한다는 의미

print('v:::', v)


print('------------------------')

# 역순 정렬 표준 라이브러리
vv = ['jhon', 'george', 'paul', 'ringo']
vv.reverse()
print('vv:::', vv)


vvv = ['jhon', 'george', 'paul', 'ringo']
yyy = list(reversed(vvv))
print('vvv:::', yyy)
