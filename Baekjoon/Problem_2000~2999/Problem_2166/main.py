import sys
input = lambda: sys.stdin.readline().rstrip()
                
if __name__ == "__main__":
    n = int(input())
    
    polygon = []
    for _ in range(n):
        x, y = map(int, input().split())
        polygon.append((x, y))
    polygon.append(polygon[0])
    
    xy = 0
    yx = 0
    for i in range(n):
        xy += polygon[i][0] * polygon[i+1][1]
        yx += polygon[i][1] * polygon[i+1][0]
    
    print(round(abs((xy - yx) / 2), 1))
    