import sys

input = lambda : sys.stdin.readline().rstrip()

dp = [ -1 ] * 1001
dp[1], dp[2] = 1, 3

def get_n_fill_box(n: int):
    if dp[n] == -1:
        dp[n] = get_n_fill_box(n-1) + 2 * get_n_fill_box(n-2)
    return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(get_n_fill_box(n) % 10007)
    