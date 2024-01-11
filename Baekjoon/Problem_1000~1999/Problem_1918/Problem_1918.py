import sys

from collections import deque

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    exp = input()
    
    stack = []
    
    for i in range(len(exp)):
        if exp[i] == '(': # 괄호 열기
            stack.append(exp[i])
            
        elif exp[i] == '+' or exp[i] == '-': # 저 우선순위 연산자
            while stack and stack[-1] != '(': # 괄호가 나오기 전까지 출력
                print(stack.pop(), end='')
            stack.append(exp[i])
            
        elif exp[i] == '*' or exp[i] == '/': # 고 우선순위 연산자
            while (stack and stack[-1] != '(' and (stack[-1] == "*" or stack[-1] =='/')):
                print(stack.pop(), end="")
            stack.append(exp[i])
            
        elif exp[i] == ')': # 괄호 닫기
            while (stack and stack[-1] != '('):
                print(stack.pop(), end="")
            stack.pop() # 괄호 빼주기
            
        else: # 피연산자
            print(exp[i], end='')
        
    for i in range(len(stack)):
        print(stack.pop(), end='')