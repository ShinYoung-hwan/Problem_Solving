import sys

from itertools import permutations

sys.setrecursionlimit(10**9)

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n, m = map(int, input().split())
    numbers = [ int(num) for num in input().split() ]
    
    for ai in sorted(list(set(permutations(numbers, m)))):
        print(*ai)