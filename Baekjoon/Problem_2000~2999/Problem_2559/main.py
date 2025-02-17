import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N, K = map(int, input().split())
    T = map(int, input().split())
    
    S = [0]
    for t in T:
        S.append(S[-1] + t)
    
    max_tempurature = S[N] - S[N-K] # N == K case
    for i in range(K, N):
        max_tempurature = max(max_tempurature, S[i] - S[i-K])
        
    print(max_tempurature)