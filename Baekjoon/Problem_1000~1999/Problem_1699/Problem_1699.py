import sys

input = lambda: sys.stdin.readline().rstrip()
    
if __name__ == "__main__":
    N = int(input())
    
    squares = []
    dp = [ sys.maxsize ] * (N+1)
    dp[1] = 1
    
    # 제곱수들 구하기
    for i in range(2, N):
        if i ** 2 > N: break
        squares.append(i ** 2)
        dp[i ** 2] = 1
    
    for i in range(2, N+1):
        dp[i] = min(dp[i], dp[i-1] + 1)
        for square in squares:
            if i < square: break
            dp[i] = min(dp[i], dp[square] + dp[i - square])
        
    print(dp[N])
    