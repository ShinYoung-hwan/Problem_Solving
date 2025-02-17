import sys

input = lambda : sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input()) # pn의 n
    s_len = int(input()) # s의 길이 m
    s = input() # 비교 대상 문자열
    n_pn = 0 # 찾아낸 pn의 길이
    
    start = 0
    count = 0
    while start < s_len-1:
        if s[start:start+3] == "IOI":
            # "IOI"의 반복된다는 성질을 이용, IOI가 나온 횟수를 이용해 계산
            start += 2
            count += 1
            if count == n:
                # pn과 일치하는 경우로, 이후에 IOI가 반복되면 pn이 1개 더 있는 것
                n_pn += 1
                count -= 1
        else:
            # IOI가 반복되지 않은 경우로, 처음부터 다시 계산
            start += 1
            count = 0
            
    print(n_pn)