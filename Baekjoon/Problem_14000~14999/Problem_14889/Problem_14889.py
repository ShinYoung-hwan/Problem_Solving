import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

def get_score(s: tuple, dp: dict):
    if s not in dp:
        score = 0
        for u, v in combinations(s, 2):
            score += S[u][v] + S[v][u]
        dp[s] = score
    return dp[s]

def get_score_difference(cur: tuple, rest: tuple, dp: dict):
    diff = get_score(cur, dp)
    diff -= get_score(rest, dp)
    
    return abs(diff)

if __name__ == "__main__":
    N = int(input())
    S = [ list(map(int, input().split())) for _ in range(N) ]
    
    answer = sys.maxsize
    dp = dict()
    
    for cur in combinations(range(N), N//2):
        rest = tuple(set(range(N)) - set(cur))
        
        answer = min(answer, get_score_difference(cur, rest, dp))
        
    print(answer)
    