#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;
const int SIZE = 51;
const int dr[4] = { -1, 1, 0, 0 };
const int dc[4] = { 0, 0, -1, 1 };

int N, M;
char board[SIZE][SIZE];
bool visited[SIZE][SIZE];
int n_descendants[SIZE][SIZE];

inline bool is_in(const int r, const int c) {
    return ((0 < r) && (r <= N)) && ((0 < c) && (c <= M));
}

int dfs(const int r0 = 1, const int c0 = 1) {
    int w = board[r0][c0] - '0';
    for (int i = 0; i < 4; i++) {
        int r = r0 + w * dr[i], c = c0 + w * dc[i];

        if (!is_in(r, c)) continue;
        else if (board[r][c] == 'H') continue;
        else if (visited[r][c]) return -1;
        else if (n_descendants[r][c] != 0 && n_descendants[r0][c0] > n_descendants[r][c]) continue;

        visited[r][c] = true;
        int ret = dfs(r, c);
        visited[r][c] = false;
        if (ret == -1) return -1;

        n_descendants[r0][c0] = max(n_descendants[r0][c0], ret);
    }
    return n_descendants[r0][c0] + 1;
}

int main(void) {
    scanf("%d %d", &N, &M);
    for (int r = 1; r <= N; r++) {
        for (int c = 1; c <= M; c++) scanf(" %1c", &board[r][c]);
    }

    visited[1][1] = true;
    printf("%d\n", dfs());

    return 0;
}