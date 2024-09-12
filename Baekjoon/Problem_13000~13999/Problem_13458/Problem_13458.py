import sys
from math import ceil

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())
        
    # solve
    _sum = 0
    for i in range(N):
        _sum += 1
        A[i] = A[i] - B
        
        if A[i] > 0:
             _sum += ceil(A[i] / C)
    
    print(_sum)