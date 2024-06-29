import sys

input = lambda: sys.stdin.readline().rstrip()

def get_max_common_number(A, B):
    A, B = sorted(A), sorted(B)
    
    while A[-1] != B[-1]:
        if A[-1] > B[-1]: 
            A.pop()
        else:
            B.pop()
            
    return A[-1]
    
def get_LCS(A, B):
    LCSs = []
    LCS_maxrix = []
    def _get_LCS_matrix():
        
    
    print(A)
    print(B)
    
    for ai in range(len(A)):
        LCS = [ A[0] ]
        for bi in range(len(B)):
            
        
            

    return LCSs

if __name__ == "__main__":
    N = int(input())
    A = [0] + list(map(int, input().split()))
    M = int(input())
    B = [0] + list(map(int, input().split()))
    
    if N == 0: ...
    if M == 0: ...
    
    max_common_number = get_max_common_number(A, B)
    print(max_common_number)
    
    all_max_A_index = list(filter(lambda x: A[x] == max_common_number, range(N)))
    all_max_B_index = list(filter(lambda x: B[x] == max_common_number, range(M)))
    
    LCSs = list()
    for max_A_index in all_max_A_index:
        for max_B_index in all_max_B_index:
            LCSs + get_LCS(A[max_A_index:], B[max_B_index:])
    
    LCSs.sort()
    print(LCSs)
    print(len(LCSs[-1]))
    print(*LCSs[-1])