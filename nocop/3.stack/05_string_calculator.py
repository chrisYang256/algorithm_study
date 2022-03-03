"""
<난이도 중급>
'7 - 6 / 3 + 3 * 2 + 4'라는 문자열이 주어졌을 때 계산하는 문제입니다.
위 문자열과 같은 경우 7 - 2 + 6 + 4가 되고 곧 15를 리턴하면 됩니다.

stack을 떠올릴 수 있는 문제입니다.
곱하기, 나누기의 경우 선행하여 연산되어야 하고 덧셈과 뺄셈은 이후에 연산하면 되는 점을 착한하여
7을 스택에 넣고 -6을 이어서 넣은 후 뒤에 오는 나눗셈을 스택의 맨 위 -6과 연산하여 -6/2 = -2로 만드는 식으로 진행하면
[7, -2, 6, 4]가 스택에 남게 되고 이들을 모두 합하면 15가 되게 됩니다.
"""

def calculate(str: str) -> int:
    str += '+' # 마지막 숫자를 stack에 넣기 위해
    stack = []

    cur_num = 0
    prev_cal = '+' # 최초 숫자 stack에 넣기 위해
    for pc in str:
        if pc.isdigit():
            cur_num = cur_num*10 + int(pc) # 숫자 저장 / 2자리 이상 숫자인 경우 고려

        elif pc == ' ':
            continue # 아래 코드 생략

        else:
            if prev_cal == '+':
                print('cnum:::', cur_num)
                stack.append(cur_num)

            elif prev_cal == '-':
                stack.append(-cur_num)

            elif prev_cal == '*':
                stack[-1] = stack[-1]*cur_num

            elif prev_cal == '/':
                stack[-1] = int(stack[-1]/cur_num)

            cur_num = 0
            prev_cal = pc

        print('stack:::', stack)

    return sum(stack)

print(calculate(str='7 - 6 / 3 + 3 * 2 + 4'))