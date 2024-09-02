import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    
    dp = [ a for a in A ]
    
    for i in range(N):
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j] + A[i])

    # print(dp)
    print(max(dp))