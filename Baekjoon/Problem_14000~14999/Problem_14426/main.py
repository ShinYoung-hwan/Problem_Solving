import sys
from bisect import bisect_left

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N, M = map(int, input().split())
    
    # N개의 S에 해당하는 문자열
    # 시간복잡도 O(N+NlogN)
    S = sorted([ input() for _ in range(N) ])
    
    # M개의 검사대상 문자열
    # 시간복잡도 O(MlogN)
    answer = 0
    for _ in range(M):
        s = input()
        idx = bisect_left(S, s)
        
        if idx < len(S) and s == S[idx][:len(s)]: answer += 1
        
    print(answer)