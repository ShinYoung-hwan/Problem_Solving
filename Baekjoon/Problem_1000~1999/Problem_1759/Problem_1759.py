import sys

input = lambda: sys.stdin.readline().rstrip()

def solve(cur=0, password=[], nVowels=0):
    # base case: 길이를 채우면 확인 후 해결
    if len(password) == L:
        if nVowels >= 1 and len(password) - nVowels >= 2:
            print(''.join(password))
        return
    
    # default case
    for i in range(cur, C):
        password.append(letters[i])
        
        solve(i+1, password, nVowels+1 if letters[i] in {'a', 'e', 'i', 'o', 'u'} else nVowels)
        
        password.pop()
    
if __name__ == "__main__":
    L, C = map(int, input().split())
    letters = sorted(input().split())
    
    solve()
