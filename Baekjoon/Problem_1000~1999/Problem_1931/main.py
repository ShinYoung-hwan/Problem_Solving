import sys

input = lambda : sys.stdin.readline().rstrip()
inputs = lambda : sys.stdin.readlines()

if __name__ == "__main__":
    nMeetings = int(input())
    meetings = list(sorted(map(lambda meeting: list(map(int, meeting.rstrip().split())) ,inputs())))

    time_line = list()
    time_line.append(meetings[0])

    for idx in range(1, nMeetings):
        cur_meeting = meetings[idx]
        # 만약 좀 더 좋은 케이스가 있을 경우 최신화
        if time_line[-1][1] > cur_meeting[1] and time_line[-1][0] <= cur_meeting[0]:
            time_line.pop()
            time_line.append(cur_meeting)
        # 다음 미팅으로 적합하다고 판단될 경우 삽입
        elif time_line[-1][1] <= cur_meeting[0]:
            time_line.append(cur_meeting)        
            
    print(len(time_line))
    