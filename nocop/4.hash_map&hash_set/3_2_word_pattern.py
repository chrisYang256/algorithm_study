"""
<초급>
두 개의 문자열이 주어졌을 때 패턴이 일치하면 True를 반환하는 문제입니다.
'coco'와 'grape mama grape mama'가 주어졌다면 c는 grape와, o는 mama와 대응하고 
이어 나오는 c와 o는 각각 앞의 c, o와 마찬가지로 같은 단어가 대응되기 때문에 True가 됩니다.
'abb'와 'corn horn you'가 주어지는 경우 a는 corn과, b는 horn과 대응되었는데 뒤의 b는 you가 대응되면서
패턴이 불일치하여 False가 됩니다.
해시맵을 통해 쉽게 풀 수 있습니다.
TC -> O(n), SC -> O(1)
보충: 해시맵을 문자열 크기만큼 만들어도 공간복잡도가 늘어나지 않는 이유는 key값이 알파벳의 갯수인 26개로 제한되기 때문입니다.
"""

def word_pattern(pattern: str, str: str) -> bool:
    words = str.split(' ')

    if len(pattern) != len(words):
        return False

    # 교차검증을 위해 해시테이블을 두 개 사용
    char_map = {}
    word_map = {}
    for idx, c in enumerate(pattern):
        word = words[idx]
        print(char_map, word_map)
        if c not in char_map: 
            if word in word_map and word_map[word] == c:
                return False
                
            char_map[c] = word
            word_map[word] = c

        elif char_map[c] != word: # 해당 케릭터의 기존 해시된 값과 일치하지 않음
            return False

    return True

# print(word_pattern(pattern='coco', str='grape mama grape mama'))
print(word_pattern(pattern='abba', str='dog dog dog dog'))