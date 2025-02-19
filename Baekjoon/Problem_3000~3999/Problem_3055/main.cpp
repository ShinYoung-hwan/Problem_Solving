#include <cstdio>
#include <iostream>
#include <queue>
#include <tuple>

using namespace std;
const int SIZE = 50 + 1;
enum { PET='S', WATER='*' };
typedef tuple<int, int, int, int> tiiii;
const int dr[4] = { -1, 1, 0, 0 };
const int dc[4] = { 0, 0, -1, 1 };

int R, C;
char board[SIZE][SIZE];
queue<tiiii> q;

bool is_in(const int r, const int c) {
    return ((0 < r && r <= R)) && (0 < c && c <= C);
}

int bfs() {
    while (!q.empty()) {
        int type, cost, r0, c0; tie(type, cost, r0, c0) = q.front(); q.pop();

        for (int i = 0; i < 4; i++) {
            int r = r0 + dr[i], c = c0 + dc[i];

            if (!is_in(r, c)) continue; // 범위를 벗어난 겨웅
            else if (board[r][c] == 'X') continue; // 벽을 만난 경우
            else if (type == PET && (board[r][c] == WATER || board[r][c] == PET)) continue;
            else if (type == WATER && (board[r][c] == 'D' || board[r][c] == WATER)) continue;
            
            else if (type == PET && board[r][c] == 'D') return cost;

            board[r][c] = type;
            q.push({ type, cost + 1, r, c });
        }
    }
    return -1;
}

int main(void) {
    int sr, sc;

    scanf("%d %d", &R, &C);
    for (int r = 1; r <= R; r++) {
        for (int c = 1; c <= C; c++) {
            scanf(" %1c", &board[r][c]);

            if (board[r][c] == PET) sr = r, sc = c;
            else if (board[r][c] == WATER) q.push({ WATER, 1, r, c });
        }
    }
    q.push({ PET, 1, sr, sc });

    int ret = bfs();
    if (ret == -1) printf("KAKTUS\n");
    else printf("%d\n", ret);
    
    return 0;
}