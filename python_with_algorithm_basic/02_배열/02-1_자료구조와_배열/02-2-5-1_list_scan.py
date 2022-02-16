# 리스트의 모든 원소 스캔(원소 수 미리 파악)
from tkinter import N


x = ['jhon', 'george', 'paul', 'ringo']

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')

print('------------------------')


# 리스트의 모든 원소를 enumerate() 함수로 스캔
xx = ['jhon', 'george', 'paul', 'ringo']

for i, name in enumerate(xx):
    print(f'x[{i}] = {name}')

print('------------------------')


# 리스트의 모든 원소를 enumerate() 함수로 스캔(1부터 카운트)
xxx = ['jhon', 'george', 'paul', 'ringo']

for i, name in enumerate(xxx, 1):
    print(f'{i}번째 = {name}')

print('------------------------')


# 리스트의 모든 원소를 스캔하기(인덱스값 사용 않음(이터러블이기 때문에 어차피 순차가 있어서 가능))

xxxx = ['jhon', 'george', 'paul', 'ringo']

for i in xxxx:
    print(i)