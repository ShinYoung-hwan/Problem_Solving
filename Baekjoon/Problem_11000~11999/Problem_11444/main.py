import sys

input = lambda: sys.stdin.readline().rstrip()

MOD = 1_000_000_007
    
dp = {
    0: 0,
    1: 1,
    2: 1,
}

def fibo(n: int):
    if n not in dp:
        if n & 1: dp[n] = (fibo((n+1)//2)**2 + fibo((n-1)//2)**2) % MOD
        else: dp[n] = (fibo(n//2)*(fibo(n//2+1) + fibo(n//2-1))) % MOD

    return dp[n]
    
if __name__ == "__main__":
    n = int(input())
    print(fibo(n))