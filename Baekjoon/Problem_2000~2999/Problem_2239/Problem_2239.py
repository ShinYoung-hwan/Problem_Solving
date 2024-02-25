import sys

input = lambda: sys.stdin.readline().rstrip()
inputs = lambda: sys.stdin.readlines()

res = None
N = 9

def get_candidates(sdoku, r0, c0):
    rows = set(sdoku[r0])
    cols = set([ sdoku[r][c0] for r in range(N) ])
    nr, nc = (r0 // 3) * 3, (c0 // 3) * 3
    areas = set([ sdoku[r][c] for c in range(nc, nc+3) for r in range(nr, nr+3) ])
    union_set = rows.union(cols).union(areas)
    
    candidates = sorted(list(set(range(1, 10)).difference(union_set)))
    
    return candidates

def solve(sdoku: list, rest):
    global res
    
    # for line in sdoku:
    #     print(*line)
    # print()
    
    if rest == 0:
        res = sdoku
        return True
    
    for r in range(N):
        for c in range(N):
            if sdoku[r][c] != 0: continue

            candidates = get_candidates(sdoku, r, c)\
            # 
            if len(candidates) == 0:
                return False
            
            for candidate in candidates:
                sdoku[r][c] = candidate
                if solve(sdoku, rest-1):
                    return True
                sdoku[r][c] = 0
                
            if sdoku[r][c] == 0:
                return False    

if __name__ == "__main__":
    sdoku = [ [ int(e) for e in line.rstrip() ] for line in inputs() ]
    rest = 0
    for r in range(N):
        for c in range(N):
            if sdoku[r][c] != 0: continue
            rest += 1
    
    solve(sdoku, rest)
    
    for r in range(N):
        for c in range(N):
            print(sdoku[r][c], end='')
        print()