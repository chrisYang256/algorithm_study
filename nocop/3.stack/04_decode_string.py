"""
<중급 난이도>
문자열에 괄호안에 있는 문자열이 있고 그 앞에 숫자가 있을 때
그 숫자만큼 괄호안의 문자가 반복시키고 괄호를 제외한 문자열들을 리턴하는 문제입니다.
'a2[b2[ak]]'라는 문자열이 주어질 경우 'abakakbakak'가 출력되어야 하고
'11[a]3[def]7[b]'의 경우 aaaaaaaaaaadefdefdef'이 출력되어야 합니다.

괄호를 보면 stack approach에 대해 생각해 볼 수 있으며 스택을 두 개를 활용하여 접근할 수 있습니다.
한쪽에는 문자를 쌓는 문자스택, 한쪽에는 반복 횟수를 쌓는 숫자스택을 만듭니다.
그리고 문자와 숫자 정보를 각각 임시저장할 곳을 필요로 합니다.
a2[b2[ak]]의 경우 a, 2가 각각 임시 저장됩니다.
문자나 숫자가 연속될 수 있기 때문에 임시저장이 필요한 것입니다.
그리고 여는 괄호를 만나면 임시저장된 정보를 스택에 쌓는데 [a], [2]처럼 각각의 스택에 쌓입니다.
이후 b, 2 임시저장 -> 여는괄호 -> [a,b], [2,2]가 됩니다.
문자열이 연속되는 ak는 a 임시저장 -> a에 b가 더해져 ak가 임시저장 됩니다.
닫히는 괄호를 만나면 이제 앞서 스택에 쌓인 데이터를 역순으로 불러와 결합시키는 작업을 합니다.
현재 임시저장되어 있는 문자 ak는 바로 이전의 숫자 2만큼의 반복 대상이 되므로 반복시키고(akak)
그 이전의 문자를 앞에 더해준 후 임시저장 합니다.(bakak)
그리고 숫자 스택에 저장된 2를 꺼내 bakakbakak를 만들고 문자 스택에 저장된 a를 앞에 더해 abakakbakak를 만들면 최종 종료됩니다.
"""

def decode_string(str: str) -> str:
    stack = []     # [a] -> [a, b] -> [a] -> []
    num_stack = [] # [2] -> [2, 2] -> [2] -> []

    cur_num = 0  # 2 -> 0 -> 2
    cur_str = '' # a -> '' -> b -> '' -> a -> ak -> bakak -> abakakbakak
    for pc in str:
        if pc == '[':
            stack.append(cur_str)
            num_stack.append(cur_num)
            cur_str = ''
            cur_num = 0
            continue
        elif pc == ']':
            prev_str = stack.pop() # b // a
            num = num_stack.pop()  # 2 // 2
            cur_str = prev_str + num*cur_str
            continue
        
        if pc.isdigit():
            # 숫자가 연속하여 입력되는 경우 먼저 들어온 숫자(들)를 한자리 더 높인 후 뒷자리를 +
            # 적용할 곳이 있을 것 같으니 기억해두자
            cur_num = cur_num*10 + int(pc) # 2 // 2
        else:
            cur_str += pc                  # a // b // a // k

    return cur_str

print(decode_string(str='a2[b2[ak]]'))
print(decode_string(str='11[a]3[def]'))