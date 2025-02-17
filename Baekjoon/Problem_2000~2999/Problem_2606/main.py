import sys
from collections import deque

input = lambda : sys.stdin.readline()

def get_virused_nComputers(networks, nComputers):
    visited = [ 0 ] * (nComputers+1)
    queue = deque([ 1 ])
    visited[1] = 1
    
    while len(queue) != 0:
        cur_node = queue.popleft()
        
        for next_node in networks[cur_node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = 1
    
    return sum(visited) - 1

if __name__ == "__main__":
    nComputers = int(input().rstrip())
    nNetworks = int(input().rstrip())
    
    networks = [ [] for _ in range(nComputers+1) ]
    for _ in range(nNetworks):
        com1, com2 = map(int, input().rstrip().split())
        networks[com1].append(com2)
        networks[com2].append(com1)
        
    print(get_virused_nComputers(networks, nComputers))