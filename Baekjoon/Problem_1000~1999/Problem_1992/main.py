import sys

input = lambda: sys.stdin.readline().rstrip()

def isAll(im0, r0, c0, N, target):
    for r in range(r0, r0+N):
        for c in range(c0, c0+N):
            if im0[r][c] != target:
                return False
    return True

def solve(im0, r0, c0, N):
    if isAll(im0, r0, c0, N, "0"): return "0"
    elif isAll(im0, r0, c0, N, "1"): return "1"
    
    im1 = solve(im0, r0, c0, N//2)
    im2 = solve(im0, r0, c0+N//2, N//2)
    im3 = solve(im0, r0+N//2, c0, N//2)
    im4 = solve(im0, r0+N//2, c0+N//2, N//2)
    return ''.join(["(", im1, im2, im3, im4,")"])

if __name__ == "__main__":
    N = int(input()) # 2의 제곱수
    im0 = [ list(input()) for _ in range(N) ]
    
    print(solve(im0, 0, 0, N))