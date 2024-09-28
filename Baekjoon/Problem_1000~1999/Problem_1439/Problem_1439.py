import sys

input = lambda: sys.stdin.readline().rstrip()

def update_cnt(s):
    global zero_cnt, one_cnt
    if s: one_cnt += 1
    else : zero_cnt += 1

if __name__ == "__main__":
    S = list(map(int, input()))
    
    zero_cnt = 0
    one_cnt = 0
        
    prev = S[0]
    update_cnt(prev)
    
    for i in range(len(S)):
        s = S[i]
        if prev == s: continue
        
        update_cnt(s)
        prev = s
    
    print(min(zero_cnt, one_cnt))