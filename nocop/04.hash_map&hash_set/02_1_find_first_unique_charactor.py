"""
<초급>
'nownocodeprogram'이라는 문자열이 주어졌을 때 반복되지 않는 알파벳 중 가장 첫번째 알파벳의 idx를 찾는 문제입니다.
문자열에서 포인터를 옮겨가며 key에는 알파벳을, value에는 반복 횟수를 넣어주며 해시맵을 만듭니다.
다시 포인터를 문자열의 가장 처음으로 돌아가 해시맵과 비교하며 해당 알파벳이 한 번만 나왔는지 체크합니다.
포인터가 문자열을 두번 도는 시간복잡도 O(n), 해시테이블이 만들어지는 O(1)의 공잔복잡도가 발생합니다.
"""

def ffuc(str: str) -> str:
    hash_table = {}

    for c in str:
        find = hash_table.get(c)
        if find is None:
            hash_table[c] = 1
            continue

        hash_table[c] +=1
    
    print(hash_table)

    for idx, c in enumerate(str):
        if hash_table[c] == 1:
            return idx
        
    return -1

print(ffuc(str='nonnonocodeprogram'))