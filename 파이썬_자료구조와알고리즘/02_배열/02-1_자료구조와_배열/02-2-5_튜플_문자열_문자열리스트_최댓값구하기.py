# 배열 원소에서 최댓값 구해서 출력

from max_module import max_of

tuple_value = (4, 7, 5.2, 2, 3.18, 1)
string_value = 'abcdefg'
list_value = ['DTS', 'ABC', 'FALCON']

print(f'{tuple_value}의 최댓값은 {max_of(tuple_value)}입니다.')
print(f'{string_value}의 최댓값은 {max_of(string_value)}입니다.')
print(f'{list_value}의 최댓값은 {max_of(list_value)}입니다.')
print('---------------')
# max(), min()으로도 가능
print(f'{tuple_value}의 최댓값은 {max(tuple_value)}입니다.')
print(f'{string_value}의 최댓값은 {max(string_value)}입니다.')
print(f'{list_value}의 최댓값은 {max(list_value)}입니다.')

print('---------------')

## 보충: 리스트와 튜플

# 따로 생성한 리스트는 모든 원소의 값이 같아도 식별번호가 다름
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]

print('list_1 is list_2:::', list_1 is list_2)
print('---------------')

# 리스트 2개를 선언하여 서로 대입해도 원소 자체는 복사 안됨.(대입에서 복사 되는 것은 값x, 참조하는 곳o)
list1 = [1, 2, 3]
list2 = list1
print('list1 is list2:::', list1 is list2)

list1[0] = 9
print('list1:::', list1, 'list1:::', list2)