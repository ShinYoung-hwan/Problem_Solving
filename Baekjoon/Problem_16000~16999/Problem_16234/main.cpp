#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

const int MAXN = 50;
int N, L, R;
int A[MAXN][MAXN];

int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

inline bool isIn(const int r, const int c) { return ( 0 <= r && r < N ) && ( 0 <= c && c < N ); }

void BFS(const int r0, const int c0, bool visited[MAXN][MAXN], int &_sum, vector<pair<int, int> > &_union) {
    queue<pair<int, int> > q;
    q.push({ r0, c0 });
    visited[r0][c0] = true;
    _sum += A[r0][c0];
    _union.push_back({ r0, c0 });

    while (!q.empty()) {
        int r0 = q.front().first, c0 = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int r = r0 + dr[i], c = c0 + dc[i];

            if (!isIn(r, c)) continue;
            else if (visited[r][c]) continue;
            else if (!( (L <= abs(A[r][c] - A[r0][c0])) && (abs(A[r][c] - A[r0][c0]) <= R) )) continue;

            q.push({ r, c });
            visited[r][c] = true;
            _sum += A[r][c];
            _union.push_back({ r, c });
        }
    }
} 

void move(const int _sum, const vector<pair<int, int> > &_union) {
    int n = _sum / _union.size();

    for (auto pos: _union) {
        A[pos.first][pos.second] = n;
    }
}

bool move_population() {
    bool isMove = false;
    bool visited[MAXN][MAXN] = { false };
    
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            if (visited[r][c]) continue;

            int _sum = 0;
            vector<pair<int, int> > _union;
            BFS(r, c, visited, _sum, _union);
            if (_union.size() >= 2) {
                isMove = true;
                move(_sum, _union);
            }
        }
    }

    return isMove;
}

int main() {
    scanf("%d %d %d", &N, &L, &R);
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            scanf("%d", &A[r][c]);
        }
    }

    for (int day = 0; day <= 2000; day++) {
        // 인구이동 실패
        if (!move_population()) {
            printf("%d\n", day);
            break;
        }
    }
    
    return 0;
}