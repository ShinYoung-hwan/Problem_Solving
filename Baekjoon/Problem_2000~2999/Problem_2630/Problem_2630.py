import sys

input = lambda : sys.stdin.readline()
inputs = lambda : sys.stdin.readlines()

def count_area(board, n, pos):
    global nBlue_area, nWhite_area
    start_x, start_y = pos
    
    color_checker = board[start_y][start_x]
    
    for y in range(start_y, start_y+n):
        for x in range(start_x, start_x+n):
            #print(board[y][x])
            if board[y][x] != color_checker:
                return False
    
    if color_checker == '1': nBlue_area += 1
    else : nWhite_area += 1
    return True

def count_areas(board, n, pos):
    if n == 1:
        count_area(board, n, pos)
        return 
    
    if not count_area(board, n, pos):
        start_x, start_y = pos
        half_n = int(n/2)
        # 1사분면
        count_areas(board, half_n, (start_x+half_n, start_y))
        # 2사분면
        count_areas(board, half_n, (start_x, start_y))
        # 3사분면
        count_areas(board, half_n, (start_x, start_y+half_n))
        # 4사분면
        count_areas(board, half_n, (start_x+half_n, start_y+half_n))        

if __name__ == "__main__":
    n = int(input().rstrip())
    board = [ line.rstrip().split() for line in inputs() ]
    
    nBlue_area, nWhite_area = 0, 0
    
    count_areas(board, n, (0, 0))
    
    print(nWhite_area)
    print(nBlue_area)
    
    