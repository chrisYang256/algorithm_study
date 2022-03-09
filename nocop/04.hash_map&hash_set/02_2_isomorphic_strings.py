"""
<초급>
두 개의 알파벳 문자열이 주어지고 알파벳의 반복 패턴이 같으면 true를 길이가 다르거나 패턴이 다르면 false를 리턴하는 문제입니다.
'aaccd', 'xxyyz'는 각각의 요소가 두번 두번 한번 동일하게 반복되므로 true입니다.
'abccd', 'xxyyz'는 반복횟수가 틀리므로 false입니다.
TC는 O(n), SC는 O(1)입니다.
"""

def isomorphic_pattern(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    length = len(str1)

    hash1 = {}
    hash2 = {}
    for idx in range(0, length):
        match1 = hash1.get(str1[idx])
        match2 = hash2.get(str2[idx])
        if match1 is None and match2 is None: # 두 개의 해시테이블에 각각의 문자열을 교차 저장하여 검증
            hash1[str1[idx]] = str2[idx] # a: x
            hash2[str2[idx]] = str1[idx] # x: a
            continue

        elif match1 == str2[idx] and match2 == str1[idx]: # 기존 저장된 해시값과 같은지(같은 알파벳인지) 확인
            continue

        return False # 둘중 하나의 해시값을 get하지 못하거나, 두개 모두 get 해도 기존 해시값과 둘 중 하나가 다른 경우

    return True

print(isomorphic_pattern(str1='aaccd', str2='xxyyz'))