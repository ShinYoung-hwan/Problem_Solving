import sys

input = lambda: sys.stdin.readline().rstrip()

def solve(s: int, e: int) -> int:
    global N, K
    # base
    if s == e:
        return s
    
    # default
    m = (s + e) // 2
    cnt = 0
    for i in range(1, N+1):
        cnt += min(N, m // i)
    
    return solve(0, m) if cnt >= K else solve(m+1, e)

if __name__ == "__main__":
    N, K = int(input()), int(input())

    print(solve(0, K))
    