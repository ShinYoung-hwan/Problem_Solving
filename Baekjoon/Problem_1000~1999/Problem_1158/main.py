import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N, K = map(int, input().split())
    queue = deque([ str(i) for i in range(1, N+1) ])
    
    answer = []
    
    while queue:
        for i in range(K):
            poped = queue.popleft()
            if i == K-1:
                answer.append(poped)
            else:
                queue.append(poped)
    
    print("<", end='')
    print(', '.join(answer), end='')
    print(">")
    