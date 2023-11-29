#include <iostream>
using namespace std;

int main() {
    int a = 0;
    int b = 0;
    int c = 0;
    int x[9][9];
    int st;


    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            cin >> st;
            x[i][j] = st;


            if (st > a) {
                a = st;
                b = i;
                c = j;
            }
        }
    }


    cout << a << endl;

    cout << b + 1 << " " << c + 1 << endl;

    return 0;
}