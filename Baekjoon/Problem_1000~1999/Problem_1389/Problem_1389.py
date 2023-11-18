import sys

from collections import deque

input = lambda : sys.stdin.readline().rstrip()

def get_relation_graph(nUsers, relations):
    relation_graph = [ [] for _ in  range(nUsers+1) ]
    for user1, user2 in relations:
        relation_graph[user1].append(user2)
        relation_graph[user2].append(user1)
    return relation_graph

def get_kevin_bacon_number(relations, start_person):
    # same as bfs algorithm
    queue = deque()
    visited = [ False for _ in range(len(relations)) ]
    
    cur_node = start_person
    visited[cur_node] = True
    queue.append((cur_node, 0))
    output = 0
    
    while len(queue) > 0:
        cur_node, cur_depth = queue.popleft()
        output += cur_depth
        for next_node in relations[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, cur_depth+1))
    return output
            
    
if __name__ == "__main__":
    nUsers, nRelations = map(int, input().split())
    relations = [ tuple(map(int, relation.rstrip().split())) for relation in sys.stdin.readlines() ]
    relations = get_relation_graph(nUsers, relations)
    
    min_user = 1
    min_number = get_kevin_bacon_number(relations, 1)
    
    for cur_user in range(2, nUsers+1):
        cur_number = get_kevin_bacon_number(relations, cur_user)
        if cur_number < min_number:
            min_user = cur_user
            min_number = cur_number
            
    print(min_user)