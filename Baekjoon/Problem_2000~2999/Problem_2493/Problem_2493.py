import sys

input = lambda: sys.stdin.readline().rstrip()
    
if __name__ == "__main__":
    N = int(input())
    towers = list(map(int, input().split()))
    stack = []
    for i, tower in enumerate(towers):
        while stack and towers[stack[-1]] < tower:
            stack.pop()
            
        print(stack[-1]+1 if stack else 0, end=' ')
        stack.append(i)
    