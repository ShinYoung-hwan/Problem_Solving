import sys

input = lambda : sys.stdin.readline().rstrip()
inputs = lambda : sys.stdin.readlines()

def get_nBlocks(ground, height):
    # ground에서 height로 만드는데 필요한 블록의 개수, 양수는 필요한 개수, 음수는 얻게되는 개수
    return sum([ sum([ height - cur_h for cur_h in side ]) for side in ground ])

def get_time(ground, height):
    return sum([ sum([ ((height-cur_h) if (height-cur_h) >= 0 else -2*(height-cur_h)) for cur_h in side ]) for side in ground ])

def get_max_possible_height(ground, nBlocks):
    s, e = 0, 256
    mid = (s+e) // 2
    
    while s <= e:
        cur_nBlocks = get_nBlocks(ground, mid)
        if cur_nBlocks > nBlocks:
            # 보유량보다 많은 경우는 유효 케이스가 아님.
            e = mid - 1
        else:
            s = mid + 1
        mid = (s+e) // 2
        
    return mid

def solve(ground, nBlocks):
    # 이진 탐색 알고리즘을 통한 최적의 높이 구하기
    proper_height = 0
    min_time = get_time(ground, 0)
    
    s, e = 0, get_max_possible_height(ground, nBlocks)
    mid = (s+e) // 2
    
    while s <= e:
        cur_time = get_time(ground, mid)
        prev_time = get_time(ground, mid-1)
        next_time = get_time(ground, mid+1)
        
        proper_height = mid
        min_time = cur_time
        if prev_time < cur_time < next_time:
            e = mid - 1
        elif prev_time >= cur_time >= next_time:
            s = mid + 1
        else:
            break

        mid = (s+e) // 2

    return min_time, proper_height
    
if __name__ == "__main__":
    n, m, b = map(int, input().split()) # n: 세로, m: 가로, b: 인벤토리 내 블록의 개수
    ground = [ list(map(int, line.split())) for line in inputs() ]
    
    print(*solve(ground, b))