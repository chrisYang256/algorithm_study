# 1 ~ 12까지 8을 건너뛰고 출력하기2
# 리스트에 8을 뺀다는 단순한 내용.. 
# list에 range()함수를 넣을 수 있고 list끼리 +가 된다는 점만 가져가자.(8은 range()함수의 두번 째 인자가 "미만"이기 때문에 안나옴. )

for i in list(range(1, 8)) + list(range(9, 12 + 1)):
    print(i, end=' ')