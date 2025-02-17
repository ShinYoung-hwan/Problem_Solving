import sys

input = lambda : sys.stdin.readline().rstrip()

def get_n_oper_to_one(n: int):
    items = [ 0 ] * (n+1)
    
    for i in range(2, n+1):
        items[i] = items[i-1]+1
        if i % 2 == 0:
            items[i] = min(items[i], items[i//2]+1)
        if i % 3 == 0:
            items[i] = min(items[i], items[i//3]+1)
        #print(i, items)
    return items

if __name__ == "__main__":
    
    n = int(input())
    items = get_n_oper_to_one(n)
    print(items[n])