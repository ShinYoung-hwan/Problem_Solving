import sys

def get_required_n_blocks(blocks, height):
    output = 0
    for y in blocks:
        for x in y:
            output += height - x
            
    return 0 if output < 0 else output

def get_required_time(blocks, height):
    output = 0
    for y in blocks:
        for x in y:
            if x < height:
                output += (height - x)
            elif x > height:
                output += 2 * (x - height)
    return output

if __name__ == "__main__":
    depth, width, nBlocks = map(int, sys.stdin.readline().rstrip().split())
    blocks = [ list(map(int, line.rstrip().split())) for line in sys.stdin.readlines() ]
    
    req_time = 500*500*256
    proper_height = 0
    for height in range(256+1):
        cur_time = get_required_time(blocks, height)
        cur_blocks = get_required_n_blocks(blocks, height)
        if cur_blocks > nBlocks:
            break
        if cur_time > req_time:
            break
        
        req_time = cur_time
        proper_height = height
        
    print(req_time, proper_height)