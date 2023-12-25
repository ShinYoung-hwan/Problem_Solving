import sys

input = lambda : sys.stdin.readline().rstrip()

if __name__ == "__main__":
    m = int(input())
    s = set()

    for _ in range(m):
        operation = input().split()
        oper_key = operation[0]
        if oper_key == 'all':
            s = set([ i for i in range(1, 21) ])
        elif oper_key == 'empty':
            s = set()
        else:
            element = int(operation[1])
            if oper_key == 'add':
                s.add(element)
            elif oper_key == 'remove':
                s.discard(element)
            elif oper_key == 'check':
                print(1 if element in s else 0)
            else: # oper_key == 'toggle':
                s.remove(element) if element in s else s.add(element)