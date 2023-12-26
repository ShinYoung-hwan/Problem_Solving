import sys

input = lambda : sys.stdin.readline().rstrip()

dp = [ 0 ] * 1001
dp[1], dp[2] = 1, 2

def get_count_fill(n: int) -> int:    
    if dp[n]:
        return dp[n]
    else:
        dp[n] = get_count_fill(n-1) + get_count_fill(n-2)
        return dp[n]

if __name__ == "__main__":
    n = int(input())
    
    print(get_count_fill(n) % 10007)