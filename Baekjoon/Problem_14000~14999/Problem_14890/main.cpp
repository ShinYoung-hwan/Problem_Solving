#include <cstdio>
#include <cmath>

const int MAXN = 100;

using namespace std;

int N, L;
int heights[MAXN][MAXN];
int answer = 0;

bool is_valid_row_front(const int r, const int c) {
    int cnt = 1;
    int height = heights[r][c];
    for (int i = c-1; i > -1; i--) {
        if (cnt == L) return true;
        else if (heights[r][i] != height) return false;
        cnt++;
    }
    return cnt == L;
}
bool is_valid_row_back(const int r, const int c) {
    int cnt = 1;
    int height = heights[r][c];
    for (int i = c+1; i < N; i++) {
        if (cnt == L) return true;
        else if (heights[r][i] != height) return false;
        cnt++;
    }
    return cnt == L;
}
void check_row(const int r) {
    bool climed[MAXN] = { false, };

    for (int c = 1; c < N; c++) {
        // 높이가 같은 경우
        if (heights[r][c-1] == heights[r][c]) continue;

        // 높이차가 2이상인 경우
        else if (abs(heights[r][c-1] - heights[r][c]) >= 2) return;

        // 높이차가 1인 경우
        // 오름
        if (heights[r][c-1] < heights[r][c]) {
            if (!is_valid_row_front(r, c-1)) return;
            for (int i = c-1; i > c-1-L; i--) {
                if (climed[i]) return;
                climed[i] = true;
            }
        }
        // 내림
        else {
            if (!is_valid_row_back(r, c)) return;
            for (int i = c; i < c+L; i++) {
                if (climed[i]) return;
                climed[i] = true;
            }
        }
    }

    answer += 1;
    // printf("row %d\n", r);
}

bool is_valid_col_front(const int r, const int c) {
    int cnt = 1;
    int height = heights[r][c];
    for (int i = r-1; i > -1; i--) {
        if (cnt == L) return true;
        else if (heights[i][c] != height) return false;
        cnt++;
    }
    return cnt == L;
}
bool is_valid_col_back(const int r, const int c) {
    int cnt = 1;
    int height = heights[r][c];
    for (int i = r+1; i < N; i++) {
        if (cnt == L) return true;
        else if (heights[i][c] != height) return false;
        cnt++;
    }
    return cnt == L;
}
void check_col(const int c) {
    bool climed[MAXN] = { false, };

    for (int r = 1; r < N; r++) {
        // 높이가 같은 경우
        if (heights[r-1][c] == heights[r][c]) continue;

        // 높이차가 2이상인 경우
        else if (abs(heights[r-1][c] - heights[r][c]) >= 2) return;

        // 높이차가 1인 경우
        // 오름
        if (heights[r-1][c] < heights[r][c]) {
            if (!is_valid_col_front(r-1, c)) return;
            for (int i = r-1; i > r-1-L; i--) {
                if (climed[i]) return;
                climed[i] = true;
            }
        }
        // 내림
        else {
            if (!is_valid_col_back(r, c)) return;
            for (int i = r; i < r+L; i++) {
                if (climed[i]) return;
                climed[i] = true;
            }
        }
    }

    answer += 1;
    // printf("col %d\n", c);
}

int main() {
    scanf("%d %d", &N, &L);
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            scanf("%d", &heights[r][c]);
        }
    }

    for (int i = 0; i < N; i++) {
        check_row(i);
        check_col(i);
    }

    printf("%d\n", answer);
    
    return 0;
}