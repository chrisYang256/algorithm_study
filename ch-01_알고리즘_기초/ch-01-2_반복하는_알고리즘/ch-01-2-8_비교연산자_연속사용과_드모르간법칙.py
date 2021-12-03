# 2자리 양수(10~99) 입력받기
# 드모르간의 법칙: 조건을 부정하고 논리곱을 논리합으로, 논리합을 논리곱으로 바꾸고 다시 전체를 부정하면 원해의 조건과 같다.
# 드모르간의 법칙 예1: x and y와 not(not x or not y)의 논리값은 같다
# 드모르간의 법칙 예2: x or y와 not(not x and not y)의 논리값은 같다

while True:
    no = int(input('두자리 양수를 입력하세요: '))
    # if no >=10 and no <= 99:   # 방법1, 반복을 "계속하기 위한" 조건
    # if 10 <= no <= 99:         # 방법2
    if not (no < 10 or no < 99): # 방법3, 반복을 "멈추기 위한" 조건, 드모르간의 법칙
        break

print(f'입력받은 양수는 {no}입니다.')