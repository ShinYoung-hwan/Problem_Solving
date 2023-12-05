import sys
import math

input = lambda : sys.stdin.readline().rstrip()

def get_nYears(target_x, target_y, M, N):        
    nYears = target_x
    y = target_x % N
    y = N if y == 0 else y
    
    while y != target_y:
        if nYears > math.lcm(M, N):
            return -1
        
        #print(f'<{x}:{y}> - {nYears}')
        y = (y+M) % N
        y = N if y == 0 else y
        nYears += M
    
    return nYears
        

if __name__ == "__main__":
    testcase = int(input())
    
    for _ in range(testcase):
        M, N, x, y = map(int, input().split())
        #print(x, y, M, N)
        print(get_nYears(x, y, M, N))