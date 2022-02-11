# 구구단 곰셈표 출력

print('_' * 29)

for i in range(1, 9 + 1):           # 세로 방향
    for j in range(1, 9 + 1):       # 가로 방향
        print(f'{i * j:3}', end='') # j:3은 i * j:3을 3자리로 출력하여 출력물의 간격을 일정하게 만들어줌
    print()

print('_' * 29)