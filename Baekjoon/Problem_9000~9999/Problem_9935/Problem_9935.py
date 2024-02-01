import sys

input = lambda: sys.stdin.readline().rstrip()

def solve(string, explosion):
    explosion_lst = list(explosion)
    stack = []
    
    for ch in string:
        stack.append(ch)
        if stack[-len(explosion):] == explosion_lst: # 마지막에
            for _ in range(len(explosion)): stack.pop()
    
    return ''.join(stack) if stack else "FRULA"

if __name__ == "__main__":
    string = input() 
    explosion = input()
    
    print(solve(string, explosion))
    