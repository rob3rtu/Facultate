#include <bits/stdc++.h>
#define mp make_pair
using namespace std;
typedef pair<long long, long long> pii;

vector<pii> poligon;

//0 coliniar, >0 stanga, <0 dreapta
//pozitia lui c fata de (a, b)
long long getDet(pii a, pii b, pii c) {
    return b.first*c.second + a.first*b.second + c.first*a.second - 
           b.first*a.second - a.first*c.second - c.first*b.second;
}

//check if q is on the line (p, r)
bool onSegment(pii p, pii q, pii r) {
    if (q.first <= max(p.first, r.first) && q.first >= min(p.first, r.first) &&
        q.second <= max(p.second, r.second) && q.second >= min(p.second, r.second))
        return true;
    return false;
}

int main() {
    long long n, m, x, y;
    
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> x >> y;
        poligon.push_back(mp(x, y));
    }
    poligon.push_back(poligon[0]);

    cin >> m;
    long long l, r, mid;
    bool ok;
    for(int i = 0; i < m; i++) {
        ok = false;
        cin >> x >> y;
        
        if(getDet(poligon[0], poligon[n - 1], mp(x, y)) == 0 && onSegment(poligon[0], mp(x, y), poligon[n - 1])) {
                cout << "BOUNDARY\n";
                continue;
        }

        if(getDet(poligon[0], poligon[1], mp(x, y)) == 0 && onSegment(poligon[0], mp(x, y), poligon[1])) {
                cout << "BOUNDARY\n";
                continue;
        }

        int last = n - 2, first = 2;
        while(getDet(poligon[0], poligon[last + 1], poligon[last]) == 0) {
            if(getDet(poligon[0], poligon[last], mp(x, y)) == 0 && onSegment(poligon[0], mp(x, y), poligon[last])) {
                cout << "BOUNDARY\n";
                ok = true;
                break;
            }   
            last--;
        }

        while(getDet(poligon[0], poligon[first - 1], poligon[first]) == 0) {
            if(getDet(poligon[0], poligon[first], mp(x, y)) == 0 && onSegment(poligon[0], mp(x, y), poligon[first])) {
                cout << "BOUNDARY\n";
                ok = true;
                break;
            } 
            first++;
        }

        if(ok) continue;

        l = 0; r = n - 1;
        while(r - l > 1) {
            mid = (l + r) / 2;

            if(getDet(poligon[0], poligon[mid], mp(x, y)) < 0) {
                    r = mid;
            } else {
                l = mid;
            }
        }

        if(getDet(poligon[l], poligon[l + 1], mp(x, y)) == 0 && onSegment(poligon[l], mp(x, y), poligon[l + 1])) {
                cout << "BOUNDARY\n";
        } else if(getDet(poligon[l], poligon[l + 1], mp(x, y)) > 0) {
            cout << "INSIDE\n";
        } else {
            cout << "OUTSIDE\n";
        }
    }

    return 0;
}