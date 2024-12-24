import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input())
    A = [ int(input()) for _ in range(N+1) ]
    
    _sum = 0
    for i in range(N):
        _sum += min([abs(A[i] - A[i+1]), abs(A[i] - (A[i+1] + 360)), abs(A[i] + 360 - A[i+1])])
    print(_sum)