import sys

input = lambda: sys.stdin.readline().rstrip()

MOD = 1_000_000_007

def factorial(n):
    ans = 1
    
    for i in range(2, n+1):
        ans *= i
        ans %= MOD
    
    return ans

def pow(a, n):
    if n == 1:
        return a
    
    half = pow(a, n//2)
    ans = ((half % MOD) * (half % MOD)) % MOD
    if n & 1:
        ans = (ans * a) % MOD
    
    return ans

def combination(N, K):
    
    return ((factorial(N) % MOD) * pow( ((factorial(N-K) % MOD) * (factorial(K) % MOD) ) % MOD , MOD-2)) % MOD

if __name__ == "__main__":
    N, K = map(int, input().split())
    
    # Modulo Inverse
    print(combination(N, K))