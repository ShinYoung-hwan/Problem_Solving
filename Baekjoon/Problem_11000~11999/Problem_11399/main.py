import sys

input = lambda : sys.stdin.readline().rstrip()
    
if __name__ == "__main__":
    n = int(input()) # 인출하는 사람 수
    ps =  [ int(p) for p in input().split() ] # 각 사람의 인출 시간
    ps.sort()

    acculated_sum = [ ps[0] ]
    for i in range(1, len(ps)):
        acculated_sum.append(acculated_sum[i-1] + ps[i])
        
    print(sum(acculated_sum))
    