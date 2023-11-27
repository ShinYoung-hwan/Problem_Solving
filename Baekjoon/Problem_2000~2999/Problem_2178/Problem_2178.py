import sys
from collections import deque

input = lambda : sys.stdin.readline()

def is_in_maze(cur_pos, maze_size):
    return 0 <= cur_pos[0] < maze_size[0] and 0 <= cur_pos[1] < maze_size[1]

def get_min_nNodes_bfs(maze, start_pos, dest_pos):
    ret = dest_pos[0] * dest_pos[1]
    visited = [ [ False ] * dest_pos[0] for _ in range(dest_pos[1]) ]
    queue = deque()
    queue.append((start_pos, 1))
    visited[0][0] = True
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    while len(queue) != 0:
        (cur_x, cur_y), cur_nNodes = queue.popleft()
        #print(cur_x, cur_y, cur_nNodes)
        if (cur_x+1, cur_y+1) == dest_pos:
            ret = ret if cur_nNodes >= ret else cur_nNodes
        
        for i in range(4):
            x, y = cur_x+dx[i], cur_y+dy[i]
            
            if is_in_maze((x, y), dest_pos) and maze[y][x]:
            
                if not visited[y][x]:
                    queue.append(((x, y), cur_nNodes+1))
                    visited[y][x] = True
    
    return ret

if __name__ == "__main__":
    y, x = map(int, input().rstrip().split())
    maze = [ [ int(x) for x in input().rstrip() ] for _ in range(y)  ]
    #maze = get_maze_graph(maze, x, y)
    print(get_min_nNodes_bfs(maze, (0, 0), (x, y)))