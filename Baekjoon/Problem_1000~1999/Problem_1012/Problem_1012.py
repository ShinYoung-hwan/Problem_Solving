import sys
sys.setrecursionlimit(10 ** 6)

def worm_traversal(fields, x0, y0, width, height):
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    
    for i in range(4):
        x, y = x0 + dx[i], y0 + dy[i]
        
        if (0 <= x < width) and (0 <= y < height):
            if fields[y][x] == 1:
                fields[y][x] = 0
                fields = worm_traversal(fields, x, y, width, height)
                
    return fields

if __name__ == "__main__":
    nTestcase = int(sys.stdin.readline().rstrip())
    
    for _ in range(nTestcase):
        width, height, nCabbage = map(int, sys.stdin.readline().rstrip().split())
        fields = [ [ 0 for _ in range(width) ] for _ in range(height) ]
        nWorms = 0
        for _ in range(nCabbage):
            x, y = map(int, sys.stdin.readline().rstrip().split())
            fields[y][x] = 1
        
        for y in range(height):
            for x in range(width):
                if fields[y][x] == 1:
                    fields[y][x] = 0
                    fields = worm_traversal(fields, x, y, width, height)
                    nWorms += 1
                
        print(nWorms)