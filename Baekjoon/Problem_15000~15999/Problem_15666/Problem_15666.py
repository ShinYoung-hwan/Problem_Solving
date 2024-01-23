import sys

from itertools import combinations_with_replacement

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n, m = map(int, input().split())
    numbers = sorted([ int(num) for num in input().split() ])
    
    for ai in sorted(list(set(combinations_with_replacement(numbers, m)))):
        print(*ai)