import sys

input = lambda: sys.stdin.readline().rstrip()

def set_palindrome(numbers, n):
    global palindrome
    # 1개부터 확인
    for i in range(n):
        palindrome[i][i] = 1
        for j in range(n):
            if (s:=i-j) >= 0 and (e:=i+j) < n and numbers[s] == numbers[e]:
                palindrome[s][e] = 1
            else: break
    
    # 2개부터 확인
    for i in range(n-1):
        if numbers[i] == numbers[i+1]:
            palindrome[i][i+1] = 1
            for j in range(n):
                if (s:=i-j) >= 0 and (e:=i+1+j) < n and numbers[s] == numbers[e]:
                    palindrome[s][e] = 1
                else: break

if __name__ == "__main__":
    n = int(input()) # 수열의 크기 n
    numbers = input().split() # n개의 수
    
    palindrome = [ [ 0 ] * n for _ in range(n) ]
    set_palindrome(numbers, n)
    
    m = int(input()) # 질문의 개수 m
    for _ in range(m):
        s, e = map(int, input().split()) # numbers[s:e]가 팰린드롬인지
        print(palindrome[s-1][e-1])