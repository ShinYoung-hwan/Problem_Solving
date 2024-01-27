import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    A = [ int(e) for e in input().split() ] # 수열 A
    
    dp = [ 1 ] * n
    
    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j]+1)
    
    print(max(dp))