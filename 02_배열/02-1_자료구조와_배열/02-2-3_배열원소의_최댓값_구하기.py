# 시퀸스 원소의 최댓값 출력하기(모듈 가져오기)

from typing import Any, Sequence

from max_module import max_of

print('배열의 최댓값 구합니다.("End"입력하면 종료됨)')

number = 0
x = []

while True:
    value = input(f'배열 x의 [{number}] 값을 입력하세요.:::')
    if value == 'End':
        break
    x.append(int(value))
    number += 1

print(f'배열의 값으로 {number}개를 입력했습니다.')
print(f'최댓값은 {max_of(x)}입니다.')    