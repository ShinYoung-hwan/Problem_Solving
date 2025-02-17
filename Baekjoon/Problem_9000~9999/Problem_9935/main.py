import sys

input = lambda: sys.stdin.readline().rstrip()

def is_in(string: list, word: str, word_len: int) -> bool:
    # string 내부에 word가 있는지 확인한다.
    if len(string) < word_len: return False
    
    for i in range(1, word_len+1):
        if string[-i] != word[-i]:
            return False
        
    return True

if __name__ == "__main__":
    s = input() # 폭파 시켜야하는 문자열
    es = input() # 폭파 시킬 문자열
    es_len = len(es)
    stack = []
    
    # solve
    # s안에 es가 있으면 삭제시킨다. by stack
    for c in s:
        stack.append(c)
        while is_in(stack, es, es_len):
            for _ in range(es_len): stack.pop()
        
    s = ''.join(stack)
    
    print(s if s else "FRULA")