import sys

input = lambda: sys.stdin.readline().rstrip()

def get_len_lcs(str1, str2):
    # str1과 str2의 공통 부분 수열 구하기
    lstr1 = len(str1)
    lstr2 = len(str2)
    lcs = [ [ 0 ] * (lstr1+1) for _ in range(lstr2+1) ]
    
    for y in range(1, lstr2+1):
        for x in range(1, lstr1+1):
            if str1[x-1] == str2[y-1]:
                lcs[y][x] = lcs[y-1][x-1] + 1
            else:
                lcs[y][x] = max(lcs[y-1][x], lcs[y][x-1])
    
    return lcs[-1][-1]

if __name__ == "__main__":
    str1 = input()
    str2 = input()
    
    print(get_len_lcs(str1, str2))