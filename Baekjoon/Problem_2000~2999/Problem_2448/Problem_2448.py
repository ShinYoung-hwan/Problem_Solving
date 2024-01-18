import sys

sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().rstrip()
inputs = lambda: sys.stdin.readlines()

stars = []

def solve(n, x0, y0):
    if n == 3:
        stars[y0][x0] = '*'
        
        stars[y0+1][x0+1] = '*'
        stars[y0+1][x0-1] = '*'
        
        stars[y0+2][x0-2] = '*'
        stars[y0+2][x0-1] = '*'
        stars[y0+2][x0] = '*'
        stars[y0+2][x0+1] = '*'
        stars[y0+2][x0+2] = '*'

    else:
        half = n // 2
        solve(half, x0, y0)
        solve(half, x0-half, y0+half)
        solve(half, x0+half, y0+half)

if __name__ == "__main__":
    n = int(input()) # 높이 n
    stars = [ [ ' ' ] * (2*n-1) for _ in range(n) ]
    solve(n, n-1, 0)
    
    # 출력하기
    for line in stars:
        print(''.join(line))