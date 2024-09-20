import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N, K = map(int, input().split())
    course_length = list(map(int, input().split()))
    
    _sum = 0
    # go forward
    for i in range(N):
        _sum += course_length[i]
        if K < _sum: 
            print(i+1)
            break
    else:
        # go backward
        for i in range(N-1, -1, -1):
            _sum += course_length[i]
            if K < _sum: 
                print(i+1)
                break