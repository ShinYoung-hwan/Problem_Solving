import sys
from collections import deque

MAX_SIZE = 100001

input = lambda : sys.stdin.readline().rstrip()

def get_min_path(src, dest):
    # using bfs algorithm
    visited = [0] * MAX_SIZE
    queue = deque()
    queue.append(src)
    
    while len(queue) != 0:
        cur_node = queue.popleft()            
        
        for next_node in [cur_node-1, cur_node+1, 2*cur_node]:
            if next_node in range(0, MAX_SIZE):
                if visited[next_node] == 0 and next_node != src:
                    visited[next_node] = visited[cur_node] + 1
                    queue.append(next_node)
    return visited[dest]
    

if __name__ == "__main__":
    posSubin, posSibling = map(int, input().split())
    
    print(get_min_path(posSubin, posSibling))