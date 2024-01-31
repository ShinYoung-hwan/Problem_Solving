import sys

input = lambda: sys.stdin.readline().rstrip()

def is_promising(depth):
    # 같은 열이나 대각선상에 있으면 안된다.
    for y in range(depth):
        if rows[y] == rows[depth] or depth - y == abs(rows[y] - rows[depth]): return False
    
    return True

def solve(depth):
    global res
    if depth == n:
        res += 1
        return

    for x in range(n):
        rows[depth] = x
        
        if is_promising(depth):
            solve(depth+1)

if __name__ == "__main__":
    n = int(input()) # 체스판의 크기 n, Queen의 개수
    
    rows = [ 0 ] * n # (row, col) 각 row, col 위치에 퀸을 놓겠다.
    
    res = 0 # 경우의 수
    solve(0)                 
    print(res)