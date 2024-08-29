#include <cstdio>
#include <queue>
#include <deque>
#include <set>
#include <utility>

using namespace std;

enum { RIGHT, UP, LEFT, DOWN };

inline int turn(const int dir, const char C) {
    return C == 'L' ? (dir + 1) % 4 : ( dir == 0 ? 3 : dir - 1 );
}

inline bool inBoard(const int r, const int c, const int N) {
    return (0 < r && r <= N) && (0 < c && c <= N);
}

pair<int, int> get_next_pos(const int r0, const int c0, const int dir) {
    int r = r0, c = c0;
    switch (dir) {
        case RIGHT:
            c++;
            break;
        case UP:
            r--;
            break;
        case LEFT:
            c--;
            break;
        case DOWN:
            r++;
            break;
    }

    return { r, c };
}


int main() {
    int N; scanf("%d", &N);
    int K; scanf("%d", &K);
    
    set<pair<int, int> > apples;
    for (int i = 0; i < K; i++) {
        int r, c; scanf("%d %d", &r, &c);
        apples.insert({ r, c });
    }

    int L; scanf("%d", &L);
    deque<pair<int, char> > cmds;
    for (int i = 0; i < L; i++) {
        int X; char C; scanf("%d %c", &X, &C);
        cmds.push_front({ X, C });
    }

    // solve
    int time = 0, dir = RIGHT;
    deque<pair<int, int> > snack;
    set<pair<int, int> > snack_pos;

    snack.push_back({ 1, 1 });
    snack_pos.insert({ 1, 1 });

    while (true) {
        // 방향 전환
        if (!cmds.empty() && cmds.back().first == time) {
            char C = cmds.back().second;
            cmds.pop_back();
            dir = turn(dir, C);
        }

        // 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
        pair<int, int> next = get_next_pos(snack.back().first, snack.back().second, dir);
        snack.push_back(next);

        // 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
        if (!inBoard(next.first, next.second, N) || snack_pos.find(next) != snack_pos.end()) break;

        // 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
        if (apples.find(next) != apples.end()) {
            apples.erase(next);
        }
        // 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
        else {
            snack_pos.erase(snack.front());
            snack.pop_front();
        }

        snack_pos.insert(next);
        time++;
    }

    printf("%d\n", time+1);
    return 0;
}