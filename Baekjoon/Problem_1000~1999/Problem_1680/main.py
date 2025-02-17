import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    for T in range(int(input())):
        W, N = map(int, input().split()) # 쓰레기차의 용량 W와 지점의 개수 N
        
        trashes = [ tuple(map(int, input().split())) for _ in range(N) ]
        
        total_x = 0
        cur_w = 0
        for i in range(len(trashes)): # 쓰레기장으로부터의 거리 x와 쓰레기의 양 w
            x, w = trashes[i]
            
            # 그 지점의 쓰레기를 실었을 때 쓰레기차의 용량을 넘게 될 때
            # 쓰레기장에 갔다가 다시 온다.
            if cur_w + w > W:
                total_x += 2 * x
                cur_w = 0
            cur_w += w
            
            # 쓰레기 용량이 도달
            if cur_w == W:
                total_x += 2 * x
                cur_w = 0
        
        # 더 이상 쓰레기를 실을 지점이 없을 때 복귀
        if cur_w: total_x += 2*x
        
        print(total_x)
