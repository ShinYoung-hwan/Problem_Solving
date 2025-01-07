#include <cstdio>
#include <string>

using namespace std;
const int SIZE = 1001;

string solve(string::iterator &iter) {
    // base
    char head = *iter;
    iter++;
    if (head == 'w' || head == 'b') return string(1, head);

    // default
    string lu = solve(iter);
    string ru = solve(iter);
    string ld = solve(iter);
    string rd = solve(iter);

    return string(1, 'x') + ld + rd + lu + ru;
}

int main(int argc, char **argv) {
    int C; scanf("%d", &C);

    for (int t = 0; t < C; t++) {
        char quadtree_char[SIZE]; scanf("%s", quadtree_char);
        string quadtree = string(quadtree_char);
        string::iterator iter = quadtree.begin();
        printf("%s\n", solve(iter).c_str());
    }

    return 0;
}