import sys

if __name__ == "__main__":
    nNumbers = int(sys.stdin.readline().rstrip())
    sequence = [ int(element.rstrip()) for element in sys.stdin.readlines() ] # bottom -> list <- top
    tmp = list()
    output = list()
    res = list()
    push_target = nNumbers
    is_break = False
    
    while push_target != 0:
        if is_break:
            break
        is_break = True
        
        # pop sequence ->tmp
        if len(tmp) != 0 and tmp[-1] == push_target:
            output.append(tmp.pop())
            res.append('+')
            push_target -= 1
            is_break = False
        # push tmp -> output    
        else:
            if len(sequence) == 0:
                continue
            tmp.append(sequence.pop())
            res.append('-')
            is_break = False

            
    if is_break:
        print('NO')
    else:
        for ans in list(reversed(res)):
            print(ans)