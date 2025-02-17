import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

def solve_combinations():
    global answer
    for n in range(1, N+1):
        for comb in combinations(seq, n):
            if sum(comb) == S:
                answer += 1
                
def solve_backtrack(start=0, n=None):
    global answer
    
    if n == S:
        answer += 1
    elif n is None:
        n = 0
        
    for cur in range(start, N):
        solve_backtrack(cur+1, n+seq[cur])
    
if __name__ == "__main__":
    N, S = map(int, input().split()) # N개의 정수, 목표 정수 S
    seq = list(map(int, input().split()))
    
    # solve
    answer = 0

    # solve_combinations()
    solve_backtrack()
        
    print(answer)