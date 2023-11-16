import sys
import math
sys.setrecursionlimit(10**6)

pow2 = lambda x: int(math.pow(2, x))

def solve(N, x0, y0, output):
    x_axis, y_axis = x0+pow2(N-1), y0+pow2(N-1)
    
    if N == 0:
        return output
    else:
        if  target_x >= x_axis and target_y < y_axis: # 1사분면
            return solve(N-1, x_axis, y0, output+pow2(N-1)**2)
        elif target_x < x_axis and target_y < y_axis: # 2사분면
            return solve(N-1, x0, y0, output)
        elif target_x < x_axis and target_y >= y_axis: # 3사분면
            return solve(N-1, x0, y_axis, output+2*pow2(N-1)**2)
        else: # 4사분면
            return solve(N-1, x_axis, y_axis, output+3*pow2(N-1)**2)
    

if __name__ == "__main__":
    N, target_y, target_x = map(int, sys.stdin.readline().rstrip().split())
    
    print(solve(N, 0, 0, 0))
    