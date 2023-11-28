import sys

input = lambda : sys.stdin.readline()
inputs = lambda : sys.stdin.readlines()

def get_max_stairs_sum(stairs, nStairs):
    if nStairs <= 2:
        return sum(stairs)
    
    sum_stairs = [stairs[0], sum(stairs[:2]), max(stairs[0]+stairs[2], stairs[1]+stairs[2])]
    
    for i in range(3, nStairs):
        sum_stairs.append(max(sum_stairs[i-3] + stairs[i-1] + stairs[i], sum_stairs[i-2] + stairs[i]))

    return sum_stairs[nStairs-1]

if __name__ == "__main__":
    nStairs = int(input().rstrip())
    stairs = [ int(stair.rstrip()) for stair in inputs() ]

    print(get_max_stairs_sum(stairs, nStairs))