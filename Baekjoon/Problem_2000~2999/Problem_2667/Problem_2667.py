import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()
inputs = lambda : sys.stdin.readlines()

def is_in_map(pos, n):
    x, y = pos
    return (0 <= x < n) and (0 <= y < n)

def get_House_complex(house_map, n):
    house_complex = [[ 0 for _ in range(n) ] for _ in range(n)] 
    nHouse_in_complex = [ 0, ]
    
    nHouse_complex = 0
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    for start_y in range(n):
        for start_x in range(n):
            # not(집이 존재 and 단지 확인 x) = (not 집애 존재) or (단지가 있음)
            if (not house_map[start_y][start_x]) or (house_complex[start_y][start_x] != 0):
                 continue
            
            nHouse_complex += 1 # == 주택단지 아이디
            queue = deque([(start_x, start_y)])
            house_complex[start_y][start_x] = nHouse_complex
            nHouse_in_complex.append(0)
            
            while(len(queue) != 0):
                cur_x, cur_y = queue.popleft()
                nHouse_in_complex[nHouse_complex] += 1
                
                #print((cur_x, cur_y, nHouse_complex))
                for i in range(4):
                    x, y = cur_x + dx[i], cur_y + dy[i]
                    
                    if not is_in_map((x, y), n):
                        continue
                    
                    if house_complex[y][x] == 0 and house_map[y][x]:
                        queue.append((x, y))
                        house_complex[y][x] = nHouse_complex
    
    return nHouse_complex, sorted(nHouse_in_complex[1:])

if __name__ == "__main__":
    n = int(input())
    house_map = [ [ bool(int(house)) for house in block.rstrip() ] for block in inputs() ]
    
    nHouse_complex, nHouse_in_complex = get_House_complex(house_map, n)
    print(nHouse_complex)
    for nHouse in nHouse_in_complex:
        print(nHouse)
    