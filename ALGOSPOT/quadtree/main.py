import sys

input = lambda: sys.stdin.readline().rstrip()

def solve(iterator: iter) -> str:
    global quadtree
    head = next(iterator)
    # base
    if head == 'b' or head == 'w': return head
    
    # default: x case
    outputs = []
    outputs.append(solve(iterator))
    outputs.append(solve(iterator))
    outputs.append(solve(iterator))
    outputs.append(solve(iterator))
    
    return ''.join(['x', outputs[2], outputs[3], outputs[0], outputs[1]])

if __name__ == "__main__":
    C = int(input())
    
    for t in range(C):
        quadtree = input()
        
        iterator = iter(quadtree)
        print(solve(iterator))
            