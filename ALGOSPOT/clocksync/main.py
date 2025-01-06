import sys

input = lambda: sys.stdin.readline().rstrip()

MAX: int = 1e+6

switches = [
    { 0, 1, 2 },            # 0
    { 3, 7, 9, 11 },        # 1
    { 4, 10, 14, 15 },      # 2
    { 0, 4, 5, 6, 7 },      # 3
    { 6, 7, 8, 10, 12 },    # 4
    { 0, 2, 14, 15 },       # 5
    { 3, 14, 15 },          # 6
    { 4, 5, 7, 14, 15 },    # 7
    { 1, 2, 3, 4, 5 },      # 8
    { 3, 4, 5, 9, 13 }      # 9
]

def is_all_12() -> bool:
    global clocks
    for clock in clocks:
        if clock == 12: continue
        
        return False
    return True
    
def push_switch(switch: int):
    global clocks
    for clock_id in switches[switch]:
        clocks[clock_id] += 3
        if clocks[clock_id] == 15: clocks[clock_id] = 3
    
def solve(switch: int=0):
    # base
    if switch == 10: 
        return 0 if is_all_12() else MAX
    
    # default
    ret = MAX
    for cnt in range(4):
        ret = min(ret, cnt + solve(switch+1))
        push_switch(switch)
    return ret

if __name__ == "__main__":
    C = int(input())
    
    for t in range(C):
        clocks = list(map(int, input().split()))
        
        ans = solve()
        print(-1 if ans >= MAX else ans)
        