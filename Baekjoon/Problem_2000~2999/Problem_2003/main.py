import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    cnt = 0
    l, r = 0, 0
    _sum = A[0]
    while l < N:
        if _sum > M:
            _sum -= A[l]
            l += 1
        elif _sum < M:
            if r == N-1: break
            r += 1
            _sum += A[r]
        else:
            cnt += 1
            if r == N-1: break
            r += 1
            _sum = _sum + A[r] - A[l]
            l += 1
    
    print(cnt)