import sys
from math import comb

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N, M = map(int, input().split()) # 수열의 길이 N, modulo M
    A = list(map(int, input().split()))
    
    S = [ 0 ]
    dp = [ [] for _ in range(M) ]
    for i in range(N):
        S.append(S[-1] + A[i])
        dp[S[-1] % M].append(i+1)

    answer = len(dp[0])
    for i in range(M):
        cur = dp[i]
        answer += comb(len(cur), 2)
    print(answer)