import sys

def get_nLans(lans, len):
    if len == 0:
        return 0
    
    output = 0
    for lan in lans:
        output += lan // len
    return output

def get_max_len_bsearch(lans, low, high, target):
    tl, mid, th = low, (low+high)//2, high
    cur_nLans = get_nLans(lans, mid)
    max_len = 0
    while True:
        if tl > th:
            break
        
        if cur_nLans >= target: # 현 길이가 짧거나 같음 유효
            tl, th = mid+1, th
            max_len = mid
        else: # 현 길이가 긺
            tl, th = tl, mid-1
        mid = (tl+th)//2
        cur_nLans = get_nLans(lans, mid)
        
    return max_len

if __name__ == "__main__":
    nLan, nReq = map(int, sys.stdin.readline().rstrip().split())
    lans = [ int(lan.rstrip()) for lan in sys.stdin.readlines() ]
    
    print(get_max_len_bsearch(lans, 1, 2*max(lans), nReq))