import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input())
    
    char2int = [ 0 ] * 26
    
    for i in range(N):
        s = input()
        for i in range(len(s)):
            c = s[i]
            char2int[ord(c) - ord('A')] += 10 ** (len(s)-1-i)
    
    char2int.sort(reverse=True)
    
    _sum = 0
    for i in range(10):
        _sum += char2int[i] * (9 - i)
        
    print(_sum)