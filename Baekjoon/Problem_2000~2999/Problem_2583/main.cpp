#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
#include <utility>

const int MAXM = 100, MAXN = 100;
const int dr[4] = { -1, 1, 0, 0 };
const int dc[4] = { 0, 0, -1, 1 };

using namespace std;

inline bool inBoard(const int r, const int c, const int M, const int N) {
    return (0 <= r && r < M) && (0 <= c && c < N);
}


int bfs(const int board[MAXM][MAXN], bool visited[MAXM][MAXN], const int M, const int N, const int r0, const int c0) {
    queue<pair<int, int> > q;
    q.push({ r0, c0 });
    visited[r0][c0] = true;
    int cnt = 1;

    while (!q.empty()) {
        int r0 = q.front().first, c0 = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int r = r0 + dr[i], c = c0 + dc[i];

            if (!inBoard(r, c, M, N)) continue;
            else if (board[r][c]) continue;
            else if (visited[r][c]) continue;

            q.push({ r, c });
            visited[r][c] = true;
            cnt++;
        }
    }

    return cnt;
}

int main() {
    int M, N, K; scanf("%d %d %d", &M, &N, &K);

    // set data
    int board[MAXM][MAXN] = { 0, };
    for (int i = 0; i < K; i++) {
        int ldx, ldy, rux, ruy; scanf("%d %d %d %d", &ldx, &ldy, &rux, &ruy);

        for (int r = ldy; r < ruy; r++) {
            for (int c = ldx; c < rux; c++) {
                board[r][c] = 1;
            }
        }
    }

    // solve
    bool visited[MAXM][MAXN] = { false, };

    vector<int> cnts;
    for (int r = 0; r < M; r++) {
        for (int c = 0; c < N; c++) {
            if (board[r][c]) continue;
            else if (visited[r][c]) continue;

            cnts.push_back(bfs(board, visited, M, N, r, c));
        }
    }

    // print output
    sort(cnts.begin(), cnts.end());
    printf("%zu\n", cnts.size());
    for (int cnt: cnts) {
        printf("%d ", cnt);
    }
    printf("\n");

    return 0;
}