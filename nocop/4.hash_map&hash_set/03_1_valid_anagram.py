"""
<초급>
두 개의 문자열이 서로 일치하는 경우에만 true를 반환하는 문제입니다.
'nocodeprogram'와 'programcodeno'라는 문자열이 주어졌을 때 
포인터를 이용해 'nocodeprogram'을 읽으며 hash table에 key에는 알파벳을, value에는 갯수를 입력한 후
'programcodeno'를 포인터로 읽으며 해시테이블에 존재하는 알파벳의 갯수를 줄여나가서 모두 0이 되는 경우 true를 반환하면 됩니다.
만약 2나 -3같은 value가 존재하면 invalid한 아나그램이므로 false를 반환합니다.
TC -> O(n), SV -> O(1)이 됩니다.
만약 테이블을 사용하지 않아야 하는 경우 각각의 문자열을 솔팅하고 포인터를 이동하면서 양쪽의 문자열을 비교하면 됩니다.
이 경우 TC -> O(n log n), SC -> O(1)이 됩니다.
"""

# <my solution>
def valid_anagram(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    hash_table = {}
    for c in str1:
        is_there = hash_table.get(c)
        if is_there is None:
            hash_table[c] = 1
            continue
        hash_table[c] += 1

    for c in str2:
        is_there = hash_table.get(c)
        if is_there is None:
            hash_table[c] = 1 # 비교할 필요 없이 return Flase를 하는게 나음
            continue
        hash_table[c] -= 1

    for key, value in hash_table.items():
        if value != 0:
            return False

    return True

print(valid_anagram(str1='nocodeprogram', str2='programcodeno'))
print(valid_anagram(str1='nocodeprogram1', str2='programcodeno2'))

print('----------')

def isAnagram(s: str, t: str) -> bool:
    table = {}

    for c in s:
        count = table.get(c)
        if count is None:
            table[c] = 1
            continue
        table[c] += 1

    for c in t:
        count = table.get(c)
        if count is None:
            return False
        table[c] -= 1

    for key, value in table.items():
        if value != 0:
            return False
    
    return True

print(isAnagram(s="nocodeprogram",t="promodernacog"))
print(isAnagram(s="nocodeprogram1",t="promodernacog2"))