import sys
from math import sqrt, floor
from itertools import product
 
input = lambda : sys.stdin.readline().rstrip()

def solve(n: int):
    one_squares = set([ i ** 2 for i in range(1, floor(sqrt(n))+1) ])
    #print("one squares:", one_squares, sqrt(n))
    if n in one_squares: # 그 자체가 제곱수
        return 1
    
    two_squares = set([ i+j for i, j in product(one_squares, one_squares) if n >= i+j ])
    #print("two squares", two_squares)
    if n in two_squares: # 제곱수 2개로 이루어진 경우
        return 2
    
    for i in one_squares: # 제곱수 3개로 이루어진 경우
        if n - i in two_squares:
            return 3
    
    return 4
    
if __name__ == "__main__":
    n = int(input())
    
    print(solve(n))
    
    