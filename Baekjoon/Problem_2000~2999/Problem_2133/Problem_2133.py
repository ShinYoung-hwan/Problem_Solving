import sys

input = lambda: sys.stdin.readline().rstrip()

sum_of_sequence = [ 1 ] + [ 0 ] * 14
sequence = [ 1, 3, 11 ] + [ 0 ] * 14

def get_element_of_sum_of_sequence(N):
    # base
    if sum_of_sequence[N]: return sum_of_sequence[N]
    
    # default
    sum_of_sequence[N] = get_element_of_sum_of_sequence(N-1) + get_element_of_sequence(N)
    return sum_of_sequence[N]

def get_element_of_sequence(N):
    # base
    if sequence[N]: return sequence[N]
    
    # default
    sequence[N] = get_element_of_sequence(N-1) * get_element_of_sequence(1) + 2 * get_element_of_sum_of_sequence(N-2)
    return sequence[N]

if __name__ == "__main__":
    N = int(input())
    if N % 2:
        print(0)
    else:
        print(get_element_of_sequence(N//2))
    