import sys

input = lambda: sys.stdin.readline().rstrip()

def solve(l: int, r: int) -> int:
    global fences
    # base
    if l >= r:  return fences[l]
    
    # default: 2*T(n/2)
    m = (l + r) // 2
    # left & right
    ret = max(solve(l, m), solve(m+1, r))
    
    # mid: O(n)
    ml, mr = m, m+1
    h = min(fences[ml], fences[mr])
    ret = max(ret, 2 * h)
    while  l < ml or mr < r:
        if mr < r and (ml == l or fences[ml-1] < fences[mr+1]):
            mr += 1
            h = min(h, fences[mr])
        else:
            ml -= 1
            h = min(h, fences[ml])
            
        ret = max(ret, h * (mr - ml + 1))
    
    return ret

if __name__ == "__main__":
    C = int(input())
    
    for t in range(C):
        N = int(input()) # 나무 판자의 수
        
        fences = list(map(int, input().split())) # 나무 판자의 높이
        print(solve(0, N-1))
            