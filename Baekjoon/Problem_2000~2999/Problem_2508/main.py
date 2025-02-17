import sys

input = lambda: sys.stdin.readline().rstrip()

def is_row_candy(matrix, visited, R, C, r0, c0):
    row_candy = ">o<"
    
    for i in range(3):
        if c0 + 2 >= C: return False
        if visited[r0][c0+i] or matrix[r0][c0+i] != row_candy[i]: return False
        
    return True
    
def is_col_candy(matrix, visited, R, C, r0, c0):
    col_candy = "vo^"
    
    for i in range(3):
        if r0 + 2 >= R: return False
        if visited[r0+i][c0] or matrix[r0+i][c0] != col_candy[i]: return False
        
    return True

if __name__ == "__main__":
    for t in range(int(input())):
        ans = 0
        
        sys.stdin.readline() # buf
        R, C = map(int, input().split())
        
        matrix = []
        for _ in range(R): matrix.append(list(input()))
        
        visited = [ [False] * C for _ in range(R) ]
        
        for r in range(R):
            for c in range(C):
                
                if is_row_candy(matrix, visited, R, C, r, c):
                    visited[r][c] = True
                    visited[r][c+1] = True
                    visited[r][c+2] = True
                    ans += 1
                    
                elif is_col_candy(matrix, visited, R, C, r, c):
                    visited[r][c] = True
                    visited[r+1][c] = True
                    visited[r+2][c] = True
                    ans += 1

        print(ans)