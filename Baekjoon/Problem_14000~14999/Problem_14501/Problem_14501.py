import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input())
    T = []
    P = []
    for _ in range(N):
        t, p = map(int, input().split())
        T.append(t)
        P.append(p)
        
    dp = [ 0 ] * N
    for i in range(0, N):
        today = P[i]
        # 현재일 기준으로 상담을 하면 퇴사 불가능
        if i + T[i] > N:
            today = 0
        
        for j in range(max(0, i-5, i)):
            # 현재일은 상담 불가능
            if j + T[j] > i: continue
            
            dp[i] = max(dp[i], dp[j]+today)
        if dp[i] == 0 and i + T[i] <= N: dp[i] = P[i]
    # print(dp)
    print(max(dp))