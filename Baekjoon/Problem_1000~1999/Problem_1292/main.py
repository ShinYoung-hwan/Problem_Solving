import sys

input = lambda: sys.stdin.readline().rstrip()

def get_sequence(last: int):
    n = 1
    cnt = 1
    seq = [0]
    while True:
        cur = n
        for _ in range(n):
            if cnt > last: return seq
            
            seq.append(cur)
            cnt += 1
        n += 1
        

if __name__ == "__main__":
    A, B = map(int, input().split())
    seq = get_sequence(B)

    print(sum(seq[A:B+1]))