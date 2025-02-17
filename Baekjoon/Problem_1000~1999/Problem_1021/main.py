import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
get_first = lambda queue: queue.popleft()
move_left = lambda queue: queue.append(queue.popleft())
move_right = lambda queue: queue.appendleft(queue.pop())

def find(lst, target):
    l, r = 0, 0
    length = len(lst)
    
    # left
    cur = 0
    while lst[cur] != target:
        l += 1
        cur = (cur - 1) % length
        
    # right
    cur = 0
    while lst[cur] != target:
        r += 1
        cur = (cur + 1) % length
    
    return l, r
    
if __name__ == "__main__":
    N, M = map(int, input().split()) # 큐의 크기 N, 뽑아내려는 수의 개수 M
    
    queue = deque(range(1, N+1))
    
    answer = 0
    for e in list(map(int, input().split())):
        
        l, r = find(queue, e)
        
        if l <= r:
            answer += l
            for i in range(l): move_right(queue)
            
        else:
            answer += r
            for i in range(r):move_left(queue)
            
        get_first(queue)
    
    print(answer)