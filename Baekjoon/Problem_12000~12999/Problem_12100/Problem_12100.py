import sys

input = lambda: sys.stdin.readline().rstrip()

RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

def move(board0, dir):
    board = [ [ 0 ] * N for _ in range(N) ]
    
    
    
    return board

def dfs(board, depth=0):
    global answer
    
    # base
    if depth == 5:
        for row in board:
            for e in row:
                answer = max(answer, e)
        return
    
    # default
    if depth != 0:
        pass
    
    for dir in range(4):
        dfs(move(board, dir), depth+1)
    
    
if __name__ == "__main__":
    N = int(input()) # 보드판의 크기
    board = [ list(map(int, input().split())) for _ in range(N) ]

    answer = 0
    
    dfs(board)
    
    print(answer)