isIn = lambda r, c: (0 <= r < 5) and (0 <= c < 5)

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

def find(board, r0, c0, keyword, idx=1):
    
    # base
    if len(keyword) == idx: 
        return True
    
    # default
    for i in range(8):
        r, c = r0 + dr[i], c0 + dc[i]
        
        if not isIn(r, c): continue
        if board[r][c] == keyword[idx] and find(board, r, c, keyword, idx+1):
            return True
        
    return False

def find_keyword(board, keyword):
    for r in range(5):
        for c in range(5):
            if board[r][c] != keyword[0]: continue # 첫번째 문자가 다른 경우
            if not find(board, r, c, keyword): continue # 문자를 찾아내지 못한 경우
                
            return "YES"
    
    return "NO"

if __name__ == "__main__":
    C = int(input())
    
    for t in range(C):
        board = tuple([ tuple([ c for c in input() ]) for _ in range(5) ])
        
        N = int(input())
        for n in range(N):
            keyword = input() # 
            
            print(f"{keyword} {find_keyword(board, keyword)}")