# 1 ~ 12까지 8을 건너뛰고 출력하기1
# 조건이 10만이면 if문 연산도 10만이므로 비효율적

for i in range(1, 13):
    if i == 8:
        continue
    print(i, end=' ')