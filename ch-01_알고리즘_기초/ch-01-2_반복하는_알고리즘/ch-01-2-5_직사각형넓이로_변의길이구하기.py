# 가로, 세로의 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기(area의 약수 나열)

area = int(input('직사각형의 넓이를 입력하세요: '))

for i in range(1, area + 1):
    if i * i > area: break      # print(i * i, f'{i}번째') # 1 * 1, 2 * 2...

    if area % i: continue       # area % 1, area % 2... -> 💡 나머지값이 "0이면 False"이므로 continue가 실행되지 않음.(헷갈림..)
    print(f'{i} x {area // i}') # area % i = True인 경우만 출력(i는 짧은 변, area // i는 긴 변)