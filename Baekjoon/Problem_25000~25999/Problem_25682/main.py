import sys

input = lambda: sys.stdin.readline().rstrip()
    

if __name__ == "__main__":
    N, M, K = map(int, input().split()) # (N, M) 크기의 체스판 -> (K, K) 크기의 체스판
    board = [ list(input()) for _ in range(N) ]
    
    dp = [[ [0] * (M+1) for _ in range(N+1) ] for _ in range(2)] # 0: (0, 0)이 B기준, 1: (0, 0)이 W
    for r in range(N):
        for c in range(M):
            if (r + c) & 1:
                dp[0][r][c] = dp[0][r][c-1] + dp[0][r-1][c] - dp[0][r-1][c-1] + (1 if board[r][c] == 'B' else 0)
                dp[1][r][c] = dp[1][r][c-1] + dp[1][r-1][c] - dp[1][r-1][c-1]  + (1 if board[r][c] == 'W' else 0)
                
            else:
                dp[0][r][c] = dp[0][r][c-1] + dp[0][r-1][c] - dp[0][r-1][c-1]  + (1 if board[r][c] == 'W' else 0)
                dp[1][r][c] = dp[1][r][c-1] + dp[1][r-1][c] - dp[1][r-1][c-1]  + (1 if board[r][c] == 'B' else 0)
    
    # solve
    answer = K * K
    for r in range(K-1, N):
        for c in range(K-1, M):
            answer = min(
                [
                    answer,
                    dp[0][r][c] - dp[0][r][c-K] - dp[0][r-K][c] + dp[0][r-K][c-K],
                    dp[1][r][c] - dp[1][r][c-K] - dp[1][r-K][c] + dp[1][r-K][c-K],
                ]
            )

    print(answer)