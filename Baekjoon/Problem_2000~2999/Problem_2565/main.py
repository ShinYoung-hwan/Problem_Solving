import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input()) # 전깃줄의 개수
    
    links = sorted([ tuple(map(int, input().split())) for _ in range(N) ]) # 전깃줄의 종류
    
    dp = [ 1 ] * N
    
    for i in range(N):
        for j in range(i):
            if links[i][1] > links[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    print(N - max(dp))