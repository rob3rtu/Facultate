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


double intersectionPointX(pii a, pii b, pii c, pii d) {
    // Line AB represented as a1x + b1y = c1
    double a1 = b.second - a.second;
    double b1 = a.first - b.first;
    double c1 = a1*(a.first) + b1*(a.second);
 
    // Line CD represented as a2x + b2y = c2
    double a2 = d.second - c.second;
    double b2 = c.first - d.first;
    double c2 = a2*(c.first)+ b2*(c.second);
 
    double determinant = a1*b2 - a2*b1;
 
    return (b2*c1 - b1*c2)/determinant;
}

//check if q is on the line (p, r)
bool onSegment(pii p, pii q, pii r) {
    if (q.first <= max(p.first, r.first) && q.first >= min(p.first, r.first) &&
        q.second <= max(p.second, r.second) && q.second >= min(p.second, r.second))
        return true;
    return false;
}

int main() {
    long long n, m, x, y, drMax = 0;
    
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> x >> y;
        drMax = max(drMax, x);
        poligon.push_back(mp(x, y));
    }
    //to complete the cycle
    poligon.push_back(poligon[0]);


    int cnt = 0;
    pii p1, p2;

    cin >> m;
    for(int i = 0; i < m; i++) {
        cin >> x >> y;
        cnt = 0;

        //for every edge in the poligon
        for(int j = 0; j < n; j++) {
            p1 = poligon[j];
            p2 = poligon[j + 1];

            if(getDet(p1, p2, mp(x, y)) == 0 && onSegment(p1, mp(x, y), p2)) {
                cout << "BOUNDARY\n";
                cnt = -1;
                break;
            }

            if((p1.second < y && p2.second < y) 
                || (p1.second >= y && p2.second >= y))
                    continue;

            if(intersectionPointX(p1, p2, mp(x, y), mp(drMax + 2, y)) > x)
                cnt++;
        }

        // cout << "\n------\n" << cnt <<"\n------\n";
        if(cnt != -1) 
            cout << (cnt % 2 == 0 ? "OUTSIDE\n" : "INSIDE\n");
    }

    return 0;
}