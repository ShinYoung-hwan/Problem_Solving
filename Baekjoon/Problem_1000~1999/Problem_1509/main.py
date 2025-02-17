import sys

input = lambda: sys.stdin.readline().rstrip()

def set_palindrome_matrix(is_p, s, s_len):
    def _is_palindrome(left, right):
        # 이미 값이 정해진 경우
        if is_p[left][right] != -1: return is_p[left][right]
    
        # 아직 값이 정해지지 않은 경우
        if s[left] == s[right]: is_p[left][right] = _is_palindrome(left+1, right-1)
        else: is_p[left][right] = 0
        
        return is_p[left][right]
    # step 1: 길이가 1인 경우
    for i in range(s_len):
        is_p[i][i] = 1
    
    # step 2: 길이가 2인 경우
    for i in range(s_len-1):
        is_p[i][i+1] = 1 if s[i] == s[i+1] else 0
            
    # step 3: 길이가 3 이상인 경우
    for i in range(s_len):
        for j in range(i+2, s_len):
            _is_palindrome(i, j) # set palindrome

if __name__ == "__main__":
    s = input()
    s_len = len(s)
    
    # palindrome setting
    is_p = [ [ -1 ] * s_len for _ in range(s_len) ] # is_p[i][j]: s[i:j+1]가 palindrome
    set_palindrome_matrix(is_p, s, s_len)
    
    # solve
    dp = [ i+1 for i in range(s_len+1) ] # dp[i]: s[:i+1]까지 palindrome의 최소 개수
    dp[-1] = 0 # buffer
    for end in range(s_len):
        for start in range(end+1):
            if is_p[start][end] == 1: # 팰린드롬인 경우
                dp[end] = min(dp[end], dp[start - 1] + 1)
            else: # 팰린드롬이 아닌 경우
                dp[end] = min(dp[end], dp[end-1] + 1)
    
    print(dp[s_len - 1])