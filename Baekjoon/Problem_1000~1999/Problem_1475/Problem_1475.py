import sys

input = lambda: sys.stdin.readline().rstrip()
    
if __name__ == "__main__":
    N = [ int(n) for n in input()]

    counts = [ 0 ] * 10
    for n in N:
        cur = n
        
        # 6과 9 balancing
        if (cur == 6 or cur == 9) :
            if (counts[6] > counts[9]): cur = 9
            else: cur = 6
        
        counts[cur] += 1
        
    print(max(counts))