import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    rest_alphas = [ 0, 2, 2, 4, 3, 5 ]
    
    T = int(input())
    for t in range(T):
        N = int(input())
        rest = N % 6
        division = N // 6
        base = 5 * division
        answer = base + rest_alphas[rest]
        
        print(answer)
    