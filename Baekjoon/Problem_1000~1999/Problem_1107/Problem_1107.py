import sys

#sys.setrecursionlimit(10**6)

def is_possible(number, living_buttons):
    s_number = str(number)
    for nth_number in s_number:
        if nth_number not in living_buttons:
            return False
    return True
    
if __name__ == "__main__":
    target_channel = int(sys.stdin.readline().rstrip())
    nBroken_buttons = int(sys.stdin.readline().rstrip())
    broken_buttons = set(map(int, sys.stdin.readline().rstrip().split()))
    living_buttons = [str(button) for button in range(10) if button not in broken_buttons]
    
    min_press_num = abs(target_channel-100)
    
    if nBroken_buttons == 10:
        print(min_press_num)
    else:
        for case in range(1000000):
            if is_possible(case, living_buttons):
                cur_press_num = abs(target_channel-case)+len(str(case))
                min_press_num = cur_press_num if cur_press_num < min_press_num else min_press_num
        print(min_press_num)