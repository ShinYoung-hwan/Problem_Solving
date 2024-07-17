import sys

input = lambda: sys.stdin.readline().rstrip()

# board에서 (r, c) 위치에 퀸을 놓을 때 valid 한지 
def is_valid(board, r, c):
    for i in range(r):
        prev = board[i]
        
        # 같은 열에 존재
        if prev == c :
            return False
        
        # 같은 대각선에 존재
        elif prev + (r - i) == c:
            return False
        elif prev - (r - i) == c:
            return False
    
    return True

def solve(board, N, depth=0):
    global answer
    if depth == N:
        answer += 1
        return
    
    for c in range(N):
        if not is_valid(board, depth, c): continue
        board[depth] = c
        solve(board, N, depth+1)

if __name__ == "__main__":
    N = int(input()) # (N, N) 크기의 체스판, N개의 퀸 배치
    
    answer = 0
    
    # 각 row에서 몇번째 col에 위치시킬 건지
    board = [-1] * N
    # solve(board, N)
    
    # search half
    for i in range(N // 2):
        board[0] = i
        solve(board, N, 1)
    answer *= 2
    
    # 반으로 나누어 떨어지지 않는 경우
    if N & 1:
        board[0] = N // 2
        solve(board, N, 1)

    print(answer)