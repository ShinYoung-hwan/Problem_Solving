import sys

input = lambda: sys.stdin.readline().rstrip()

def fibonacci(n):
    f = [0, 1, 1]
    
    for i in range(3, n+1):
        f.append(f[i-1] + f[i-2])
    
    return f[n]
    
if __name__ == "__main__":
    n = int(input())
    
    fibonacci(n)
    
    # 1의 호출횟수
    # 기저케이스 2개를 제외한 횟수
    print(fibonacci(n), n-2)
    