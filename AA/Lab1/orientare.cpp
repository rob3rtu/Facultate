#include <bits/stdc++.h>
using namespace std;

int main() {
    long long t, xp, yp, xq, yq, xr, yr;

    for(cin >> t; t; t--) {
        cin >> xp >> yp >> xq >> yq >> xr >> yr;

        long long det = xq*yr + xp*yq + xr*yp - xq*yp - xp*yr - xr*yq;

        cout << ((det > 0) ? "LEFT\n" : (det < 0 ? "RIGHT\n" : "TOUCH\n"));
    }

    return 0;
}