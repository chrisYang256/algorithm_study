"""
<중급 난이도>

문자열에 괄호안에 있는 문자열이 있고 그 앞에 숫자가 있을 때
그 숫자만큼 괄호안의 문자가 반복시키고 괄호를 제외한 문자열들을 리턴하는 문제입니다.
'a2[b2[ak]]'라는 문자열이 주어질 경우 'abakakbakak'가 출력되어야 하고
'9[a]3[def]7[b]'의 경우 aaaaaaaaadefdefdefbbbbbbb'이 출력되어야 합니다.

"""

from calendar import c


def decode_string(str: str) -> str:
    stack = []
    num_stack = []

    cur_num = 0
    cur_str = ''
    for pcs in str:
        if pcs == '[':
            stack.append(cur_str)
            num_stack.append(cur_num)
            cur_str = ''
            cur_num = 0
            continue
        elif pcs == ']':
            prev_str = stack.pop()
            num = num_stack.pop()
            cur_str = prev_str + num*cur_str
            continue
        
        if pcs.isdigit():
            cur_num = cur_num*10 + int(pcs)
        else:
            cur_str += pcs

    return cur_str

print(decode_string(str = 'a2[b2[ak]]'))
print(decode_string(str = '9[a]3[def]7[b]'))