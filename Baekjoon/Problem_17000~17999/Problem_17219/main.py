import sys

input = lambda : sys.stdin.readline().rstrip()
inputs = lambda : sys.stdin.readlines()    
    
if __name__ == "__main__":
    n, m = map(int, input().split()) # n개의 사이트, m개의 비밀번호를 찾으려는 사이트 수
    
    password_dict = dict() # key: url, value: password
    
    for _ in range(n):
        url, password = input().split()
        password_dict[url] = password
        
    for _ in range(m):
        url = input()
        print(password_dict[url])