import sys
from itertools import permutations

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    
    answer = 0
    for perm in permutations(range(N), N):
        
        _sum = 0
        for i in range(N-1):
            a_cur, a_next = A[perm[i]], A[perm[i+1]]
            _sum += abs(a_cur - a_next)
        answer = max(answer, _sum)
        
    print(answer)