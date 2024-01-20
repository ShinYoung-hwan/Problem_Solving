import sys

# from itertools import permutations

def permutations(numbers, r, visited=[], ans=[]):
    # n개의 원소를 갖는 numbers에서 r개를 순열로 뽑기

    if len(visited) == r:
        ans.append(list(visited))
    
    for number in numbers:
        if number not in visited:
            visited.append(number)
            permutations(numbers, r, visited, ans)
            visited.pop()
    
    return ans

input = lambda: sys.stdin.readline().rstrip()
    
if __name__ == "__main__":
    n, m = map(int, input().split()) # n개의 자연수 중 m개를 고르는 문제
    numbers = sorted([ int(number) for number in input().split() ]) # n개의 자연수
    
    for ai in permutations(numbers, m):
        print(*ai)
    