import sys

input = lambda: sys.stdin.readline().rstrip()

nMinus = 0
nZero = 0
nPlus = 0

def isAll(paper, r0, c0, N, target):
    for r in range(r0, r0+N):
        for c in range(c0, c0+N):
            if paper[r][c] != target: return False
            
    return True

def solve(paper, r0, c0, N):
    global nMinus, nZero, nPlus
    
    if isAll(paper, r0, c0, N, -1):
        nMinus += 1
        return
    elif isAll(paper, r0, c0, N, 0):
        nZero += 1
        return
    elif isAll(paper, r0, c0, N, 1):
        nPlus += 1
        return
    
    for r in range(r0, r0 + N, N//3):
        for c in range(c0, c0 + N, N//3):
            solve(paper, r, c, N//3)


if __name__ == "__main__":
    N = int(input())
    paper = [ list(map(int, input().split())) for _ in range(N) ]

    solve(paper, 0, 0, N)
    
    print(nMinus)
    print(nZero)
    print(nPlus)