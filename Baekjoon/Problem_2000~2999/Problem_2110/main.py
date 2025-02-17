import sys

input = lambda: sys.stdin.readline().rstrip()

def is_valid_distance(distance):
    cnt = 1
    prev = houses[0]
    for i in range(1, N):
        cur = houses[i]
        if cur - prev >= distance:
            prev = cur
            cnt += 1
            
        if cnt == C: return True
    
    return False
    
if __name__ == "__main__":
    N, C = map(int, input().split())
    
    houses = sorted([ int(input()) for _ in range(N) ])
    
    l, r = 0, houses[-1]
    ans = 0
    while l <= r:
        m = (l + r) // 2
        
        if is_valid_distance(m):
            l = m + 1
            ans = m
        else:
            r = m - 1
    
    print(ans)