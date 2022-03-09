"""
알파벳으로 된 문자열 중에 반복되는 알파벳을 지워주는 문제입니다.
스택을 사용해 매우 쉽게 풀 수 있는 문제입니다.
아래와 같이 스택을 사용하는 경우 문자를 하나씩 쌓아가며 삭제하게 되면 마지막에 문자가 더이상 존재하지 않으므로
문자열 내에서 문자를 삭제하는 경우 삭제한 문자 뒤에 있는 문자를 앞으로 shift해야 하는 복잡한 연산이 필요 없어집니다.
array, string 문제를 마주하게 된다면 정렬, 투포인터스, 바이너리서치 외에 stack approach를 생각하는 연습이 필요합니다.

<초급 난이도>
문자열에서 2개의 알파벳이 연속하는 경우 그 알파벳들을 삭제하는 문제입니다.
배열을 스택처럼 사용하면 됩니다.
'abccdeefg'라는 문자열이 있는 경우 배열의 처음부터 시작하여 배열에 넣으면서
같은 문자가 들어오게 되면 삭제해 주면 되고 'abdfg'가 출력되야 합니다.
포인터가 문자열의 처음부터 끝까지 이동하였으므로 시간복잡도는 O(n), 알파벳이 보관되는 스택을 사용하였으므로 공간복잡도는 O(n)이 됩니다.

<중급 난이도>
'abcccdeefg'라는 문자열과 특정한 숫자 n이 함께 주어지면 숫자만큼 같은 알파벳이 연속되는 경우만 삭제해줍니다.
위 문제에서 n이 3이라면 'abdeefg'가, 2라면 'abcccdfg'가 출력되어야 합니다.
두 개의 스택을 만들고 한쪽에는 알파벳을, 한쪽에는 다른 한쪽의 스택에 쌓이는 알파벳을 카운팅합니다.
만약 n이 3인 경우 스택에 c가 3번 쌓이는 경우 카운팅하는 스택의 값이 3이 되기 때문에 pop을 해주면 됩니다.
시간복잡도는 O(n), 공간복잡도는 두개의 스택을 사용하였으므로 O(2n)이 되고 즉 O(n)이 됩니다.
"""


def remove_duplicats(str: str) -> str:
    stack = []
    for piece in str:
        if len(stack) == 0: # 첫 비교를 위해 하나 문자를 입력되어 있어야함
            stack.append(piece)
        elif stack[-1] == piece:
            stack.pop()
        else:
            stack.append(piece)
    
    return ''.join(stack)

print(remove_duplicats(str = 'abccdeffg'))

print('----------')

def remove_duplicats_n(str: str, n: int) -> str:
    stack = []
    count_stack = []

    for piece in str:
        if len(stack) == 0:
            stack.append(piece)
            count_stack.append(1)
        elif stack[-1] == piece:
            dup_count = count_stack[-1] # 중복 횟수 확인을 위한 이전 카운팅 불러오기
            if dup_count < n-1:
                stack.append(piece)
                count_stack.append(dup_count+1)
                print('count_stack-1:::', count_stack)
            # dup_count가 n-1인 상태에서 똑같은 알파벳이 들어온 상태이므로 곧 dup_count == n이 되는 순서
            # 따라서 stack이나 count_stack을 추가할 필요 없이 n-1만큼 기존 스택을 제거하기만 하면 됨
            elif dup_count == n-1: 
                for _ in range(n-1):
                    stack.pop()
                    count_stack.pop()
            print('count_stack-2:::', count_stack)
            
        else:
            stack.append(piece)
            count_stack.append(1)
    
    return ''.join(stack)

print(remove_duplicats_n(str = 'abcccdeffg', n = 3))