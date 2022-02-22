"""
스텍은 데이터가 하나씩 쌓여 올라가는 데이터 구조이며 선입후출(FILO)됩니다.
명령어로는 가장 위의 데이터를 입력하는 push, 빼 내는 Pop, 읽는 top이 있습니다.(언어마다 차이 있음)
배열을 스택의 관점으로 보고 문제를 해결해 나갈 수 있습니다.

다음은 괄호들이 대칭 구조를 이루거나({([])}) 연속된 괄호의 짝이 맞을 때({}()[]), 
혹은 이 두가지가 적절히 나열({[()[]]})될 때만 true가 되는 문제입니다.
만약 stack이 {([와 같이 쌓여있다면 ]를 만나면 [라는 스택이 끝나는 의미로 pop을 해주고 다음으로 ), }을 적용하는 식입니다.
괄호들이 열리고 닫히는 문제가 스텍과 딱 맞기 때문에 괄호 문제는 대부분 stack으로 풀면 풀리게 됩니다.
"""

class ValidParentheses:
    def _match(self, p):
        if p == ')':
            return '('
        elif p == '}':
            return '{'
        elif p == ']':
            return '['

    def is_vaild(self, s):
        stack = []
        for ch in s:
            print('stack:::', stack)
            # stack이 빈 상태에서 닫는 괄호가 들어오는 경우 
            # else문의 stack[-1]이 적용되면서 에러가 나기 때문에 첫 괄호는 무조건 삽입
            if len(stack) == 0: 
                stack.append(ch)
            if ch == '(' or ch == '{' or ch == '[': # 여는 괄호는 stack에 쌓음
                stack.append(ch)
            else:
                match_ch = self._match(ch) # 닫는 괄호가 들어오면 stack의 마지막 괄호와 비교
                last_ch = stack[-1]
                if match_ch == last_ch: # 같은 때만 stack에서 제거
                    stack.pop()
                else:
                    return False
            
        if len(stack) == 0: # stack에 남은게 없어야 짝이 다 맞는 것이므로 True
            return True
        else:
            return False

VP = ValidParentheses()
print(VP.is_vaild('{([{}]())}'))
print(VP.is_vaild('}()[]('))