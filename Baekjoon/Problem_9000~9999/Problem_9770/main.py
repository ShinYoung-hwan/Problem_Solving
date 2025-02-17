import sys
from itertools import combinations
import math

inputs = lambda: sys.stdin.readlines()

if __name__ == "__main__":
    numbers = [ int(number) for line in inputs() for number in line.split() ] 
    
    ans = 1
    for n1, n2 in combinations(numbers, 2):
        ans = max(ans, math.gcd(n1, n2))
        
    print(ans)