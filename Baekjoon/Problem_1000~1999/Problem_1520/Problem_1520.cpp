#include <cstdio>
#include <unordered_set>
#include <algorithm>
#include <utility>

const int MAXRC = 500;

using namespace std;

int R, C; 
int dp[MAXRC][MAXRC];
int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

inline bool isIn(const int r, const int c) {
    return (0 <= r && r < R) && (0 <= c && c <= C);
}

int DFS(const int board[MAXRC][MAXRC], const int r0, const int c0, vector<pair<int, int> > &visited) {
    // base
    if (dp[r0][c0] >= 0) {
        return dp[r0][c0];
    }

    // default
    int cnt = 0;
    for (int i = 0; i < 4; i++) {
        int r = r0 + dr[i], c = c0 + dc[i];

        if (!isIn(r, c)) continue;
        else if (!visited.empty() && visited.back().first == r && visited.back().second == c) continue;
        else if (board[r0][c0] <= board[r][c]) continue;
        else if (dp[r][c] == 0) continue;

        visited.push_back({ r, c });
        cnt += DFS(board, r, c, visited);
        visited.pop_back();
    }
    dp[r0][c0] = cnt;
    return dp[r0][c0];
}

int main() {
    scanf("%d %d", &R, &C);

    int board[MAXRC][MAXRC];
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            scanf("%d", &board[r][c]);
            dp[r][c] = -1;
        }
    }
    dp[R-1][C-1] = 1;

    vector<pair<int, int> > visited;
    DFS(board, 0, 0, visited);

    printf("%d\n", dp[0][0]);
    
    return 0;
}