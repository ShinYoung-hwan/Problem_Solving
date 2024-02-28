import sys

input = lambda: sys.stdin.readline().rstrip()

def get_lcs(str1, str2):
    lstr1 = len(str1)
    lstr2 = len(str2)

    lcs = [ [ "" ] * (lstr1 + 1) for _ in range(lstr2 + 1) ]
    
    for i in range(1, lstr2 + 1):
        for j in range(1, lstr1 + 1):
            if str1[j-1] == str2[i-1]:
                lcs[i][j] = lcs[i-1][j-1] + str1[j-1]
            else:
                lcs[i][j] = lcs[i-1][j] if len(lcs[i-1][j]) > len(lcs[i][j-1]) else lcs[i][j-1]
    
    # print(*["   "] + list(str1))
    # for i in range(lstr2+1):
    #     print(([" "] + list(str2))[i], end=' ')
    #     print(*lcs[i])
        
    return lcs[-1][-1]

if __name__ == "__main__":
    str1, str2 = input(), input()
    
    lcs = get_lcs(str1, str2)
    
    print(len(lcs))
    print(lcs)