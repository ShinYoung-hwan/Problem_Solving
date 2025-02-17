#include <cstdio>
#include <vector>
#include <queue>
#include <tuple>
#include <utility>
#include <algorithm>

using namespace std;

const int MAXRC = 300;
int R, C;
int heights[MAXRC][MAXRC] = { 0, };
int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

void BFS(int r0, int c0, bool visited[MAXRC][MAXRC], vector<tuple<int, int, int> > &schedules) {
    queue<pair<int ,int> > q;
    q.push({ r0, c0 });
    visited[r0][c0] = true;

    while (!q.empty()) {
        r0 = q.front().first, c0 = q.front().second;
        q.pop();

        int cnt_sea = 0;
        for (int i = 0; i < 4; i++) {
            int r = r0 + dr[i], c = c0 + dc[i];

            if (heights[r][c] == 0) {
                cnt_sea++;
                continue;
            } else if (visited[r][c]) continue;

            q.push({ r, c });
            visited[r][c] = true;
        }
        if (cnt_sea) schedules.push_back({ r0, c0, cnt_sea });
    }

}

void melt(vector<tuple<int, int, int> > &schedules) {
    int r, c, a;
    for (auto e: schedules) {
        tie(r, c, a) = e;
        heights[r][c] = max(0, heights[r][c] - a);
    }
}

int solve() {
    int year = 0;
    while (true) {
        vector<tuple<int, int, int> > schedules;
        bool visited[MAXRC][MAXRC] = { false, };

        int cnt = 0;
        for (int r = 1; r < R-1; r++) {
            for (int c = 1; c < C-1; c++) {
                if (heights[r][c] == 0) continue;
                else if (visited[r][c]) continue;
                BFS(r, c, visited, schedules);
                cnt++;
            }
        }
        
        if (cnt > 1) return year;
        else if (cnt == 0) return 0;
        melt(schedules);
        year++;
    }
}

int main() {
    scanf("%d %d", &R, &C);
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            scanf("%d", &heights[r][c]);
        }
    }
    printf("%d", solve());
    
    return 0;
}