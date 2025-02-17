import sys

from collections import deque

#sys.setrecursionlimit(10**6)

class Graph():
    def __init__(self, nNodes):
        self.items = [ [] for _ in range(nNodes+1) ]
        self.nNodes = nNodes
        
    def set_edge(self, node1, node2):
        self.items[node1].append(node2)
        self.items[node2].append(node1)
        self.items[node1].sort()
        self.items[node2].sort()
        
    def dfs(self, start_node):
        stack = deque()
        visited = [ False for _ in range(self.nNodes+1) ]
        
        stack.append(start_node)
        
        while len(stack) != 0:
            cur_node = stack.pop()
            
            if not visited[cur_node]:
                visited[cur_node] = True
                print(cur_node, end=' ')
                for next_node in reversed(self.items[cur_node]):
                    stack.append(next_node)
    
    def bfs(self, start_node):
        queue = deque()
        visited = [ False for _ in range(self.nNodes+1) ]
        
        queue.append(start_node)
        visited[start_node] = True
        
        while len(queue) != 0:
            cur_node = queue.popleft()
            print(cur_node, end=' ')
            for next_node in self.items[cur_node]:
                if not visited[next_node]:
                    queue.append(next_node)
                    visited[next_node] = True
    
if __name__ == "__main__":
    nNodes, nEdges, start_node = map(int, sys.stdin.readline().rstrip().split())
    #print(nNodes, nEdges, start_node)
    
    graph = Graph(nNodes)
    
    for _ in range(nEdges):
        node1, node2 = map(int, sys.stdin.readline().rstrip().split())
        graph.set_edge(node1, node2)
        
    graph.dfs(start_node)
    print()
    graph.bfs(start_node)
    