import sys

input = lambda: sys.stdin.readline().rstrip()

def solve(start=0, lst=[], n=0):
    if n == 6:
        print(*lst)
        return
    
    for i in range(start, k):
        lst.append(S[i])
        solve(i+1, lst, n+1)
        lst.pop()
    
if __name__ == "__main__":
    while True:
        cmd = list(map(int, input().split()))
        if cmd[0] == 0: break
        
        k, S = cmd[0], cmd[1:]
        
        solve()
        print()