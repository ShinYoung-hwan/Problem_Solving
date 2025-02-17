import sys

input = lambda: sys.stdin.readline().rstrip()

def factorial(n: int) -> int:
    _prod = 1
    for i in range(1, n+1):
        _prod *= i
    return _prod

if __name__ == "__main__":
    N = int(input())
    
    print(factorial(N))