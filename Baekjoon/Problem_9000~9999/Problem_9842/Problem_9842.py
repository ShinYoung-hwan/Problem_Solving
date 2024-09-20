import sys
from math import sqrt, ceil

input = lambda: sys.stdin.readline().rstrip()

def is_prime(val: int, primes: list) -> bool:
    if val == 2: return True
    
    for i in primes:
        if i > ceil(sqrt(val)): break
        if val % i == 0: return False
        
    return True

if __name__ == "__main__":
    N = int(input())
    
    val = 1
    primes = [ ]
    while len(primes) < N:
        val += 1
        if is_prime(val, primes):
            primes.append(val)

    print(primes[N-1])
    