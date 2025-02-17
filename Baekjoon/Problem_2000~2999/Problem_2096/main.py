import sys

from collections import deque

input = lambda: sys.stdin.readline().rstrip()
inputs = lambda: sys.stdin.readlines() 
    
if __name__ == "__main__":
    n = int(input())
    
    lst = list(map(int, input().split()))
    max_dq, min_dq = deque(), deque()
    max_dq.append(lst)
    min_dq.append(lst)
    
    for i in range(n-1):
        
        il, im, ir = map(int, input().split())
        
        # 최대값 구하기
        l, m, r = max_dq.popleft()
        max_dq.append([max(l+il, m+il), max(l+im, m+im, r+im), max(m+ir, r+ir)])
        
        # 최솟값 구하기
        l, m, r = min_dq.popleft()
        min_dq.append([min(l+il, m+il), min(l+im, m+im, r+im), min(m+ir, r+ir)])
        
        
    print(max(max_dq[-1]), min(min_dq[-1]))