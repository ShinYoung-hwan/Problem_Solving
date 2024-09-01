import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    X = int(input())
    
    cnt = 0
    _sum = 0
    for i in range(6, -1, -1):
        if _sum == X: break
        rest = 1 << i
        
        if _sum + rest <= X:
            _sum += rest
            cnt += 1
    
    print(cnt)