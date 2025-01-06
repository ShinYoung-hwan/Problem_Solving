#include <cstdio>
#include <set>
#include <algorithm>

using namespace std;

const int NCLOCKS = 16;
const int NBTNS = 10;
const int MAXANS = 1000000;
const set<int> btns[NBTNS] = {
    { 0, 1, 2 },            // 0
    { 3, 7, 9, 11 },        // 1
    { 4, 10, 14, 15 },      // 2
    { 0, 4, 5, 6, 7 },      // 3
    { 6, 7, 8, 10, 12 },    // 4
    { 0, 2, 14, 15 },       // 5
    { 3, 14, 15 },          // 6
    { 4, 5, 7, 14, 15 },    // 7
    { 1, 2, 3, 4, 5 },      // 8
    { 3, 4, 5, 9, 13 }      // 9
};

int clocks[NCLOCKS] = { 0, };

bool is_all_12() {
    for (int i = 0; i < NCLOCKS; i++) {
        if (clocks[i] != 12) return false;
    }
    return true;
}

void push_btn(const int btn) {
    for (auto clock: btns[btn]) {
        clocks[clock] += 3;
        if (clocks[clock] == 15) clocks[clock] = 3;
    }
}

int solve(const int btn=0) {
    // base
    int ret = MAXANS;
    if (btn == NBTNS) return is_all_12() ? 0 : ret;

    // default
    for (int cnt = 0; cnt < 4; cnt++) {
        ret = min(ret, cnt+solve(btn+1));
        push_btn(btn);
    }
    return ret;
}

int main(int argc, char **argv) {
    int C; scanf("%d", &C);

    for (int t = 0; t < C; t++) {
        for (int i = 0; i < NCLOCKS; i++) scanf("%d", &clocks[i]);

        int ans = solve();
        printf("%d\n", ans >= MAXANS ? -1 : ans);
    }

    return 0;
}