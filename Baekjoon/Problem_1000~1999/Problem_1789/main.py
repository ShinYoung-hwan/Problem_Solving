import sys

input = lambda: sys.stdin.readline().rstrip()
    
if __name__ == "__main__":
    S = int(input()) 
    
    _sum = 0
    cur = 1
    while _sum < S:
        _sum += cur
        cur += 1
    
    print(cur-1 if _sum == S else cur-2)