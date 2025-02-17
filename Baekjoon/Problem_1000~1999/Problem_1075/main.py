import sys

input = lambda: sys.stdin.readline().rstrip()

def solve(N: str, F: int):
    start = N[:-2]
    for last_digit in range(0, 100):
        last_digit = f'{last_digit:02}'
        
        cur = int(start+last_digit)
        if cur % F == 0:
            return last_digit

if __name__ == "__main__":
    N = input()
    F = int(input())
    
    print(solve(N, F))