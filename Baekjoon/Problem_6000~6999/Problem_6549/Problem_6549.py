import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def solve(l: int, r: int):
    global hist
    # base
    if l >= r:
        return hist[l]
    
    # default, left & right: 2T(n/2)
    m = (l + r) // 2
    ml, mr = m, m+1
    ret = max(solve(l, ml), solve(mr, r))
    
    # default, mid: O(n)
    h = min(hist[ml], hist[mr])
    ret = max(ret, 2 * h)
    
    while l < ml or mr < r:
        if mr < r and (l == ml or hist[ml-1] < hist[mr+1]): # 우로 확장
            h = min(h, hist[mr:=mr+1])
        else: # 좌로 확장
            h = min(h, hist[ml:=ml-1])
            
        ret = max(ret, h * (mr - ml +1))
    
    return ret

if __name__ == "__main__":
    while (hist:=deque(map(int, input().split())))[0] != 0:
        N = hist.popleft()
        print(solve(0, N-1))