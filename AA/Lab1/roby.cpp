#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;

int getDet(pii a, pii b, pii c) {
    return b.first*c.second + a.first*b.second + c.first*a.second - 
           b.first*a.second - a.first*c.second - c.first*b.second;
}

vector<pii> points;

int main() {
    int n, x, y;
    int left = 0, right = 0, touch = 0;

    for(cin >> n; n; n--) {
        cin >> x >> y;
        points.push_back(make_pair(x, y));
    }

    pii first = points[0], second = points[1], third;
    int i = 2, det;

    while(i < points.size()) {
        third = points[i];

        det = getDet(first, second, third);

        if(det > 0) left++;
        else if(det < 0) right++;
        else touch++;

        first = second;
        second = third;
        i++;
    }

    third = points[0];
    det = getDet(first, second, third);

    if(det > 0) left++;
    else if(det < 0) right++;
    else touch++;

    cout << left << " " << right << " " << touch << '\n';

    return 0;
}