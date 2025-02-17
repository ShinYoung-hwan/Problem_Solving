import sys

input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, K, A):
    target_n = M * K # 필요한 연필의 수
    
    ans = 0
    cur_n = 0
    for n_pen in A:
        cur_n += n_pen
        ans += 1
        if cur_n >= target_n:
            return ans
        
    return "STRESS"
    
if __name__ == "__main__":
    N = int(input()) # CTP 회원의 수
    M, K = map(int, input().split()) # M개의 팀, K명의 팀원들
    A = sorted(list(map(int, input().split())), reverse=True) # 각 CTP 회원이 갖고 있는 수
    
    print(solve(N, M, K, A))