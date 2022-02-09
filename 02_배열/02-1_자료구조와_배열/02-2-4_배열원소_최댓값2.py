# 배열 원소에서 최댓값 구해서 출력

import random
from max_module import max_of

print('난수의 최댓값 구합니다')
num = int(input('난수의 갯수 입력..:'))
low = int(input('난수의 최솟값 입력..:'))
high = int(input('난수의 최댓값 입력..:'))
x = [None] * num # 원소 갯수가 num개인 리스트 생성(이렇게 해야 index를 가져서 for문으로 값을 넣기 좋음)

for i in range(num):
    x[i] = random.randint(low, high)

print(f'{x}')
print(f'최댓값은 {max_of(x)} 입니다.')