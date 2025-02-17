import sys

input = lambda: sys.stdin.readline().rstrip()
inputs = lambda: sys.stdin.readlines()

if __name__ == "__main__":
    M, N = map(int, input().split()) # 선거인원의 수 M, 선거후보의 수 N
    
    all_election_result = [ 0 for _ in range(N+1) ]
    points = list(range(N-1, -1, -1))
    # M lines, N numbers
    for _ in range(M):
        vote = map(int, input().split()) # 선거인원의 선거 결과
        for i, v in enumerate(vote): # 우선순위: 선거후보
            all_election_result[v] += points[i]
            
    max_election_value = max(all_election_result)
    # print(all_election_result)
    for winner in filter(lambda i: all_election_result[i] == max_election_value, range(1, N+1)):
        print(winner)