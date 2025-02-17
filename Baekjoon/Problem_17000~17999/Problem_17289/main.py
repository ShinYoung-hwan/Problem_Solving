import sys

input = lambda: sys.stdin.readline().rstrip()
    
if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    
    # solve
    NGE = [ -1 ] * N
    
    stack = []
    for i in range(N-1):
        if A[i] < A[i+1]:
            NGE[i] = A[i+1]
            
            while len(stack) and A[stack[-1]] < A[i+1]:
                top = stack.pop()
                NGE[top] = A[i+1]
            
        else:
            stack.append(i)
    
    print(*NGE)