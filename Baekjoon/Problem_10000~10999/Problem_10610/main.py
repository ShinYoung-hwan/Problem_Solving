import sys

input = lambda: sys.stdin.readline().rstrip()

def solve(N):
    # 10의 배수가 아님
    if N[-1] != 0: return [-1]
    
    # 3의 배수가 아님
    elif sum(N) % 3 != 0: return [-1]
    
    # 30의 배수임이 보장됨.
    return N

if __name__ == "__main__":
    N = sorted(list(map(int, input())), reverse=True)

    print(''.join(map(str, solve(N))))